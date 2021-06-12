from pydantic import ValidationError

from wmd import models

business_application = {
    "name": "Well Managed Deployments",
    "is_active": True,
    "created_at": "2020-02-01T15:31:24.349857",
    "maintenance_team": "DEVOPS_WMD",
}


def test_business_application_model():
    try:
        models.BusinessApplication(**business_application)
    except ValidationError as e:
        print(str(e))
        assert False

    assert True


def test_business_applications_collection_model():
    try:
        models.BusinessApplicationsCollection(
            business_applications=[models.BusinessApplication(**business_application)]
        )
    except ValidationError as e:
        print(str(e))
        assert False

    assert True
