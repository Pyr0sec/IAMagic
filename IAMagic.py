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
        print("User Name: " + n.split("/")[-1])
        print("User Type: IAM")
    else:
        if n == "root":
            print("User Name: " + n)
            print("User Type: " + '\x1b[1;33;41m' + 'Root/Owner' + '\x1b[0m')
        else:
            print("User Name: " + n)


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

if args.profile:
    session = boto3.Session(profile_name=args.profile)
    sts = session.client('sts')
else:
    sts = boto3.client('sts', aws_access_key_id=args.access_key_id, aws_secret_access_key=args.secret_access_key)

if check_creds():
    print('\x1b[6;30;42m' + '\nCredentials are valid!' + '\x1b[0m' + "\n\nTry '--enumerate' to get more information.")
else:
    print('\x1b[1;33;41m' + '\nInvalid Credentials' + '\x1b[0m')
    exit()

if check_creds() and args.enumerate:
    print("\nEnumerating...")
    cred_enum()