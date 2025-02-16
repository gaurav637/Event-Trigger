from django.db import models


class EventTrigger(models.Models):
    SCHEDULED = "scheduled"
    API = "api"

    TRIGGER_TYPES = [(SCHEDULED, "scheduled"), (API, "api")]
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="event_triggers"
    )
    name = models.CharField(max_length=200)
    trigger_type = models.CharField(max_length=50, choices=TRIGGER_TYPES)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
