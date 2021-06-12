from http import HTTPStatus

from .models import (
    BusinessApplication,
    BusinessApplicationsCollection,
    ControllerResponse,
)


def index_business_applications():
    empty_response = BusinessApplicationsCollection()

    return ControllerResponse(
        status_code=HTTPStatus.NOT_IMPLEMENTED, payload=empty_response
    )
