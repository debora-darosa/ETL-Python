import os
import csv
import tempfile
import requests
import pandas as pd


base_path = os.path.abspath(__file__ + "dados/source/books_sample.csv")

source_path = "dados/source/books_sample.csv"

raw_path = "dados/raw/catalogo.csv/catalogo.csv"

def create_folder_if_not_exists(path):
  if not os.path.exists(path):
    os.makedirs(path)

def save_new_raw_data():
  
    create_folder_if_not_exists(raw_path)
        # Open the CSV file in read mode
    with open(source_path, mode="r", encoding="utf-8",errors='ignore') as csv_file:
            reader = csv.DictReader(csv_file)
            
            row = next(reader)  # Get first row from reader
            print("[Extract] First row example:", row)

          # Open the CSV file in write mode
            with open(raw_path,mode="w",encoding="utf-8",errors='ignore' ) as csv_file:
              fieldnames = {
                "BNP record ID": "Book_ID",
                'ISBN': 'ISBN',
                'Material type': "Material_type",
                'Legal deposit number': "Legal_deposit_number",
                'Language of Text': "Language_of_text",
                'Language of Original Work': "Language_original",
                'Title': "Title",
                'Subtitle': "Subtitle",
                'Original title': "Original_title",
                'Edition': "Edition", 
                'Place of publicattion': "Place_of_publication",
                'Name of Publisher': "Publisher",
                'Date of Publication': "Date_of_publication",
                'Extent of Item': "Extent_of_item",
                'Dimensions': "Dimensions",
                'Series': 'Series', 
                'Volume': 'Volume', 
                'Universal Decimal Classification': "Decimal_Classification",
                'Authors': "Authors",
                'Image': "Imagens",
                'Persistent URL': "URL",
                '': "Extra",
              }
              writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
              writer.writerow(fieldnames)
              for row in reader:
                writer.writerow(row)
    return raw_path

def acessar_id(raw_path, id_choice):
  try:
    # Use a função read_csv do pandas para ler o arquivo CSV
    df = pd.read_csv(raw_path)

    # Verifique se o ID fornecido pelo usuário existe no DataFrame
    if id_choice in df['Book_ID'].values:
      # Use o método .loc para acessar o título com base no ID
      titulo = df.loc[df['Book_ID'] == id_choice, 'Title'].values[0]
      return titulo
    else:
      return "ID não encontrado no arquivo CSV."
  except Exception as e:
    return str(e)


def main():
  print("[Extract] Start")
  print(f"[Extract] Saving data from '{source_path}' to '{raw_path}'")
  raw_file = save_new_raw_data()
  print("[Extract] End")
  id_choice = int(input("Digite o ID do livro que você deseja: "))
  titulo = acessar_id(raw_file, id_choice)

  print(f"Resultado: {titulo}")