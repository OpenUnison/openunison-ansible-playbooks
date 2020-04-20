#!/usr/local/aws/bin/python

import boto3
import sys


out_to = open(sys.argv[2],"w")

client = boto3.client('ssm',region_name='us-east-1')
response = client.get_parameters_by_path(Path=sys.argv[1],Recursive=True,WithDecryption=True)
done = False

while not done:
        for r in response['Parameters']:
                out_to.write(r['Name'][r['Name'].rfind('/')+1:] + '=' + r['Value'] + '\n')
        if 'NextToken' in response.keys():
                response = client.get_parameters_by_path(Path=sys.argv[1],Recursive=True,WithDecryption=True,NextToken=response['NextToken'])
        else:
                done = True

out_to.close()
