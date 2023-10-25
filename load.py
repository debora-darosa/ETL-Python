import pymongo
from pymongo import MongoClient


def salvar_livros_no_mongodb(livro):
 
    client = MongoClient("mongodb+srv://debora_darosa:******@books-pt.oqfpfy1.mongodb.net/?retryWrites=true&w=majority") 

    # Acesse o banco de dados (ou crie um novo)
    db = client["books-pt"]  # Substitua pelo nome do seu banco de dados

    # Acesse a coleção onde você deseja salvar os livros
    colecao = db["livros"]

    # Insira o livro no MongoDB
    colecao.insert_one(livro)


def main():
  with open("generated_title.txt", "r") as file:
    titulo = file.read()

  # Crie um documento de livro com o título
  livro = {
      'titulo': titulo,
  }

  salvar_livros_no_mongodb(livro)