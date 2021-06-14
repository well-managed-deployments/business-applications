import json
from decimal import Decimal

from mypy_boto3_dynamodb.service_resource import Table

from wmd.models import BusinessApplication


def _format_dynamodb(pydantic_model) -> dict:
    """Hacky pydantic formatting for dynamodb"""
    # DynamoDB only understands Decimal format for numbers, not float
    return json.loads(pydantic_model.json(), parse_float=Decimal)


def retrieve_business_application(
    dynamo_table: Table, configuration_item_id: str
) -> dict:
    return dynamo_table.get_item(Key=configuration_item_id)


def create_business_application(
    dynamo_table: Table, configuration_item: BusinessApplication
) -> None:
    item_data = _format_dynamodb(configuration_item)
    dynamo_table.put_item(Item=item_data)
