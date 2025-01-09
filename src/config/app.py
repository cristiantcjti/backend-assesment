import json
from typing import Type, Union

from django.http import HttpRequest, HttpResponse
from ninja import NinjaAPI
from ninja.errors import ValidationError as NinjaValidationError
from pydantic.error_wrappers import ValidationError as PydanticValidationError

from src.core.controllers.account import account_router


Exc = Union[Exception, Type[Exception]]


class AssessmentNinjaAPI(NinjaAPI):
    def on_exception(self, request: HttpRequest, exc: Exc) -> HttpResponse:
        errors = []
        status = 400
        if isinstance(exc, PydanticValidationError):
            errors = [{"field": error.get("loc")[-1], "message": error.get("msg")} for error in exc.errors()]
        elif isinstance(exc, NinjaValidationError):
            errors = [{"field": error.get("loc")[-1], "message": error.get("msg")} for error in exc.errors]
        else:
            errors = [{"message": str(exc)}]
        return api_v1.create_response(
            request,
            {"errors": errors},
            status=status,
        )


api_v1 = AssessmentNinjaAPI(
    version="1.0.0",
    description="Assessment Project.",
    title="Assessment Project",
)


api_v1.add_router("", account_router)

