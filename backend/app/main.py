from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# inicializamos la aplicación fastapi
app = FastAPI(
    title="OmniAgent API",
    description="Microservicio backend para OmniAgent impulsado por CrewAI y Gemini Pro",
    version="0.1.0",
)

# configuramos cors para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endpoint de verificación de salud
@app.get("/health")
def check_health():
    return {"status": "ok", "message": "OmniAgent API funcionando correctamente"}

