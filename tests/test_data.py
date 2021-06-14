from mypy_boto3_dynamodb.service_resource import Table

from wmd.data import create_business_application
from wmd.models import BusinessApplication


def test_it_creates_a_business_application(dynamo_table_business_applications: Table):
    new_app = BusinessApplication(
        name="BusinessAppWMD",
        is_active=True,
        maintenance_team="well-managed-deployments",
    )
    print(new_app.json())

    create_business_application(dynamo_table_business_applications, new_app)

    item_data = dynamo_table_business_applications.get_item(Key={"name": new_app.name})[
        "Item"
    ]
    print(item_data)

    assert new_app.name == item_data.get("name")
    assert new_app.is_active == item_data.get("is_active")


# TODO finalize test for fetch functionality
# def test_it_can_fetch_a_business_application():
#     business_application = data.retrieve_business_application()

#     assert business_application is not None
