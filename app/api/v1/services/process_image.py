import os
from functools import lru_cache
from typing import Optional

import joblib
from PIL import Image
import io
import numpy as np
from fastapi import UploadFile
from sklearn.svm import SVC

from ..schemas.image_schema import ImageRequest
from ..utils import process_image
from ..exceptions import exceptions

MODEL_PATH = "app/api/v1/models/svm_digits_model.pkl"  # Or .joblib


@lru_cache(maxsize=1)
def load_svm_model() -> SVC:
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"SVM model not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


async def predict_image_array(data: ImageRequest) -> Optional[int]:
    image_array = np.array(data.array)

    if image_array.shape != (8, 8):
        raise exceptions.InvalidImageSize

    return await predict_array(image_array)


async def predict_image_file(file: UploadFile) -> Optional[int]:
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert('L')  # Convert to grayscale

    # Resize image to 8x8 (digits dataset images are 8x8)
    image = image.resize((8, 8), Image.ANTIALIAS)
    image_array = np.array(image)
    return await predict_array(image_array)


async def predict_array(image_array: np.array):
    # Preprocess image and extract HOG features
    features = await process_image.preprocess_image(image_array)

    # Reshape the features to match the model input shape
    features = features.reshape(1, -1)

    # Make prediction using the pre-trained model
    model = load_svm_model()
    prediction = model.predict(features)
    return prediction[0] if len(prediction) > 0 else None
