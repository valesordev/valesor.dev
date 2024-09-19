#!/bin/bash

# Variables
NAMESPACE=${NAMESPACE:-default}
SECRET_NAME=${SECRET_NAME:-minio-creds-secret}
TENANT_URL=${TENANT_URL:-http://minio-tenant:9000}
BUCKET_NAME=${BUCKET_NAME:-my-bucket}

# Install mc if not available
if ! command -v mc &> /dev/null
then
    echo "MinIO client (mc) is not installed. Installing..."
    curl -o mc https://dl.min.io/client/mc/release/linux-amd64/mc
    chmod +x mc
    mv mc /usr/local/bin/
fi

# Retrieve Access Key and Secret Key from Kubernetes Secret
echo "Retrieving credentials from Kubernetes secret..."
ACCESS_KEY=$(kubectl get secret $SECRET_NAME -n $NAMESPACE -o jsonpath='{.data.CONSOLE_ACCESS_KEY}' | base64 --decode)
SECRET_KEY=$(kubectl get secret $SECRET_NAME -n $NAMESPACE -o jsonpath='{.data.CONSOLE_SECRET_KEY}' | base64 --decode)

if [[ -z "$ACCESS_KEY" || -z "$SECRET_KEY" ]]; then
    echo "Failed to retrieve credentials. Exiting."
    exit 1
fi

echo "Credentials retrieved successfully."

# Configure mc alias
echo "Configuring mc alias..."
mc alias set myminio $TENANT_URL $ACCESS_KEY $SECRET_KEY

# Create the bucket
echo "Creating bucket '$BUCKET_NAME'..."
mc mb myminio/$BUCKET_NAME

if [ $? -eq 0 ]; then
    echo "Bucket '$BUCKET_NAME' created successfully."
else
    echo "Failed to create bucket."
    exit 1
fi

