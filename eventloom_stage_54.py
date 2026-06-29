# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: EventLoom
import sys, colorama
colorama.init()

def colored(text: str, fg=None, bg=None):
    codes = []
    if fg: codes.append(f"\033[{fg}m")
    if bg: codes.append(f"\033[10{bg}m")
    return "".join(codes) + text + "\033[0m"

def print_header(title):
    print(colored("=" * 40, fg=7))
    print(colored(f" {title}", fg=6, bg=25))
    print(colored("=" * 40, fg=7))

def print_section(label):
    print(colored("\n---", fg=10), colored(label, fg=3), colored("---", fg=10))

def print_success(msg):
    print(colored(f"[OK] {msg}", fg=2))

def print_error(msg):
    print(colored(f"[ERR] {msg}", fg=9))

def print_warning(msg):
    print(colored(f"[WARN] {msg}", fg=3, bg=104))
