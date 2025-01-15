from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import pipeline as pipeline_crud
from app.models import pipeline as pipeline_model
from app.schemas import pipeline as pipeline_schema
from app.db.database import SessionLocal,engine

pipeline_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/pipelines/", response_model=pipeline_schema.Pipeline)
def create_pipeline(pipeline: pipeline_schema.PipelineCreate, db: Session = Depends(get_db)):
    return pipeline_crud.create_pipeline(db=db, pipeline=pipeline)

@router.get("pipelines/{pipeline_id}", response_model=pipeline_schema.Pipeline)
def read_pipeline(pipeline_id: int, db: Session = Depends(get_db)):
    db_pipeline = pipeline_crud.get_pipeline(db, pipeline_id=pipeline_id)
    if db_pipeline is None:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    return db_pipeline

@router.get("/pipelines/", response_model=list[pipeline_schema.Pipeline])
def read_pipelines(skip: int = 0, limit: int =10, db: Session = Depends(get_db)):
    pipelines = pipeline_crud.get_pipelines(db, skip=skip, limit=limit)
    return pipelines