# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: EventLoom
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}
    
    def dispatch(self, text):
        normalized = text.strip().lower()
        if not normalized or normalized.startswith('#'): return None
        parts = normalized.split(maxsplit=1)
        command = parts[0]
        args = parts[1] if len(parts) > 1 else ''
        handler = self.handlers.get(command)
        if handler:
            try:
                result = handler(args)
                return f"OK: {result}" if result is not None else "OK"
            except Exception as e:
                return f"ERROR: {str(e)}"
        return f"Unknown command: {command}"

    def register(self, cmd, func):
        self.handlers[cmd.lower()] = func
