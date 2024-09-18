import streamlit as st
from datetime import datetime,time
import contrato

def main():

    st.title("Sistema de CRM e vendas do ZapFlow - V1.0")
    email = st.text_input("Campo de texto para inserção de e-mail do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora =st.time_input("Hora da compra", value=time(9, 0)) #valor padrão: 09:00
    valor = st.number_input("valor da venda",min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos vendidos",min_value=1, step=1)	
    produto = st.selectbox("Campo de seleção para escolher o produto vendido.",["Zapflow com Gemini", "Zapflow com ChatGPT", "Zapflow com Llama3.0"])

    if st.button("Salvar"):
       
       data_hora = datetime.combine(data, hora)
       st.write("**Dados da Venda**")
       st.write(f"Email: {email}")
       st.write(f"Data e Hora da Compra: {data_hora}")
       st.write(f"Valor da Venda: R$ {valor:.2f}")
       st.write(f"Quantidade de  Produtos: {quantidade}")
       st.write(f"Produto Vendido: {produto}")

if __name__ == "__main__":
    main()