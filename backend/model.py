import logging
import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

GEMINI_MODEL = "gemini-3-flash-preview"

PROMPT = (
    "This video shows a person communicating using Indian Sign Language (ISL). "
    "Describe what they are conveying."
)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def predict(video_path: str) -> str:
    file_size = os.path.getsize(video_path) / (1024 * 1024)
    logger.info(f"Uploading video to Gemini — file: {os.path.basename(video_path)}, size: {file_size:.2f} MB")

    uploaded = client.files.upload(file=video_path)
    logger.info(f"Upload complete — file ID: {uploaded.name}, state: {uploaded.state}")

    wait_count = 0
    while uploaded.state == "PROCESSING":
        wait_count += 1
        logger.info(f"Waiting for Gemini to process file... (attempt {wait_count})")
        time.sleep(3)
        uploaded = client.files.get(name=uploaded.name)

    if uploaded.state == "FAILED":
        logger.error("Gemini file processing failed.")
        raise RuntimeError("Gemini file processing failed.")

    logger.info(f"File ready — state: {uploaded.state}. Sending prompt to {GEMINI_MODEL}")

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=[uploaded, PROMPT],
    )

    logger.info("Response received. Cleaning up uploaded file.")
    client.files.delete(name=uploaded.name)

    result = response.text.strip()
    logger.info(f"Done — response length: {len(result)} chars")
    return result
