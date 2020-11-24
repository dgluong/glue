import boto3


def upload_file(file_name, bucket):
    """
    Upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

    return response


def download_file(file_name, bucket):
    """
    Download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output = f"download/{file_name}"
    # output += file_name
    s3.Bucket(bucket).download_file(file_name, output)

    return output


def list_files(bucket):
    """
    List files in a given S3 bucket
    """
    s3 = boto3.client('s3')
    contents = []
    try:
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            contents.append(item)
    except Exception as e:
        pass

    return contents
