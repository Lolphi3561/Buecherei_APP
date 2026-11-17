from datetime import date

from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import BaseModel, Field, ValidationError, field_validator
from sqlalchemy.orm import Session

from fastapi_restful.cbv import cbv
from routers.base import BaseAPI
import models

router = APIRouter(prefix="/loans", tags=["Loan"])


class LoanCreate(BaseModel):    
    bookId: int = Field(..., gt=0)
    userId: int = Field(..., gt=0),
    borrowedAt: date
    dueDate: date
    returnedAt: date
    status: str

class LoanResponse(LoanCreate):
    id: int = Field(..., gt=0)



@cbv(router)
class LoanAPI(BaseAPI):
    db: Session = Depends(get_db)
        
    @router.post("/loans", response_model=LoanResponse)
    def creat_loan(self, loan:LoanCreate):
        db_loan = models.LOANS()
        self.db.add(db_loan)
        self.db.commit()
        self.db.refresh(db_loan)
        return db_loan

    @router.patch("/loans/{id}", response_model = LoanResponse)
    def patch_loan(self):
        #TODO !!!!!!!!!!!!