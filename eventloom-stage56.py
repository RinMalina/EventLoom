# === Stage 56: Add compact error classes for domain failures ===
# Project: EventLoom
class EventLoomError(Exception): pass
class ScheduleConflictError(EventLoomError): pass
class BudgetOverflowError(EventLoomError): pass
class AttendeeDuplicateError(EventLoomError): pass
class TaskMissingDetailsError(EventLoomError): pass
class ResourceUnavailableError(EventLoomError): pass
class InvalidDateRangeError(EventLoomError): pass
class CurrencyMismatchError(EventLoomError): pass
