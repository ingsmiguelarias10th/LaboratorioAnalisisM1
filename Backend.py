from fastapi import FastAPI
app = FastAPI()

@app.get("/api/estudiantes")
def listar_estudiantes():
    return [{"id": 1, "nombre": "Ana"}]

@app.post("/api/estudiantes")
def crear_estudiante(estudiante: dict):
    return {"message": "Estudiante creado", "estudiante": estudiante}