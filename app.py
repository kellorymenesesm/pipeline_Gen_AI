import streamlit as st
from datetime import datetime,time
from contrato import Vendas
from pydantic import ValidationError
from database import salvar_no_postgres

def main():

    st.title("Sistema de CRM e vendas do ZapFlow - V1.0")
    email = st.text_input("Campo de texto para inserção de e-mail do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora =st.time_input("Hora da compra", value=time(9, 0)) #valor padrão: 09:00
    valor = st.number_input("valor da venda",min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos vendidos",min_value=1, step=1)	
    produto = st.selectbox("Campo de seleção para escolher o produto vendido.",["Zapflow com Gemini", "Zapflow com ChatGPT", "Zapflow com Llama3.0"])

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,  
                quantidade = quantidade, 
                produto = produto 

            )
       
            st.write(venda)
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")

if __name__ == "__main__":
    main()