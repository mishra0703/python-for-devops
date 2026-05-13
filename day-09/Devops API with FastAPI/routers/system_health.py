from fastapi import APIRouter , HTTPException
from services.system_health_check import check_system_health

router = APIRouter()

@router.get("/health" , status_code=200)
def health_check():
    try:        
        metrics = check_system_health()
        return metrics
    except:
       raise HTTPException(
           status_code=500,
           detail="Internal Server Error"
       )

