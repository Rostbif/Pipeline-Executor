from fastapi import FastAPI
import logging
from app.routes import pipeline
# from app.db.database import engine
# from app.models import pipeline as pipeline_model

# run the server using the following command: uvicorn app.main:app --reload

# pipeline_model.Base.metadata.create_all(bind=engine)


# init logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(pipeline.router)

@app.get("/")
def read_root():
    logger.info({"message": "reached the test endpoint"})
    return{"message: Welcome ofir to the Pipeline CRUD service"}

