#(A "Planta": Só tem a classe Livro com seus atributos)
from sqlalchemy import Column, Integer, String, Date 
from database import Base #importar base do nosso arquivo 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    # Isso cria uma "lista mágica" de livros neste autor
    livros = relationship("Livro", back_populates="autor")

class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False) #nullable=False obriga a ter título

   # Em vez de uma coluna texto 'autor', guardamos o ID
    autor_id = Column(Integer, ForeignKey('autores.id'))

    # Isso cria o link reverso para facilitar o acesso no Python
    autor = relationship("Autor", back_populates="livros")

    data_publicacao = Column(Date)
    genero = Column(String)

    #ao buscar os mesmos 3 livros ira mostrar o nome como um 'print' de uma melhor forma
    def __repr__(self):
        return f"<Livro(titulo='{self.titulo}')"
    
    #NOVO MÉTODO (PODER)
    def apresentar_se(self):
        return f"Olá, eu sou o livro '{self.titulo}' e custaria R$50,00." 
    
    