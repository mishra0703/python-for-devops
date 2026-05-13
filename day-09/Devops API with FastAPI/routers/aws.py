from fastapi import APIRouter , HTTPException
from services.aws_services import ec2_Instances,s3_Buckets,s3_Buckets_Manage,iam_users_list,calculate_bill

router = APIRouter()


@router.get("/ec2",status_code=200)
def get_instances():

    try:
        instances = ec2_Instances()
        return instances
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )


@router.get("/s3-list",status_code=200)
def get_buckets():

    try:
        buckets = s3_Buckets()
        return buckets
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )


@router.get("/s3-buckets",status_code=200)
def get_buckets_info():

    try:
        buckets = s3_Buckets_Manage()
        return buckets
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )


@router.get("/iam-list",status_code=200)
def get_iam_users_list():

    try:
        iam_users = iam_users_list()
        return iam_users
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )


@router.get("/bill",status_code=200)
def get_bill():
    try:
        bill = calculate_bill()
        return bill
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

