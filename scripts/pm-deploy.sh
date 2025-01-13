#!/bin/bash

PROJ=project-name

# Tag and push to GCP Container Registry
podman tag mldemo-wr gcr.io/$PROJ/mldemo-wr
podman push gcr.io/$PROJ/mldemo-wr --creds=oauth2accesstoken:$(gcloud auth print-access-token)

# Deploy to Cloud Run
gcloud run deploy mldemo-wr \
  --image gcr.io/$PROJ/mldemo-wr \
  --platform managed \
  --region asia-southeast1 \
  --allow-unauthenticated
