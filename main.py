import streamlit as st
from pymongo import MongoClient
import uuid
import json
import xml.etree.ElementTree as ET

# Conectando ao MongoDB

client = MongoClient('localhost', 27017)
db = client['Desafio_Genesis']
collection = db['teste']

st.title("Web Service")

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    ################CORRIGIR A DATA############################
    input_date = st.number_input(label="Insira a data", format="%d", step=1)
    input_button_submit = st.form_submit_button("Enviar")

if input_button_submit:
    
    # Gerando um ID aleatório
    unique_id = str(uuid.uuid4())

    registro = {
        "_id": unique_id,
        "nome": input_name,
        "data": input_date,
        
    }
    
    # Exportando os dados para o MongoDB e o retorno
    collection.insert_one(registro)
    st.write("Dados enviados com sucesso para o MongoDB.")
    
    # Exportando para JSON
    json_data = json.dumps(registro, indent=4)
    with open("data.json", "w") as json_file:
        json_file.write(json_data)
    st.write("Dados exportados para JSON com sucesso.")
    
    # Exportando para XML
    root = ET.Element("root")
    for key, value in registro.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)
    tree = ET.ElementTree(root)
    tree.write("data.xml")
    st.write("Dados exportados para XML com sucesso.")


