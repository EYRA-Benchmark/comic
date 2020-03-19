from django.core.exceptions import ValidationError

import requests

def isValidDockerhubImage(value: str):
    # example https://index.docker.io/v1/repositories/eyra/comic/tags/123
    try:
        image, tag = value.split(':')
    except ValueError:
        raise ValidationError("Invalid image format, use 'image:tag'")
    resp = requests.get(f"https://index.docker.io/v1/repositories/{image}/tags/{tag}")

    if not resp.status_code == 200:
        raise ValidationError(
            f"Id {value} does not exist in Dockerhub. "
        )