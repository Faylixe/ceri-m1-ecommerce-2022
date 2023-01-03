import uvicorn
from src.api import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    uvicorn.run(app, port=5000)