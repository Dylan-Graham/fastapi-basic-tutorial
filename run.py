import os

os.system("source venv/bin/activate")
os.system("uvicorn main:app --reload")