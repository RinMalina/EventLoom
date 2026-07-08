# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: EventLoom
import signal


def _cleanup():
    # Gracefully close any open resources before exiting
    for handler in ["schedule", "attendees", "budgets", "tasks"]:
        resource = getattr(_app, handler, None)
        if resource is not None and hasattr(resource, "close"):
            try:
                resource.close()
            except Exception:
                pass


def _signal_handler(signum, frame):
    """Handle SIGINT (Ctrl+C) gracefully."""
    print("\nInterrupted. Cleaning up...")
    _cleanup()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
