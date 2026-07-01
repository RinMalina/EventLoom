# === Stage 57: Add structured result objects for command handlers ===
# Project: EventLoom
class EventResult(BaseModel):
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None
    error_code: Optional[int] = None

def format_command_result(success: bool, msg: str, payload=None, code=200) -> Dict[str, Any]:
    return EventResult(success=success, message=msg, data=payload, error_code=code if not success else None).model_dump()
