import json
import boto3
import requests


def lambda_handler(event, context):
    ip = requests.get('http://checkip.amazonaws.com/')

    dynamodb = boto3.resource(
                    'dynamodb',
                    region_name='ap-northeast-a'
                )

    return {
        "statusCode": 200,
        "body": json.dumps({
            'message': 'hello world',
            'location': ip.text.replace('\n', ''),
        })
    }
