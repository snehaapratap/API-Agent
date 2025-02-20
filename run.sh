#!/bin/bash
echo "Starting Graph RAG Setup..."
python backend/storecode.py
python backend/storeembeddings.py
uvicorn backend/api:app --reload
