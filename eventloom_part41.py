# === Stage 41: Add plain text import for a simple line-based format ===
# Project: EventLoom
def load_plain_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def save_plain_text(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(item + '\n')

if __name__ == '__main__':
    print("Plain text I/O utilities loaded.")
