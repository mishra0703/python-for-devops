from fastapi import APIRouter , HTTPException
from services.log_analyzer_service import summary 

router = APIRouter()


@router.get("/logs",status_code=200)
def get_logs_report():
    try:
        log_summary = summary()
        return log_summary
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )