import os
from typing import Union
from zipfile import ZipFile

import boto3
import botocore
from sagaconfig import config

s3 = boto3.resource(
    "s3",
    region_name=config["aws"]["region"],
    aws_access_key_id=config["aws"]["access_key_id"],
    aws_secret_access_key=config["aws"]["secret_access_key"],
)

s3_client = boto3.client(
    "s3",
    region_name=config["aws"]["region"],
    aws_access_key_id=config["aws"]["access_key_id"],
    aws_secret_access_key=config["aws"]["secret_access_key"],
)

bucket = config["s3"]["bucket"]


def download(s3_path: str, local_file: str) -> None:
    """Download a file from an Amazon S3 bucket.

    Args:
        s3_path: path of the file in S3
        local_file: path to the local file

    Requires:
        S3_path and local_file are not None and have correct
        values

    Raises:
        ClientError if the file cannot be downloaded

    Effects:
        The file is downloaded

    """
    try:
        s3.Bucket(bucket).download_file(s3_path, local_file)
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print("The object {} does not exist.".format(s3_path))
        raise e


def download_if_not_exist(
    s3_path: str,
    local_file: str,
    zip_tmp: Union[str, None] = None,
    out_folder: Union[str, None] = None,
) -> None:
    """Download a file from Amazon S3 bucket if it not exists locally.

    Note that this function support zip download and extraction with the
    zip_tmp and out_folder keyword arguments.

    Args:
        s3_path: path in S3 bucket
        local_file: path for the local file
        zip_tmp: temporary directory for zip file extraction
        out_folder: final destination for zip extraction

    Requires:
        S3_path and local_file are not None and have correct
        values

    Raises:
        ClientError if the file cannot be downloaded

    Effects or Returns:
        Value

    """
    if not os.path.exists(local_file):
        if zip_tmp:
            # Download in zip tmp
            download(s3_path, zip_tmp)

            # Extract zip
            with ZipFile(zip_tmp, "r") as zip_file:
                zip_file.extractall(out_folder)

            # Remove archive
            os.remove(zip)
        else:
            # Download
            download(s3_path, local_file)
        print("{} downloaded".format(s3_path))
    else:
        print("{} Already downloaded".format(s3_path))


def upload_file(file_name: str, s3_path: str) -> None:
    """Upload the given file to specified path in s3 bucket.

    Args:
        file_name: the local file
        s3_path: destination in s3 bucket

    Requires:
        file_name and s3_path are not None and have valid values

    """
    s3_client.upload_file(file_name, bucket, s3_path)
