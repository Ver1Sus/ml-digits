from fastapi import HTTPException


class EmptyImage(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.detail = "Empty image"


class InvalidImageSize(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.detail = "Image must be 8x8 in size"

