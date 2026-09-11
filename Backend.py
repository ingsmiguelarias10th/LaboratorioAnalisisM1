from fastapi import FastAPI
app = FastAPI()

@app.get("/api/estudiantes")
def listar_estudiantes():
    return [{"id": 1, "nombre": "Ana"}]