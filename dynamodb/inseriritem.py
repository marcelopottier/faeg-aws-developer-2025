from dotenv import load_dotenv
import boto3

load_dotenv()
dynamodb = boto3.resource('dynamodb')


table = dynamodb.Table('cliente')

response = table.put_item(
    Item={
        'id': 2,
        'nome': 'luizinho',
        #'email': '',
        #'telefone': '232323-22323'
    }
)

print("Item inserted", response)