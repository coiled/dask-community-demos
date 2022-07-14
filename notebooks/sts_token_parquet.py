import boto3
import dask

# this should be key and secret for IAM user, and s3 path that user can write to
user_key = "***"
user_secret = "***"
s3_path = "s3://coiled-nat-test-account-0/local-write"

# get temporary credentials
session = boto3.session.Session(
    aws_access_key_id=user_key, aws_secret_access_key=user_secret
)
sts = session.client("sts")
token_credentials = sts.get_session_token()["Credentials"]
storage_options = {
    "key":token_credentials["AccessKeyId"],
    "secret":token_credentials["SecretAccessKey"],
    "token":token_credentials["SessionToken"]
}

print(f"STS expiration: {token_credentials['Expiration']}")

# make some sample data
df = dask.datasets.timeseries("2001", "2002", partition_freq="2w")

# write it to s3
df.to_parquet(s3_path, storage_options=storage_options)
