import pytest

from app.api.v1.schemas import image_schema
from app.api.v1.services import process_image

DIGIT_0 = [
    [0.0, 0.0, 5.0, 13.0, 9.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 13.0, 15.0, 10.0, 15.0, 5.0, 0.0],
    [0.0, 3.0, 15.0, 2.0, 0.0, 11.0, 8.0, 0.0],
    [0.0, 4.0, 12.0, 0.0, 0.0, 8.0, 8.0, 0.0],
    [0.0, 5.0, 8.0, 0.0, 0.0, 9.0, 8.0, 0.0],
    [0.0, 4.0, 11.0, 0.0, 1.0, 12.0, 7.0, 0.0],
    [0.0, 2.0, 14.0, 5.0, 10.0, 12.0, 0.0, 0.0],
    [0.0, 0.0, 6.0, 13.0, 10.0, 0.0, 0.0, 0.0],
]
DIGIT_8 = [
    [0.0, 0.0, 0.0, 3.0, 12.0, 13.0, 3.0, 0.0],
    [0.0, 0.0, 3.0, 15.0, 16.0, 16.0, 5.0, 0.0],
    [0.0, 0.0, 8.0, 13.0, 16.0, 16.0, 5.0, 0.0],
    [0.0, 0.0, 1.0, 6.0, 16.0, 16.0, 4.0, 0.0],
    [0.0, 0.0, 0.0, 3.0, 13.0, 16.0, 4.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 6.0, 16.0, 5.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 10.0, 16.0, 2.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 12.0, 16.0, 3.0, 0.0],
]
INVALID_ARRAY = [
    [0.0, 0.12, 2],
    [77, 4],
    [],
]


@pytest.mark.asyncio
@pytest.mark.parametrize("digit, expected", [
    (DIGIT_0, 0),
    (DIGIT_8, 8)
])
async def test_process_image_predict_array(change_to_root_directory, digit, expected):
    res = await process_image.predict_image_array(image_schema.ImageRequest(array=digit))
    assert res == expected


@pytest.mark.asyncio
async def test_process_image_predict_array_invalid(change_to_root_directory):
    with pytest.raises(ValueError):
        await process_image.predict_image_array(image_schema.ImageRequest(array=INVALID_ARRAY))
