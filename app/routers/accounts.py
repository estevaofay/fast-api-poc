from fastapi import APIRouter

from app.models.account import Account

router = APIRouter()


@router.post("/accounts/", response_model=Account)
async def create_account(account: Account):
    return account
