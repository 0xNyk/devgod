#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
V="$ROOT/scripts/validate-orchestration-contract.py"
S="$ROOT/templates/agentic/orchestration-contract.sample.json"
T="$(mktemp -d)"
trap 'rm -rf "$T"' EXIT
python3 "$V" "$S" >/dev/null
python3 - "$S" "$T/captured.json" <<'PY'
import json
import sys
d=json.load(open(sys.argv[1]))
d['receipt_kind']='captured_contract'
d['review']['approved']=True
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
mutate cycle 'd["delegations"].append({"from":"code_worker","to":"manager","task_id":"task_cycle","input_refs":["x"],"context_allowlist":["goal"],"authority_tools":["read"],"output_ref":"x","evidence_required":["x"],"approval_required":False})'
mutate authority_escalation 'd["delegations"][0]["authority_tools"].append("deploy")'
mutate undeclared_child_tool 'd["delegations"][1]["authority_tools"].remove("browser")'
mutate shared_write 'd["lanes"][2]["write"]=["artifacts/code"]'
mutate duplicate_lane_agent 'd["lanes"][2]["agent_id"]="code_worker"'
mutate unassigned_requirement 'd["agents"][0]["requirements"]=["req_code"]'
mutate overspend 'd["agents"][1]["budget"]["max_cost_usd"]=4.0'
mutate no_cancel 'd["failure_policy"]["cancel_descendants"]=False'
mutate sensitive_trace 'd["trace_policy"]["include_sensitive_data"]=True'
mutate missing_handoff_trace 'd["trace_policy"]["events"].remove("handoff")'
mutate self_review 'd["review"]["independent_reviewer"]=d["review"]["owner"]'
mutate illustrative_approval 'd["receipt_kind"]="illustrative_fixture"'
mutate no_independent_verify 'd["synthesis"]["independent_verification"]=False'
mutate legacy_schema 'd["schema_version"]=1'
mutate missing_model 'd["agents"][1].pop("model_selection")'
mutate unavailable_model 'd["agents"][1]["model_selection"]["model"]="unavailable"'
mutate unsupported_effort 'd["agents"][1]["model_selection"]["reasoning_effort"]="unsupported"'
mutate unresolved_inheritance 'd["agents"][1]["model_selection"]["model"]="inherit"'
mutate missing_vision 'd["agents"][2]["model_selection"]["available_capabilities"]=["tool_use"]'
mutate silent_fallback 'd["agents"][1]["model_selection"]["fallback"]="auto"'
mutate no_catalog_evidence 'd["agents"][1]["model_selection"]["evidence_ref"]=""'
mutate malformed_catalog 'd["agents"][1]["model_selection"]["available_models"]=[{}]'
mutate host_concurrency 'd["limits"]["host_concurrency_limit"]=2'
mutate fractional_concurrency 'd["limits"]["max_concurrent_agents"]=2.5'
mutate infinite_budget 'd["limits"]["max_cost_usd"]=float("inf")'
mutate negative_descendants 'd["agents"][1]["budget"]["max_descendants"]=-1'
mutate nested_write 'd["lanes"][2]["write"]=["artifacts/code/nested"]'
mutate parent_write 'd["lanes"][2]["write"]=["artifacts"]'
python3 - "$T/captured.json" "$V" <<'PY'
import importlib.util
import json
import sys

spec=importlib.util.spec_from_file_location('contract',sys.argv[2])
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
d=json.load(open(sys.argv[1]))
# A valid chain distinguishes total descendants from immediate children.
d['limits']['max_depth']=3
d['limits']['max_retries_per_task']=0
d['agents'][1]['tools'].append('browser')
d['agents'][1]['denied_tools'].remove('browser')
d['agents'][1]['budget']['max_descendants']=1
d['agents'][2]['parent_id']='code_worker'
d['delegations'][0]['authority_tools'].append('browser')
d['delegations'][1]['from']='code_worker'
assert module.validate(d)==([],[]), module.validate(d)
d['agents'][0]['budget']['max_descendants']=1
errors,gates=module.validate(d)
assert not errors and 'total descendants exceed budget at manager' in gates, (errors,gates)
PY
echo "orchestration contract fixtures passed"
