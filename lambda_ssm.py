from __future__ import print_function

import boto3
import time
import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = event['Records'][0]['Sns']['Message']
    #print("From SNS: " + message)
    instanceId = 'i-0d40bf0f0d09b981c'
    if (message=='start') :
        ssmClient = boto3.client('ssm')
        ssmCommand = ssmClient.send_command(
        InstanceIds = [
           instanceId
        ],
        DocumentName = 'AWS-RunShellScript',
        TimeoutSeconds = 240,
        Comment = 'Run nginx',
        Parameters = {
           'commands': [
              "sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT"
          ]
        }
    )
    else :
        ssmClient = boto3.client('ssm')
        ssmCommand = ssmClient.send_command(
        InstanceIds = [
           instanceId
        ],
        DocumentName = 'AWS-RunShellScript',
        TimeoutSeconds = 240,
        Comment = 'Donot Run Tests',
        Parameters = {
           'commands': [
             "sudo iptables -I INPUT -p tcp --dport 80 -j DROP"
          ]
        }
    )
    print("From SNS new: " + message)
