from pydantic import BaseModel


class Account(BaseModel):
    first_name: str
    last_name: str
    document_id: str
