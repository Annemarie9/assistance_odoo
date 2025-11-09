
import os
from openai import OpenAI
#from dotenv import load_dotenv
from rag_system import RAGSYTEM
import streamlit as st  


#load_dotenv()

markdown_path="./markdown_data"
data_path = "./data"
doc_path="./BASE_DIR "
openai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
db_connection_str = st.secrets["DB_CONNECTION_STR"]
DB_NAME = st.secrets["DB_NAME"]
DB_USER = st.secrets["DB_USER"]
DB_PASSWORD = st.secrets["DB_PASSWORD"]
HOST = st.secrets["HOST"]
PORT = st.secrets["PORT"]

db_connection_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={HOST} port={PORT}"



def store_data():
    rag_system = RAGSYTEM(openai_client, db_connection_str, data_path=data_path, markdown_path=markdown_path)
    rag_system.store_documents()
    rag_system.store_markdown_documents()    



if __name__ == "__main__":
    store_data()
    