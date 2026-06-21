# === Stage 32: Add pagination helpers for long console output ===
# Project: EventLoom
def paginate_output(lines, page_size=15):
    """Yields chunks of text for console pagination."""
    total_pages = (len(lines) + page_size - 1) // page_size if lines else 0
    current_page = 0
    while True:
        yield f"[Page {current_page}/{total_pages}]\n"
        chunk = lines[current_page * page_size : (current_page + 1) * page_size]
        for line in chunk:
            print(line, end='')
        if current_page >= total_pages - 1:
            break
        current_page += 1

def main():
    # Simulate long output
    lines = [f"Event {i}: Scheduled for {date}" for i in range(50) for date in ["Mon", "Tue"]]
    
    try:
        print("=== EventLoom Schedule Report ===")
        for chunk in paginate_output(lines):
            if not chunk.startswith("[Page"):  # Skip header lines from generator when printing directly
                pass 
            else:
                print(chunk, end='')
        
        print("\n[End of Output]")
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")

if __name__ == "__main__":
    main()
