from decimal import Decimal
from typing import List

from ninja import Query, Router
from ninja.pagination import paginate

from src.config.pagination import CustomPagination
from src.core.models.enums import AccountStatus
from src.core.schemas.account import AccountOutput


from ..models.models import Account

account_router = Router(tags=["Accounts"])


@account_router.get("/accounts", response={200: List[AccountOutput]})
@paginate(CustomPagination)
def list_accounts(
    request,
    min_balance: Decimal = Query(default=None),
    max_balance: Decimal = Query(default=None),
    consumer_name: str = Query(default=None),
    status: List[AccountStatus] = Query(default=None)
):
    payload = {
        "min_balance": min_balance,
        "max_balance": max_balance,
        "consumer_name": consumer_name,
        "status": status,
    }
    return Account.objects.with_filter(payload=payload)

