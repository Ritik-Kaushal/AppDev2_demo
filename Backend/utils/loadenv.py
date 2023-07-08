import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(".env")

if os.getenv("DATABASE_URI") : print("Enviroment Fetched Variables Successfully")
else: print("Could not fetch the environment variables")