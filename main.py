import io
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
from ultralytics import YOLO

app = FastAPI(
    title="Plant Disease Detection API",
    description="YOLOv8-based plant disease classification microservice",
    version="1.0.0"
)

# Dynamic path configuration to prevent OS path conflicts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "weights", "best.pt")

try:
    # Initializing the YOLOv8 model
    model = YOLO(MODEL_PATH)
    print(f"✅ AI Model ({MODEL_PATH}) successfully loaded into memory.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    raise RuntimeError("Model file not found or could not be initialized.")


@app.get("/")
def read_root():
    return {"status": "healthy", "message": "API is running smoothly!"}


@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    # Validate that the uploaded file is indeed an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")

    try:
        # Read image bytes and convert to PIL Image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # Ensure image is in RGB format (YOLO requirement)
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Execute YOLOv8 classification inference
        results = model.predict(source=image, imgsz=224, verbose=False)
        result = results[0]

        # Extract the top-1 predicted class and its confidence score
        top1_idx = result.probs.top1
        predicted_class = result.names[top1_idx]
        confidence = float(result.probs.top1conf)

        return {
            "status": "success",
            "prediction": predicted_class,
            "confidence": round(confidence, 4),
            "all_predictions": {result.names[i]: float(prob) for i, prob in enumerate(result.probs.data)}
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error occurred: {str(e)}")