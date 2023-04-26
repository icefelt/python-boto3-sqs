import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

queue.send_message(MessageBody='boto3', MessageAttributes={
    'Author': {
        'StringValue': 'Scott',
        'DataType': 'String'
    }
})