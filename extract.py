path = "dados/source/catalogo.csv"
""" import os
import csv
import tempfile
import requests
from zipfile import ZipFile
import pandas as pd


#base_path = os.path.abspath(__file__ + ")

#source_path = ""

#raw_path = "dados/raw/catalogo.csv/catalogo.csv"

def create_folder_if_not_exists(path):
  if not os.path.exists(path):
    os.makedirs(path)

def save_new_raw_data():
  
    create_folder_if_not_exists(raw_path)
    with tempfile.TemporaryDirectory() as dirpath, ZipFile(source_path, "r") as zipfile:
        names_list = zipfile.namelist()
        csv_file_path =zipfile.extract(names_list[0], path=dirpath)
        # Open the CSV file in read mode
        with open(csv_file_path, mode="r", encoding="utf-8",errors='ignore') as csv_file:
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
              }
              writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
              writer.writerow(fieldnames)
              for row in reader:
                writer.writerow(row)
    return raw_path

def main(): """
"""  print("[Extract] Start")
  print(f"[Extract] Saving data from '{source_path}' to '{raw_path}'")
  save_new_raw_data()
  print("[Extract] End") """