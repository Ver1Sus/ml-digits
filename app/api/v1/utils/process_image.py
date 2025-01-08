import numpy as np
from skimage import filters, feature
from skimage.exposure import rescale_intensity
from skimage.util import img_as_float
from ..exceptions.exceptions import EmptyImage


# Preprocessing the image and extracting features
async def preprocess_image(image: np.array) -> np.array:
    # Convert image to float and normalize
    img = img_as_float(image)
    img = (img - np.min(img)) / (np.max(img) - np.min(img))  # Normalize to [0, 1]

    if np.isnan(img).any():
        raise EmptyImage

    # Apply Gaussian filter to reduce noise
    img = filters.gaussian(img, sigma=0.5)

    # Enhance contrast using Histogram Equalization
    img = rescale_intensity(img, in_range='image', out_range=(0, 1))

    # Extract HOG features
    return feature.hog(
        img,
        orientations=9,
        pixels_per_cell=(4, 4),
        cells_per_block=(2, 2),
        visualize=False,
        feature_vector=True,
    )
