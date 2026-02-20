from __future__ import annotations

from typing import Any, Dict


def extract_features_from_raw(raw_payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Contract:
      Input  : raw_payload (the JSON stored in interaction_summaries.raw_payload)
      Output : dict matching contracts/feature_vector.schema.json

    Notes:
      - Only uses relative times (t_rel_ms)
      - Returns modality-level features + combined feature_vector
      - Values must be numbers; keys must be stable (later locked by feature_order.json)
    """

    # Placeholders: will be implemented in Sprint 2/3
    mouse_features: Dict[str, float] = {}
    keystroke_features: Dict[str, float] = {}
    scroll_features: Dict[str, float] = {}

    # Combined model input features (merged)
    feature_vector: Dict[str, float] = {}

    return {
        "mouse_features": mouse_features,
        "keystroke_features": keystroke_features,
        "scroll_features": scroll_features,
        "feature_vector": feature_vector,
        "meta": {
            "extractor_version": "0.1.0",
            "feature_set_version": "0.1.0"
        }
    }