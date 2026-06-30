# === Stage 55: Add a setting to disable colorized output ===
# Project: EventLoom
class ColorMode:
    def __init__(self, enabled=True):
        self.enabled = enabled

    def is_colorized(self) -> bool:
        return self.enabled and os.name != 'nt'

def get_terminal_colors() -> tuple[int, int]:
    if not ColorMode().is_colorized():
        return (0, 0)
    try:
        from colorama import Fore, Style
        return (Fore.RED.value, Fore.GREEN.value)
    except ImportError:
        return (0, 0)

def print_colored(text: str, fg: int = None, bg: int = None):
    if not ColorMode().is_colorized():
        print(text)
        return
    try:
        from colorama import Fore, Style
        prefix = ""
        suffix = "\n"
        if fg is not None:
            prefix += Fore.colors.get(fg, "")
        if bg is not None:
            prefix += Style.BRIGHT + Fore.bg_colors.get(bg, "")
        print(prefix + text + Style.RESET_ALL)
    except Exception:
        print(text)

def setup_color_mode():
    import os
    from colorama import init
    try:
        if ColorMode().is_colorized() and 'TERM' in os.environ or not os.name == 'nt':
            init(autoreset=True)
    except ImportError:
        pass
