#!/bin/bash
uvicorn server.app:app --host 0.0.0.0 --port 8000 &
streamlit run frontend/main.py --server.port 8501 --server.headless true
