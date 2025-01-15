from fastapi import FastAPI
# from app.routes import pipeline
# from app.db.database import engine
# from app.models import pipeline as pipeline_model

# pipeline_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.include_router(pipeline.router)

@app.get("/")
def read_root():
    return{"message: Welcome ofir to the Pipeline CRUD service"}

