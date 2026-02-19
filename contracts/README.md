# Contracts – Data Agreement Layer

This folder defines the official data contracts between:

- Frontend (React – Interaction Capture)
- Backend (FastAPI – Validation & Storage)
- ML Layer (Feature Extraction & Inference)

After Sprint 1, all files inside this folder are considered FROZEN.

---

##  Contract Freeze Policy

- Contracts must NOT be modified without full team agreement.
- Any change requires:
  - Pull Request with label: `[CONTRACT CHANGE]`
  - At least 2 reviewers (Frontend + ML mandatory)
- Breaking changes must be discussed before implementation.

---

##  Interaction Payload

Defined in:

`sample_payload.json`
`interaction.schema.json`

This contract defines how frontend sends time-windowed interaction data.

Key rules:

- Time is relative (`t_rel_ms`)
- Events are grouped by window
- Mouse, key and scroll arrays must always exist (can be empty)

---

##  Feature Extraction Output

Defined in:

`feature_vector.schema.json`

Feature names are NOT arbitrary.

The final model input feature set is locked by:

`feature_order.json`

---

##  Database Mapping

Feature outputs are stored in the following columns:

- `mouse_features` → interaction_summaries.mouse_features
- `keystroke_features` → interaction_summaries.keystroke_features
- `scroll_features` → interaction_summaries.scroll_features
- `feature_vector` → interaction_summaries.feature_vector (optional but recommended)

---

##  Important

Contracts define structure, not values.

Values are dynamic.
Structure is fixed.
