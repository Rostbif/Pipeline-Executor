from sqlalchemy.orm import Session
from app.models import pipeline as pipeline_model
from app.schemas import pipeline as pipeline_schema

def get_pipeline(db: Session, pipeline_id: int):
    return db.query(pipeline_model.Pipeline).filter(pipeline_model.Pipeline.id == pipeline_id).first()

def get_pipelines(db: Session, skip: int = 0, limit: int = 10):
    return db.query(pipeline_model.Pipeline).offset(skip).limit(limit).all()

def create_pipeline(db: Session, pipeline: pipeline_schema.PipelineCreate):
    db_pipeline = pipeline_model.Pipeline(name=pipeline.name, description=pipeline.description)
    db.add(db_pipeline)
    db.commit()
    db.refresh(db_pipeline)
    return db_pipeline

