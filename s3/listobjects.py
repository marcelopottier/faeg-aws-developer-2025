import boto3

bucket_name = "marcelopottier2000"

s3 = boto3.resource('s3')

bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.all():
    print(f"{obj.key}")