import boto3
import json
import pdb


def print_instances():
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

    return instance_list        





def Buckets_list():
    s3 = boto3.resource("s3")

    buckets = {}
    index = 1
    # print("\n---------- Buckets ----------\n")

    for bucket in s3.buckets.all():
        buckets[f'bucket_{index}'] = {"Name" : bucket.name}
        index+=1

    return buckets


instances = print_instances()
buckets = Buckets_list()

json_output = {"instances" : instances , "Buckets" : buckets}

print("\n--------- AWS REPORT ---------\n")
print(json_output)



print("\nAWS Report is saved in \"aws_report.json\" file.\n")
with open("aws_report.json","w") as json_output_file:
    json.dump(json_output,json_output_file)