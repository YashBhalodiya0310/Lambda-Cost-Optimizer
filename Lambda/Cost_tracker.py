import boto3
import datetime
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LambdaCostTable')

def lambda_handler(event, context):
    client = boto3.client('ce')
    end = datetime.datetime.utcnow().date()
    start = end - datetime.timedelta(days=7)

    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start.strftime('%Y-%m-%d'),
            'End': end.strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'FunctionName'}]
    )

    for group in response['ResultsByTime'][0]['Groups']:
        function_name = group['Keys'][0]
        cost = Decimal(group['Metrics']['UnblendedCost']['Amount'])
        
        table.put_item(Item={
            'FunctionName': function_name,
            'Cost': str(cost),
            'Timestamp': str(datetime.datetime.now())
        })

    return {
        'statusCode': 200,
        'body': 'Lambda cost data saved to DynamoDB'
    }
