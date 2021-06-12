from datetime import datetime

from pydantic import BaseModel, validator


class BusinessApplication(BaseModel):
    name: str
    is_active: bool
    created_at: datetime
    maintenance_team: str

    @validator("created_at", pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.utcnow()
