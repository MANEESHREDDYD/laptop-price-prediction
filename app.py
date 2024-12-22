from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import traceback

# Initialize FastAPI app
app = FastAPI()

# Load the model
try:
    model = joblib.load("final_model_pipeline.joblib")  # Replace with the actual path to your model
except Exception as e:
    raise RuntimeError(f"Error loading model: {str(e)}")

# Input schema using Pydantic
class InputFeatures(BaseModel):
    brand_name: str
    model_name: str
    processor_brand: str
    processor_name: str
    processor_gnrtn: str
    ram_gb: str
    ram_type: str
    ssd: str
    hdd: str
    weight: str
    display_size: str
    warranty: int
    Touchscreen: str
    msoffice: str
    star_rating: float
    ratings: int
    reviews: int
    reactions: int
    warranty_importance: int

@app.get("/")
async def root():
    return {"message": "Welcome to the Laptop Prediction API!"}


# Prediction endpoint
@app.post("/predict")
async def predict(data: InputFeatures):
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([data.dict()])


        # Make predictions
        prediction = model.predict(input_data)

        # Return predictions and confidence
        return {
            "prediction": int(prediction[0]),
        }

    except Exception as e:
        # Log traceback for debugging purposes
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")