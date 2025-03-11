import logging
import boto3

#write a function to take a prompt and call the converse function in bedrock
def converse(prompt):
    #create a boto3 client for bedrock
    client = boto3.client(service_name='bedrock-runtime')
    #create a logger
    logger = logging.getLogger(__name__)
    #create a response
    response = client.invoke_model(
        modelId='anthropic.claude-3-5-sonnet-20241022-v2:0',
        body=prompt
    )
    #return the response
    return response


converse("Hello, how are you?")