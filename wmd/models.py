from datetime import datetime
from http import HTTPStatus
from typing import List, Optional

from pydantic import BaseModel, Field


class Model(BaseModel):
    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }


class BusinessApplication(Model):
    name: str
    is_active: bool
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="UTC timestamp for when the business application was built",
    )
    maintenance_team: str = Field(
        description="Named identifier of the team responsible for this element"
    )


class BusinessApplicationsCollection(Model):
    business_applications: List[BusinessApplication] = []


class ControllerResponse(Model):
    headers: Optional[dict]
    payload: Optional[dict]
    status_code: HTTPStatus
