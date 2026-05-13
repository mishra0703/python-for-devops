import boto3
from datetime import datetime , timezone , timedelta , date


def calculate_bill():
    ce_client = boto3.client('ce', region_name='us-east-1')

    today = date.today()
    start_date = today.replace(day=1).strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')

    response = ce_client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date,
            'End': end_date
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],          
    )

    bill = {}

    for result in response['ResultsByTime']:
        total_cost = result['Total']['UnblendedCost']['Amount']
        bill.update({f"Total AWS Cost of the month until {end_date}" :  f" ${total_cost} "})

    return bill




def iam_users_list():

    iam = boto3.client('iam')

    response = iam.list_users()
    iam_users = {}
    index=1

    for user in response['Users']:
        iam_users.update({f"User_{index}" : user['UserName']})
        index = index+1

    print(iam_users)
    return iam_users  



def ec2_Instances():
    ec2 = boto3.resource('ec2' , region_name='us-east-1')

    instance_list = {}
    index=1

    for instance in ec2.instances.all():
        instance_name = "No Name"
        if instance.tags:
            for tag in instance.tags:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
                    break
        
        instance_list[f'instance_{index}'] = {"Name" : instance_name ,  "Id" : instance.id , "State" : instance.state['Name']}
        index+=1

    return {
        "instances" : instance_list
    }        



def s3_Buckets():
    s3 = boto3.resource("s3")

    buckets_list = {}
    index = 1

    for bucket in s3.buckets.all():
        buckets_list[f'bucket_{index}'] = {"Name" : bucket.name}
        index+=1

    return {
        "buckets" : buckets_list
    }        




def s3_Buckets_Manage():
    
    s3 = boto3.client("s3")

    all_buckets = s3.list_buckets()["Buckets"]
    new_buckets_list = []
    old_buckets_list = []    
    curr_time = datetime.now(timezone.utc).astimezone()

    for bucket in all_buckets:
        bucket_name = bucket["Name"]        
        creation_date = bucket["CreationDate"]
        days_ago_90 = curr_time - timedelta(days=15)
        if creation_date < days_ago_90:
            old_buckets_list.append(bucket_name)
        else:
            new_buckets_list.append(bucket_name)

    return {
        "Total_buckets": len(all_buckets),
        "Total_New_Buckets" : len(new_buckets_list), 
        "New_buckets" : new_buckets_list,
        "Total_Old_Buckets" : len(old_buckets_list) ,
        "Old_buckets" : old_buckets_list
    }