from dotenv import load_dotenv
import boto3

load_dotenv()
dynamodb = boto3.resource('dynamodb')


table = dynamodb.Table('cliente')


response = table.get_item(
    Key={
        'id': 2
    }
)

item = response['Item']
print(response)