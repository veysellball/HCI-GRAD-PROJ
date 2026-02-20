# Database Schema Design (High-Level)

This document defines the target DB schema (proposal-aligned).
Implementation (migrations/models) is owned by Backend (Emir).

## sessions
- id (UUID, PK)
- started_at (timestamp)
- ended_at (timestamp, nullable)

## tasks
- id (UUID, PK)
- session_id (UUID, FK -> sessions.id)
- task_type (text)  # optional
- started_at (timestamp)
- ended_at (timestamp, nullable)

## interaction_summaries
Represents one time-window (e.g., 5 seconds) of interaction data.

- id (UUID, PK)
- task_id (UUID, FK -> tasks.id)
- window_idx (int)
- window_start_rel_ms (int)
- window_end_rel_ms (int)

Raw payload (for reprocessing / audit):
- raw_payload (JSONB)

Feature summaries (proposal-aligned):
- mouse_features (JSONB, nullable)
- keystroke_features (JSONB, nullable)
- scroll_features (JSONB, nullable)

Optional combined model input:
- feature_vector (JSONB, nullable)

## inference_results
Stores predicted labels per interaction_summary.

- id (UUID, PK)
- interaction_summary_id (UUID, FK -> interaction_summaries.id)
- attention_level (text)
- mental_workload (text)
- stress_indicator (text)
- created_at (timestamp)