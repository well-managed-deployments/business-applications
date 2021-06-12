from pydantic import ValidationError

from wmd import models


def test_business_application_model():
    business_application = {
        "name": "Well Managed Deployments",
        "is_active": True,
        "created_at": "2020-02-01T15:31:24.349857",
        "maintenance_team": "DEVOPS_WMD",
    }

    try:
        models.BusinessApplication(**business_application)
    except ValidationError as e:
        print(str(e))
        assert False

    assert True
