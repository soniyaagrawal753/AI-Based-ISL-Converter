import os
import tempfile

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from model import predict

app = FastAPI(title="ISL Interpreter")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class PredictResponse(BaseModel):
    interpretation: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
async def predict_endpoint(video: UploadFile = File(...)):
    if not video.content_type.startswith("video/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be a video.")

    suffix = os.path.splitext(video.filename)[-1] or ".mp4"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await video.read())
        tmp_path = tmp.name

    try:
        result = predict(tmp_path)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.unlink(tmp_path)

    return PredictResponse(interpretation=result)
