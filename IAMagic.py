import argparse
import boto3, botocore

def check_creds():
    try:
        sts.get_caller_identity()
        return True
    except botocore.exceptions.ClientError:
        return False

def cred_enum():
    name = sts.get_caller_identity().get('Arn')
    n = name.split(":")[-1]
    if "/" in n:
        print("User Name: " + '\33[94m' + n.split("/")[-1] + '\33[0m')
        print("User Type: IAM")
    else:
        if n == "root":
            print("User Name: " + '\33[94m' + n + '\33[0m')
            print("User Type: " + '\x1b[1;33;41m' + 'Root/Owner' + '\x1b[0m')
        else:
            print("User Name: " + '\33[94m' + n + '\33[0m')

def list_buckets():
    print("\nListing buckets...")
    count = 0;
    try:
        for bucket in s3.buckets.all():
            print('\33[94m' + bucket.name + '\33[0m')
            count+=1
        if count == 0:
            print('\33[91m'+"No buckets found"+'\33[0m')
        else:
            print("Looks like there are some buckets here :D be sure to check out https://github.com/Pyr0sec/S3scan to scan these buckets.")
    except botocore.exceptions.ClientError:
        print('\33[91m'+"Access Denied :("+'\33[0m')

def available_regions(service):
    regions = []
    if args.profile:
        session = boto3.Session(profile_name=args.profile)
        ec2 = session.client(service, region_name='us-west-1')
    else:
        ec2 = boto3.client(service, aws_access_key_id=args.access_key_id, aws_secret_access_key=args.secret_access_key)
    response = ec2.describe_regions()

    for item in response["Regions"]:
        regions.append(item["RegionName"])

    return regions

def list_ec2():
    print("\nListing running EC2 instances...")
    try:
        regions = available_regions("ec2")
        cnt = 0
        for region in regions:
            if args.profile:
                session = boto3.Session(profile_name=args.profile)
                ec2 = session.client('ec2', region_name=region)
            else:
                ec2 = boto3.client('ec2', aws_access_key_id=args.access_key_id, aws_secret_access_key=args.secret_access_key, region_name=region)
            response = ec2.describe_instances()
            for r in response["Reservations"]:
                status = r["Instances"][0]["State"]["Name"]
                if status == "running":
                    instance_id = r["Instances"][0]["InstanceId"]
                    instance_type = r["Instances"][0]["InstanceType"]
                    az = r["Instances"][0]["Placement"]["AvailabilityZone"]
                    print('\33[94m' + f"id: {instance_id}, type: {instance_type}, az: {az}" + '\33[0m')
                    cnt += 1
        if cnt == 0:
                print('\33[91m'+"No running instances found"+'\33[0m')
    except botocore.exceptions.ClientError:
         print('\33[91m'+"Access Denied :("+'\33[0m')

def list_policy():
    print("\nPolicies attached to the credentials:")
    try:
        name = sts.get_caller_identity().get('Arn')
        n = name.split(":")[-1]
        if "/" in n:
            n = n.split("/")[-1]
        response = iam.list_attached_user_policies(UserName=n)
        count1 = 0;
        for policy in response['AttachedPolicies']:
            print('\33[94m' + policy['PolicyName'] + '\33[0m')
            count1+=1;
        if count1 == 0:
            print("No policies attached to the credentials")
    except botocore.exceptions.ClientError:
         print('\33[91m'+"Access Denied :("+'\33[0m')

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument('-id', '--access-key-id', help="Accepts AWS access key ID as an argument", type=str)
parser.add_argument('-key', '--secret-access-key', help="Accepts AWS Secret access key as an argument", type=str)
group.add_argument('--profile', help="Used to specify an AWS profile on your system (like awscli), Uses default credentials if not specified any.", type=str)
parser.add_argument('--enumerate', help="Further enumerates the credentials by Checking ", action='store_true', default=False)

args = parser.parse_args()

if args.access_key_id and not args.secret_access_key:
    parser.error('the following arguments are required: -key OR --secret-access-key')
elif args.secret_access_key and not args.access_key_id:
    parser.error('the following arguments are required: -id OR --access-key-id')

try:
    if args.profile:
        session = boto3.Session(profile_name=args.profile)
        sts = session.client('sts')
        iam = session.client('iam')
        s3 = session.resource('s3')
    else:
        sts = boto3.client('sts', aws_access_key_id=args.access_key_id, aws_secret_access_key=args.secret_access_key)
        iam = boto3.client('iam', aws_access_key_id=args.access_key_id, aws_secret_access_key=args.secret_access_key)
        s3 = boto3.resource('s3', aws_access_key_id=args.access_key_id, aws_secret_access_key=args.secret_access_key)
except botocore.exceptions.ProfileNotFound:
    print('\33[91m'+"Error: ProfileNotFound"+'\33[0m')
    exit()

if check_creds():
    print('\x1b[6;30;42m' + '\nCredentials are valid!' + '\x1b[0m')
else:
    print('\x1b[1;33;41m' + '\nInvalid Credentials' + '\x1b[0m')
    exit()

if check_creds() and args.enumerate:
    print("\nEnumerating...")
    cred_enum()
    list_buckets()
    list_ec2()
    list_policy()
else:
    print("\nTry '--enumerate' to get more information.")