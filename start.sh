#!/bin/bash
pip install -r requirements.txt
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
