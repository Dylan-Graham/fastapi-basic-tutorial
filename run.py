import os

os.system("source venv/bin/activate")
os.system("uvicorn tutorial:app --reload")