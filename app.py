import streamlit as st
import yfinance as yf
import smtplib
import time
from email.message import EmailMessage
def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "Jodha3699@gmail.com"
    msg['To'] = "Jodha3699@gmail.com"
    server = smtplib.SMTP_SSL(jodha1234567...,,)
    server.login("Jodha3699@gmail.com", "jodha123456..,,,")
    server.send_message(msg)
    server.quit()
st.title("Bitcoin Trading Bot")
ticker = "BTC-USD"
time.sleep(2)
data = yf.Ticker(ticker).history(period="1d", interval="15m")
current_price = data['Close'].iloc[-1]
sma_20 = data['Close'].rolling(window=20).mean().iloc[-1]
st.write(f"Current Price of Bitcoin: ${current_price:.2f}")
st.write(f"SMA 20: ${sma_20:.2f}")
entry_price = 60000.00 
profit = current_price - entry_price
st.write(f"Unrealized Profit/Loss: ${profit:.2f}"
if current_price > sma_20:
    st.success("Signal: BUY"
    # send_email("Bitcoin Alert", f"BUY Signal! Price: {current_price}")
elif current_price < sma_20:
    st.error("Signal: SELL")
    # send_email("Bitcoin Alert", f"SELL Signal! Price: {current_price}. Profit: {profit}")
else:
    st.warning("Signal: WAIT")
