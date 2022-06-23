from pydantic import BaseModel, Field

# メモ参照定義
class MemoSchema (BaseModel):
    memo_id: int = Field()
    team: str = Field()
    content: str = Field(max_length=100)

    class Config:
        orm_mode = True

# メモ登録定義
class MemoCreatingSchema (BaseModel):
    team: str = Field()
    content: str = Field(max_length=100)
    
    class Config:
        orm_mode = True
