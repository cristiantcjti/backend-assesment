from datetime import datetime
from decimal import Decimal
from uuid import UUID

from ninja import Schema

from ..models.enums import AccountStatus


class AccountOutput(Schema):
    id: UUID
    reference_no : UUID
    balance : Decimal
    status : AccountStatus
    created_at: datetime
    updated_at: datetime

