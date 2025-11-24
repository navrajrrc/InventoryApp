import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['item_id']
        location_id = int(event['queryStringParameters']['location_id'])

        response = table.delete_item(
            Key={
                'item_id': item_id,
                'location_id': location_id
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Item {item_id} deleted'})
        }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
