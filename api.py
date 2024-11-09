from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import main

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

@app.post("/catalog")
async def catalog(request: URLRequest):  # Extrai o JSON do corpo da requisição
    url = request.url  # Acessa o valor de "url"
    
    # Verifique se 'url' existe e é uma string antes de passar para a função 'acess'
    if isinstance(url, str):
        result = main.process_url(url)
        return {"result": result}
    else:
        return {"error": "Invalid URL"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
