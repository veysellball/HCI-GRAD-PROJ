## Window boundary semantics (v1.0)
- All times are relative to task start (t0).
- window_start_rel_ms is **inclusive**
- window_end_rel_ms is **exclusive**

For any event:
window_start_rel_ms <= t_rel_ms < window_end_rel_ms

Window index rule (WINDOW_MS = 5000 in Sprint 2):
window_idx = floor(t_rel_ms / WINDOW_MS)

Reason:
- Prevents duplication at boundaries (an event at exactly 5000ms belongs to window_idx=1, not 0)