

import urllib.parse

print('Loading function')
import pandas as pd
import numpy as np
import boto3
import json
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """capturing the inference file to read from s3 events
      After batch transform Job successiful executed
    """
    inference_file = event['Records'][0]['s3']['object']['key']
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    data =pd.read_csv(f's3://{bucket_name}/{inference_file}', sep=',')
    for key in data:
        if key[0] > 10:
            boto3.client('sns').publish(
                TargetArn=os.environ['ARN'],
                Message= f"User {user} and ip{ip} is trying to access ",
                MessageStructure='string'
            )
            boto3.client('waf').publish(
                """
                Will get the best way to put this
                """
            )

        
           
    