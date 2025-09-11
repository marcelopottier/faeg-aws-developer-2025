import boto3

#cliente é low level em python / resource é high level
s3api = boto3.client("s3", region_name="us-east-1")

bucket_name = "marcelopottier2000"

file_name = "./s3/index.html"
object_name = "index.html"

result = s3api.upload_file(file_name, bucket_name, object_name)

print("arquivo enviado", result)
