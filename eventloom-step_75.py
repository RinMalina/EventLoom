# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: EventLoom
class ValidationReport:
    def __init__(self):
        self.warnings = []
        self.errors = []

    def check_schedule_conflicts(self, schedules):
        for i in range(len(schedules)):
            for j in range(i + 1, len(schedules)):
                if schedules[i].overlap(schedules[j]):
                    self.errors.append(
                        f"Schedule conflict: {schedules[i].name} and {schedules[j].name}"
                    )

    def check_attendee_budget(self, attendees, budget):
        total = sum(a.cost for a in attendees)
        if total > budget:
            diff = total - budget
            self.warnings.append(
                f"Total attendee cost ({total}) exceeds budget ({budget}) by {diff}"
            )

    def check_task_deadlines(self, tasks):
        for task in tasks:
            if task.deadline is not None and task.status == "pending":
                self.warnings.append(f"Task '{task.name}' has no progress toward deadline")

    def generate(self):
        report = f"=== EventLoom Validation Report ===\n\n"
        if self.errors:
            report += "ERRORS:\n" + "\n".join(f"- {e}" for e in self.errors) + "\n\n"
        if self.warnings:
            report += "WARNINGS:\n" + "\n".join(f"* {w}" for w in self.warnings) + "\n\n"
        if not self.errors and not self.warnings:
            report += "All checks passed.\n"
        return report.strip()
