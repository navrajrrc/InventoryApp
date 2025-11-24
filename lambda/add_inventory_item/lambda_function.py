import json
import boto3
import ulid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])

        item_id = str(ulid.new())

        item = {
            "item_id": item_id,
            "location_id": int(data['location_id']),
            "item_name": data['item_name'],
            "item_description": data['item_description'],
            "item_qty": int(data['item_qty']),
            "item_price": Decimal(str(data['item_price']))
        }

        table.put_item(Item=item)

        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Item added', 'item_id': item_id})
        }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
