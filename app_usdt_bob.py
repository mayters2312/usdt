import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="USDT/BOB Histórico", layout="centered")

st.title("📈 Histórico USDT / BOB - Mercado P2P Bolivia")
st.markdown("Este gráfico se actualiza automáticamente cada vez que visitas esta página.")

# Obtener datos
url = "https://dolarboliviahoy.com/api/getHistoricalData"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

    # Convertir columnas
    df['buy_average_price'] = pd.to_numeric(df['buy_average_price'], errors='coerce')
    df['sell_average_price'] = pd.to_numeric(df['sell_average_price'], errors='coerce')
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['date'], df['buy_average_price'], label='Compra Promedio (BOB/USDT)', marker='o')
    ax.plot(df['date'], df['sell_average_price'], label='Venta Promedio (BOB/USDT)', marker='x')
    ax.set_title('Histórico USDT BOB - Mercado P2P')
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Precio (BOB)')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
else:
    st.error(f"❌ Error {response.status_code} al acceder a los datos.")
