# Simple Devops API using FastAPI

## Aim


Our Goal is to **convert our Python logic into a simple API**.

Till now, we have:
- Written Python scripts
- Run them from terminal
- Used AWS and automation

Today, we will learn how DevOps engineers:
- Wrap Python logic inside an API
- Expose it using HTTP endpoints
- Build internal tools for teams

We will use **FastAPI** to build a **simple DevOps-style API**.


## Usage : 

```bash
git clone <repo-url> 
cd '.\day-09\Devops API with FastAPI\'
```


### Setting up python virtual environment

```bash
python -m venv project-env
.\project-env\Scripts\Activate.ps1  # for windows (in VS CODE)
```


### Install requirements

```bash
pip install -r requirements.txt
```


### Run Application

```bash
python main.py
```


### Access at Browser Endpoint

```bash
Open http://127.0.0.1:8000 in browser
```


### Getting response from all APIs

```bash
Open http://127.0.0.1:8000/health              # for system health 
Open http://127.0.0.1:8000/logs                # for checking log file 
Open http://127.0.0.1:8000/aws/ec2             # for ec2 instances list 
Open http://127.0.0.1:8000/aws/s3-list         # for s3 buckets list 
Open http://127.0.0.1:8000/aws/s3-buckets      # for s3 new and old buckets 
Open http://127.0.0.1:8000/aws/iam-list        # for iam users list 
Open http://127.0.0.1:8000/aws/bill            # for aws current month bill 
```

### Response is in JSON format 

```bash

# When hit http://127.0.0.1:8000/health
{
  "cpu_percentage": 41.9,
  "CPU_status": "CPU is working fine",
  "disk_percentage": 18.4,
  "Disk_status": "You still have some disk space left",
  "memory_percentage": 92.6,
  "Memory_status": "Memory is about to get full"
}


# When hit http://127.0.0.1:8000/aws/ec2
{
"instances": {
"instance_1": {
"Name": "First_Instance_Name",
"Id": "i-123xyz",
"State": "stopped"
},
"instance_2": {
"Name": "Second_Instance_Name",
"Id": "i-456abc",
"State": "running"
}
}
}



# When hit http://127.0.0.1:8000/aws/s3-list
{
"buckets": {
"bucket_1": {
"Name": "first_bucket_name"
},
"bucket_2": {
"Name": "second_bucket_name"
},
"bucket_3": {
"Name": "third_bucket_name"
},
"bucket_4": {
"Name": "fourth_bucket_name"
}
}
}



# When hit http://127.0.0.1:8000/aws/s3-buckets
{
"Total_buckets": 4,
"Total_New_Buckets": 3,
"New_buckets": [
"first_bucket_name",
"second_bucket_name",
"third_bucket_name"
],
"Total_Old_Buckets": 1,
"Old_buckets": [
"fourth_bucket_name"
]
}


# When hit http://127.0.0.1:8000/aws/iam-list
{
  "User_1": "user1",
  "User_2": "user2"
}


# When hit http://127.0.0.1:8000/aws/bill
{
  "Total AWS Cost of the month until 2026-05-13": " $0.0000000735 "
}


# When hit http://127.0.0.1:8000/logs
{
  "INFO": 25,
  "WARNING": 11,
  "ERROR": 13,
  "Suggestion": "You need to review your code"
}

```