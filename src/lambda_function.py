import json


def lambda_handler(event, context):
    body = {
        "event": event,
    }

    return {
        'statusCode': 200,
        'body': json.dumps(body, indent=2)
    }
