import csv
import json
import boto3
import pandas as pd
import os
import glob

def lambda_handler(event, context):

    #Creates boto3 s3 session that is connected to localstack
    s3 = boto3.resource('s3', aws_access_key_id="123", aws_secret_access_key="124", endpoint_url="http://s3.localhost.localstack.cloud:4566")
    sess = boto3.client("s3", endpoint_url="http://s3.localhost.localstack.cloud:4566", region_name='us-east-1')

    bucket_name = 'bucketerie'

    #creates bucket
    sess.create_bucket(Bucket=bucket_name)

    #Reads from CSV files
    files = os.path.join("example*.csv")
    files = glob.glob(files)
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    json_name = 'colors_united.json'
    df.to_json(json_name)

    #Creates json file and puts it in the bucket
    with open (json_name, "w") as f:
        s3object = s3.Object(bucket_name, json_name)

        s3object.put(Body=(bytes(json.dumps(json_name).encode("UTF-8"))))

