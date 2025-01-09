from typing import List

from ninja import Router, UploadedFile

from src.core.schemas.file import FileOutput
from src.core.services.file_service import FileService

from .base import get_request_files, validate_request

ingestion_router = Router(tags=["Ingestion"])

ingestion_router.post("/ingestion/files", response={201: FileOutput})
def post_file(
    request,
    csv_file: UploadedFile = None,
):
    file = get_request_files("csv_file", csv_file)
    validate_request(
        request=request,
        file=file,
    )
    file_service = FileService(file=file)
    result = file_service.process()

    return {"file_ingested": result}
