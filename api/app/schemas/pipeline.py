from pydantic import BaseModel

class PipelineBase(BaseModel):
    name: str
    description: str

class PipelineCreate(PipelineBase):
    pass

class Pipeline(PipelineBase):
    id: int

    class Config:
        orm_mode = True