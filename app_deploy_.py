# %%
import yfinance as yf
import streamlit as st  
import pandas as pd
import random
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import numpy as np
import ffn
import datetime
#Creamos nuestro objeto portafolio con los precios de cierre y los ordenamos con todos los registros que tenemos

result=False
if result==False:
    
    def get_data(stocks_symbols, start):
        portafolio = pd.DataFrame()
        for i, stock in enumerate(stocks_symbols):
            portafolio[stock] = yf.Ticker(stock).history(period="max")["Close"].sort_index().loc[start:]
        return portafolio


    #if c:
        #Elegimos nuestras acciones, en este caso serán APPLE, MICROSOFT, AMAZON y GOOGLE
    stocks_symbols = ['NVR', 'GOOGL', 'AZO', 'CMG', 'MTD', 'TSLA', 'BLK', 'EQIX', 'ORLY', 'REGN', 'TDG', 'AVGO', 'SIVB', 'CHTR', 'NOW']
    df = get_data(stocks_symbols, "01-01-2021")

    st.title('PROYECTO FINAL --> DEEP LEARNING EN MERCADOS FINANCIEROS?')
    "Asi se ven los datos con los que trabajaremos , tenemos DF de 15 activos "    
    st.write(df)




    "Asi se ven nustros datos graficados"

    options = st.multiselect(
        'Dame activos a evaluar',
        ['NVR', 'GOOGL', 'AZO', 'CMG', 'MTD', 'TSLA', 'BLK', 'EQIX', 'ORLY', 'REGN', 'TDG', 'AVGO', 'SIVB', 'CHTR', 'NOW'],
        ['NVR', 'GOOGL', 'AZO', 'CMG', 'MTD', 'TSLA', 'BLK', 'EQIX', 'ORLY', 'REGN', 'TDG', 'AVGO', 'SIVB', 'CHTR', 'NOW'])


    st.line_chart(df[options])




    "El precio de hoy"

    def get_data2(stocks_symbols, start, end):
        portafolio = pd.DataFrame()
        for i, stock in enumerate(stocks_symbols):
            portafolio[stock] = yf.Ticker(stock).history(period="max")["Close"].sort_index()
        return portafolio.iloc[-1]





    d = st.date_input(
        "Dame una fecha despues de la fecha estandar ",
        datetime.date(2020, 5, 5))

    df2 = get_data2(stocks_symbols, d,d)
    st.write(df2)

    option = st.selectbox(
        'Selecciona un activo ',
        ('NVR', 'GOOGL', 'AZO', 'CMG', 'MTD', 'TSLA', 'BLK', 'EQIX', 'ORLY', 'REGN', 'TDG', 'AVGO', 'SIVB', 'CHTR', 'NOW'))


    #st.pyplot(df2)
    st.metric(label=option, value=df2[option], delta="1.99 %")

"Pesos de las acciones con nuestro modelo "

stocks_symbols = ['NVR', 'GOOGL', 'AZO', 'CMG', 'MTD', 'TSLA', 'BLK', 'EQIX', 'ORLY', 'REGN', 'TDG', 'AVGO', 'SIVB', 'CHTR', 'NOW']
n = len(stocks_symbols)
a = np.random.uniform(size = n)
sum = np.sum(a)
a = a/sum
np.sum(a)

pesos = pd.DataFrame()
pesos['acciones'] = stocks_symbols
pesos['weights'] = a
pesos.set_index('acciones',inplace = True)




result = st.button('Precio de las acciones de hoy')

if result:
     st.write(pesos)





