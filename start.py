#lambda V6
import boto3

# Enter the region your instances are in, e.g. 'us-east-1'

region = 'ap-northeast-1'

# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']


instances = ['i-07b017eccb3632877','i-06d3118b433d93b7f','i-00de66f07b5d07233']
def lambda_handler(event, context):

	ec2 = boto3.client('ec2', region_name=region)

	ec2.start_instances(InstanceIds=instances)

	print 'started your instances: ' + str(instances)