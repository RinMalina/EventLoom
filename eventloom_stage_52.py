# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: EventLoom
def format_currency(amount: float, currency: str = "USD") -> str:
    """Format a monetary amount with locale-aware symbols."""
    return f"{currency} {amount:.2f}"


def calculate_total_budget(items: list[dict[str, any]]) -> float:
    """Sum up costs from a list of budget items and round to cents."""
    total = sum(item.get("cost", 0) for item in items if isinstance(item, dict))
    return round(total, 2)


def validate_date_range(start: str, end: str) -> bool:
    """Check if start date is strictly before or equal to end date using string comparison."""
    try:
        s = datetime.strptime(start, "%Y-%m-%d")
        e = datetime.strptime(end, "%Y-%m-%d")
        return s <= e
    except ValueError:
        return False


def generate_task_id(task_name: str) -> str:
    """Create a unique task identifier by hashing the name and truncating."""
    import hashlib
    hash_obj = hashlib.md5(task_name.encode())
    return f"T-{hash_obj.hexdigest()[:8].upper()}"
