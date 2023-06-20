import boto3
import sys

region=sys.argv[1]
accesskey=sys.argv[2]
secretkey=sys.argv[3]

# for_vpc = boto3.client('ec2',region_name="ap-south-1",aws_access_key_id="AKIA5B6S4DPLE2B2YG73",aws_secret_access_key="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")
for_vpc = boto3.client('ec2',region_name=region,aws_access_key_id=accesskey,aws_secret_access_key=secretkey)

vpc_create = for_vpc.create_vpc(
    CidrBlock='10.11.0.0/16'
    )

# print (vpc_create)
vpc_id = vpc_create["Vpc"]["VpcId"]
# print (vpc_id)

subnet_create = for_vpc.create_subnet(AvailabilityZone='ap-south-1a',
										VpcId=vpc_id,
										CidrBlock='10.11.1.0/24'
										)

# print (subnet_create["Subnet"]["SubnetId"])

ig_create = for_vpc.create_internet_gateway()
ig_id = ig_create['InternetGateway']['InternetGatewayId']

# print(ig_create['InternetGateway']['InternetGatewayId'])

attach_ig = for_vpc.attach_internet_gateway(
    InternetGatewayId=ig_id,
    VpcId=vpc_id
)

print (attach_ig)


