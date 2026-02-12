from pydantic import BaseModel

class AutorSchema(BaseModel):
    nome: str

class LivroSchema(BaseModel):
    titulo: str
    autor_id: int