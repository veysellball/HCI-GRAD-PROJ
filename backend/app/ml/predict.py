from __future__ import annotations

from typing import Any, Dict


def predict_from_feature_vector(feature_vector: Dict[str, Any]) -> Dict[str, str]:
    """
    Contract:
      Input  : feature_vector (dict of feature_name -> number)
      Output : labels dict:
        - attention_level
        - mental_workload
        - stress_indicator

    Notes:
      - Real model loading will be added in Sprint 3
      - Keep the output keys stable for backend + dashboard
    """
    return {
        "attention_level": "unknown",
        "mental_workload": "unknown",
        "stress_indicator": "unknown"
    }


def predict_from_raw_payload(raw_payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convenience entrypoint:
      raw_payload -> extract_features -> predict -> return both features and labels
    """
    from .feature_extractor import extract_features_from_raw

    features_out = extract_features_from_raw(raw_payload)
    labels = predict_from_feature_vector(features_out["feature_vector"])

    return {
        "features": features_out,
        "labels": labels
    }