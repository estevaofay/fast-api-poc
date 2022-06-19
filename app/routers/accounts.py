from typing import List

from fastapi import APIRouter

from app.models.account import Account

router = APIRouter()


@router.post("/accounts/", response_model=List[Account])
async def create_account(account: Account):
    return [account]