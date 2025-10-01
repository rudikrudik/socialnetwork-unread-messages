from pydantic import BaseModel


class UserAddCount(BaseModel):
    from_user: int
    to_user: int
