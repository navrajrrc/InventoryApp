import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    try:
        location_id = int(event['pathParameters']['location_id'])

        response = table.query(
            IndexName='LocationItemGSI', 
            KeyConditionExpression=boto3.dynamodb.conditions.Key('location_id').eq(location_id)
        )

        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
