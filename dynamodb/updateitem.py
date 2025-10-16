from dotenv import load_dotenv
import boto3

load_dotenv()
dynamodb = boto3.resource('dynamodb')


table = dynamodb.Table('cliente')

response = table.update_item(
    Key={
        'id': 2,
    },
    UpdateExpression = "SET nome = :val1",
    ExpressionAttributeValues = {
        ":val1" : "marcelo"
    }
)

print("Item updated", response)