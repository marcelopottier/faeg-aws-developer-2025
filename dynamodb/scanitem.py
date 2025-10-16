from dotenv import load_dotenv
import boto3
from boto3.dynamodb.conditions import Attr
load_dotenv()
dynamodb = boto3.resource('dynamodb')


table = dynamodb.Table('cliente')


response = table.scan(
    FilterExpression = Attr('nome').eq('marcelo')
)

print(response)