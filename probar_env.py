from dotenv import load_dotenv
import os

load_dotenv()

print("CLOUD_NAME:", os.getenv("CLOUD_NAME"))
print("API_KEY:", os.getenv("API_KEY"))
print("API_SECRET:", os.getenv("API_SECRET"))
