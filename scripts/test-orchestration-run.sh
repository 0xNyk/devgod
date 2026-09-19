#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
V="$ROOT/scripts/validate-orchestration-run.py"
S="$ROOT/templates/agentic/orchestration-run.sample.json"
T="$(mktemp -d)"
trap 'rm -rf "$T"' EXIT
python3 "$V" "$S" >/dev/null
cp "$ROOT/templates/agentic/orchestration-contract.sample.json" "$T/orchestration-contract.sample.json"
cp -R "$ROOT/templates/agentic/orchestration-run-evidence" "$T/orchestration-run-evidence"
python3 - "$S" "$T/captured.json" "$T/orchestration-contract.sample.json" <<'PY'
import hashlib
import json
import pathlib
import sys
contract_path=pathlib.Path(sys.argv[3])
contract=json.loads(contract_path.read_text())
contract['receipt_kind']='captured_contract'
contract['review']['approved']=True
contract_path.write_text(json.dumps(contract,indent=2))
d=json.load(open(sys.argv[1]))
d['run']['contract_sha256']=hashlib.sha256(contract_path.read_bytes()).hexdigest()
d['receipt_kind']='captured_run'
d['review']['approved']=True
d['decision']={'outcome':'pass','reasons':['Captured run satisfied the bound contract.'],'unresolved_risks':[]}
json.dump(d,open(sys.argv[2],'w'),indent=2)
PY
python3 "$V" "$T/captured.json" >/dev/null
mutate() {
  local name="$1" expression="$2"
  python3 - "$T/captured.json" "$T/$name.json" "$expression" <<'PY'
import json
import sys
d=json.load(open(sys.argv[1]))
exec(sys.argv[3],{'d':d})
json.dump(d,open(sys.argv[2],'w'),indent=2)
PY
  if python3 "$V" "$T/$name.json" >/dev/null 2>&1; then
    echo "expected rejection: $name" >&2
    exit 1
  fi
}
mutate forged_contract 'd["run"]["contract_sha256"]="0"*64'
mutate forged_artifact 'd["artifacts"][0]["sha256"]="0"*64'
mutate sensitive_trace 'd["trace"]["include_sensitive_data"]=True'
mutate incomplete_trace 'd["trace"]["complete"]=False'
mutate missing_worker 'd["workers"]=d["workers"][:-1]'
mutate unreleased_lease 'd["workers"][1]["lease_released"]=False'
mutate worker_overspend 'd["workers"][1]["cost_usd"]=2.0'
mutate success_without_artifact 'd["workers"][1]["output_artifact_id"]="art_ui"'
mutate undeclared_tool 'd["spans"][5]["tool"]="deploy"'
mutate undeclared_destination 'd["spans"][8]["destination"]="https://example.invalid"'
mutate cross_lane_write 'd["spans"][10]["write_lane"]="artifacts/code"'
mutate missing_approval 'd["spans"][8]["approval"]=None'
mutate broken_parent 'd["spans"][5]["parent_span_id"]="missing"'
mutate missing_handoff 'd["spans"]=[s for s in d["spans"] if s["span_id"]!="span_handoff_ui"]; [s.update(seq=i+1) for i,s in enumerate(d["spans"])]'
mutate wrong_join 'd["join"]["participants"]=["code_worker"]'
mutate missing_provenance 'd["synthesis"]["provenance"].pop("req_ui")'
mutate self_verification 'd["synthesis"]["verifier"]="manager"'
mutate self_review 'd["review"]["reviewer"]="manager"'
mutate infrastructure_pass 'd["run"]["infrastructure_errors"]=["trace exporter dropped spans"]'
mutate unresolved_pass 'd["decision"]["unresolved_risks"]=["worker state uncertain"]'
mutate illustrative_pass 'd["receipt_kind"]="illustrative_fixture"'
mutate legacy_schema 'd["schema_version"]=1'
mutate missing_model_identity 'd["workers"][1].pop("execution")'
mutate silent_model_change 'd["workers"][1]["execution"]["model"]="other-model"'
mutate wrong_host 'd["workers"][1]["execution"]["host"]="other-host"'
mutate changed_effort 'd["workers"][1]["execution"]["reasoning_effort"]="high"'
mutate missing_model_evidence 'd["workers"][1]["execution"]["evidence_ref"]=""'
mutate nonfinite_worker_cost 'd["workers"][1]["cost_usd"]=float("nan")'
mutate nonfinite_span_cost 'd["spans"][5]["cost_usd"]=float("nan")'
mutate worker_timeout 'd["workers"][1]["ended_at"]="2026-07-15T04:06:00+00:00"'
mutate malformed_model_identity 'd["workers"][1]["execution"]=[]'
python3 - "$T" "$V" <<'PY'
import hashlib
import json
import pathlib
import subprocess
import sys

root=pathlib.Path(sys.argv[1])
contract=json.loads((root/'orchestration-contract.sample.json').read_text())
receipt=json.loads((root/'captured.json').read_text())
for name in ('concurrency', 'illustrative_contract'):
    changed=json.loads(json.dumps(contract))
    if name=='concurrency':
        changed['limits']['max_concurrent_agents']=2
        expected='observed concurrency exceeds contract'
    else:
        changed['receipt_kind']='illustrative_fixture'
        changed['review']['approved']=False
        expected='passing run requires a captured contract'
    path=root/f'{name}-contract.json'
    path.write_text(json.dumps(changed))
    receipt['run']['contract_path']=path.name
    receipt['run']['contract_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    run=root/f'{name}-run.json'
    run.write_text(json.dumps(receipt))
    result=subprocess.run([sys.executable,sys.argv[2],str(run)],capture_output=True,text=True)
    assert result.returncode==1 and expected in result.stdout, result.stdout+result.stderr
PY
echo "orchestration run fixtures passed"
