import boto3

response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'world'
    },
    {
        'Id': '2',
        'MessageBody': 'boto3',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Scott',
                'DataType': 'String'
            }
        }
    }
])

# Print out any failures
print(response.get('Failed'))