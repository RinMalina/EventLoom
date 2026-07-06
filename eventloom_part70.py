# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: EventLoom
CLEAR = "clear"

def clear_state():
    """Reset all internal state and return a confirmation flag."""
    global _state, _confirm
    if _state is None:
        raise RuntimeError("No state to clear")
    if not _confirm:
        return False
    _state.reset()
    _confirm = False
    return True
