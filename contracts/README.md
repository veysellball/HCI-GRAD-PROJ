# Contracts – Data Agreement Layer

This folder defines the official data contracts between:
- Frontend (React – Interaction Capture)
- Backend (Validation & Storage)
- ML Layer (Feature Extraction & Inference)

---

## Contract Freeze Policy

Interaction contract is frozen after Sprint 1.

Feature extraction output contract is frozen when feature_set_version is finalized (typically Sprint 2/3).

Any change requires:

Pull Request with label: [CONTRACT CHANGE]

At least 2 reviewers (Frontend + ML mandatory)

Breaking changes must be discussed before implementation.

Contract version (schema_version) must be incremented for breaking structural changes.

---

## Interaction Payload (FROZEN after Sprint 1)

Defined in:

sample_payload.json

interaction.schema.json

Key rules:

Time is relative to task start (t_rel_ms).

t_rel_ms does not reset per window.

All time values are integers in milliseconds.

Events are grouped by fixed-size time windows.

mouse, key, scroll arrays must always exist (can be empty, never null).

Event arrays must be sorted by t_rel_ms in ascending order.

Window boundary semantics: [start, end) (end exclusive).

Window rule:

window_start_rel_ms <= t_rel_ms < window_end_rel_ms

Window index rule:

window_idx = floor(t_rel_ms / WINDOW_MS)

An event at exactly the window boundary belongs to the next window.
Event duplication across windows is not allowed.

v1.0 scope:

Mouse: move, click

Key: action = "down" only

Scroll: deltaY

Client metadata:

client object is optional.

If present, viewport is required.

Client metadata is not mandatory for model correctness.

---

## Feature Extraction Output (FROZEN when feature set is finalized)

Defined in:

feature_vector.schema.json

Feature output must correspond to exactly one interaction window and include:

schema_version

session_id

task_id

window_idx

Notes:

Feature keys are controlled by meta.feature_set_version.

meta.extractor_version identifies the extraction logic version.

Feature names must remain stable within the same feature_set_version.

If the feature set changes, feature_set_version must change.

If a fixed order is required for model input, it is defined in:

feature_order.json (introduced when finalized).

---

Important

Contracts define structure and semantics, not values.
Values are dynamic. Structure is fixed.
No implementation details belong in this layer.