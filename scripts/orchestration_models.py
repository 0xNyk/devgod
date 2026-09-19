"""Validate declared model choices and runtime identity without contacting providers."""

from __future__ import annotations

from typing import Any


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def strings(value: Any) -> bool:
    return (isinstance(value, list) and bool(value)
            and all(nonempty(item) for item in value)
            and len(value) == len(set(value)))


def validate_selection(selection: Any) -> list[str]:
    keys = {"host", "model", "reasoning_effort", "available_models", "supported_efforts",
            "required_capabilities", "available_capabilities", "selection_basis",
            "rationale", "evidence_ref", "fallback"}
    if not isinstance(selection, dict) or set(selection) != keys:
        return ["model_selection keys invalid"]
    issues = []
    for key in ("host", "model", "reasoning_effort", "rationale", "evidence_ref",
                "selection_basis", "fallback"):
        if not nonempty(selection[key]):
            issues.append(f"model_selection {key} required")
    for key in ("available_models", "supported_efforts", "required_capabilities",
                "available_capabilities"):
        if not strings(selection[key]):
            issues.append(f"model_selection {key} must contain unique nonempty strings")
    if issues:
        return issues
    if selection["model"] in {"auto", "inherit", "default", "unknown"}:
        issues.append("resolve the effective model before execution")
    if selection["model"] not in selection["available_models"]:
        issues.append("selected model is not in the observed host catalog")
    if selection["reasoning_effort"] not in selection["supported_efforts"]:
        issues.append("selected reasoning effort is not supported by this model and host")
    if not set(selection["required_capabilities"]).issubset(selection["available_capabilities"]):
        issues.append("selected model and host lack required capabilities")
    if selection["selection_basis"] not in {"user_override", "project_policy", "task_fit", "inherit"}:
        issues.append("model selection basis invalid")
    if selection["fallback"] != "stop_and_replan":
        issues.append("model fallback must stop and replan; silent substitution is forbidden")
    return issues


def validate_observed(observed: Any, selection: Any) -> list[str]:
    keys = {"host", "model", "reasoning_effort", "evidence_ref"}
    if not isinstance(observed, dict) or set(observed) != keys:
        return ["observed execution identity required"]
    if any(not nonempty(observed[key]) for key in keys):
        return ["observed execution identity must be complete"]
    if not isinstance(selection, dict):
        return ["contracted model selection missing"]
    return [f"observed {key} differs from the contracted model selection"
            for key in ("host", "model", "reasoning_effort")
            if observed[key] != selection.get(key)]
