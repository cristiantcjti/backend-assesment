from django.db import models


class AccountStatus(models.TextChoices):
    IN_COLLECTION = "IN_COLLECTION"
    PAID_IN_FULL = "PAID_IN_FULL"
