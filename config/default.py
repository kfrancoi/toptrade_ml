import os

config = {
    "aws": {
        "access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
        "secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "region": os.getenv("AWS_REGION") or "eu-west-1",
    },
    "s3": {
        "bucket": os.getenv("S3_BUCKET"),
        "raw": [],
        "resources": [],
        "processed": []
    }
}
