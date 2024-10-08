import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os
#Carregar variáveis do arquivo .env
load_dotenv()

#Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASS')

"""
Função para salvar no PostgresSQL os dados de vendas
"""

#Função para salvar os dados validados no PostgreeSQL
def salvar_no_postgres(dados: Vendas):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        #Inserção dos dados na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados inseridos com sucesso no banco de Dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de Dados {e}")

        
        