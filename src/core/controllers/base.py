from typing import List

from django.conf import settings


def get_request_files(name, file) -> dict:
    if file:
        return {name: file}
    return {}


def validate_file_extensions(file, allowed_file_config) -> bool:
    allowed_extensions = [extension for extension in allowed_file_config]
    extension = file.name.split(".").pop()
    if extension not in allowed_extensions:
        raise Exception(f"Extension not allowed, only {allowed_extensions} is supported")


def validate_request(
    request,
    file,
    allowed_file_config: List[str] = settings.REQUEST_ALLOWED_FILE_CONFIG,
) -> None:
    request_content_type = request.headers.get("content-type", "")

    if "multipart/form-data" not in request_content_type:
        raise Exception("Invalid content-type, only multipart/form-data is supported")

    if not file:
        raise Exception("At least one file is required")

    validate_file_extensions(file, allowed_file_config)
