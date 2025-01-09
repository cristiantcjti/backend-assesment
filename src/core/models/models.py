import uuid

from django.db import models


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Client(Base):
    reference = models.CharField(max_length=255)

class Consumer(Base):
    name = models.CharField(max_length=255)
    address = models.TextField()
    ssn = models.CharField(max_length=11, unique=True)

class AccountManager(models.Manager):
    def with_filter(self, payload):
        min_balance = payload.get("min_balance")
        max_balance = payload.get("max_balance")
        consumer_name = payload.get("consumer_name")
        status = payload.get("status")

        accounts = self.select_related("client", "consumer")

        if min_balance:
            accounts = accounts.filter(balance_gte=min_balance)

        if max_balance:
            accounts = accounts.filter(balance__lte=max_balance)

        if consumer_name:
            accounts = accounts.filter(consumer_name__icontains=consumer_name)

        if status:
            accounts = accounts.filter(status=status)

        return accounts.values(
            "id",
            "reference_no",
            "balance"
            "status",
            "created_at",
            "updated_at",
        )

class Account(Base):
    objects = AccountManager()
    reference_no = models.UUIDField(unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="accounts")
    consumers = models.ManyToManyField(Consumer, related_name="accounts")
