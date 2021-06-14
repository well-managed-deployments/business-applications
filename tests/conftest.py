import os

import boto3
import pytest
from moto import mock_dynamodb2
from mypy_boto3_dynamodb.literals import BillingModeType
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource, Table


@pytest.fixture(scope="module")
def pagination_size() -> int:
    yield 30


@pytest.fixture(scope="module")
def aws_credentials() -> None:
    """Fake AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture(scope="module")
def active_region() -> str:
    yield "us-east-1"


@pytest.fixture(scope="module")
def dynamodb(aws_credentials, active_region) -> DynamoDBServiceResource:
    """Build mock dynamodb2 resource for testing"""
    with mock_dynamodb2():
        yield boto3.resource("dynamodb", region_name=active_region)


@pytest.fixture(scope="module")
def dynamo_table_business_applications(dynamodb) -> Table:
    """Setup dynamodb for moto testing"""
    table_name = os.getenv("APPLICATION_TABLE", "business-applications")

    yield dynamodb.create_table(
        AttributeDefinitions=[
            {"AttributeName": "name", "AttributeType": "S"},
        ],
        BillingMode="PAY_PER_REQUEST",
        TableName=table_name,
        KeySchema=[{"AttributeName": "name", "KeyType": "HASH"}],
    )
