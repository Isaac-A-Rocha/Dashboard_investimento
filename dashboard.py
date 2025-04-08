import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_csv("dados_investimentos.csv")

# Título do dashboard
st.title("📊 Dashboard de Investimentos - Empresa X")

# Filtro de ano
anos = df["ano"].unique()
ano_selecionado = st.selectbox("Selecione o ano:", sorted(anos))

df_ano = df[df["ano"] == ano_selecionado]

# Gráfico de barras de retorno por empresa
st.subheader("Retorno Total por Empresa")
retornos = df_ano.groupby("empresa")["retorno"].sum().sort_values()
fig1, ax1 = plt.subplots()
retornos.plot(kind="barh", ax=ax1, color="skyblue")
ax1.set_xlabel("Retorno Total (R$)")
st.pyplot(fig1)

# Gráfico de linhas de lucro/prejuízo por mês
st.subheader("Lucro ou Prejuízo Mensal por Empresa")
fig2, ax2 = plt.subplots()
for empresa in df_ano["empresa"].unique():
    dados = df_ano[df_ano["empresa"] == empresa]
    ax2.plot(dados["mes"], dados["lucro_prejuizo"], label=empresa, marker='o')
ax2.set_xlabel("Mês")
ax2.set_ylabel("Lucro / Prejuízo (R$)")
ax2.legend()
st.pyplot(fig2)

# Empresa com melhor desempenho
desempenho_total = df_ano.groupby("empresa")["lucro_prejuizo"].sum()
melhor = desempenho_total.idxmax()
lucro = desempenho_total.max()

st.success(f"🏆 Em {ano_selecionado}, a empresa com melhor desempenho foi **{melhor}**, com um lucro total de **R$ {lucro:,.2f}**.")