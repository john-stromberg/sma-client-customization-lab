from fastapi import FastAPI
from src.core import run_placeholder_analysis
app = FastAPI(title='sma-client-customization-lab')
@app.get('/health')
def health():
    return run_placeholder_analysis()

