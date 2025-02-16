# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
