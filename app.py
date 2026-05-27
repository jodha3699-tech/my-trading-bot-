import streamlit as st
import time
import yfinance as yf
import time
st.title("🚀 500x Gold-Mean Quant Dashboard")

if 'running' not in st.session_state:
    st.session_state.running = False

def run_trading_bot():
    ticker = "SPY"
    time.sleep(2)
    data = yf.Ticker(ticker).history(period="1d", interval="15m")
    current_price = data['Close'].iloc[-1]
    sma20 = data['Close'].rolling(window=20).mean().iloc[-1]
    
    st.write(f"📈 Current Price of {ticker}: ${current_price:.2f}")
    st.write(f"📊 SMA 20: ${sma20:.2f}")
    
    if current_price < sma20:
        st.success("🟢 Signal: BUY")
    else:
        st.error("🔴 Signal: WAIT")

col1, col2 = st.columns(2)
with col1:
    if st.button("Start Bot"):
        st.session_state.running = True
with col2:
    if st.button("Stop Bot"):
        st.session_state.running = False

if st.session_state.running:
    st.write("📊 Trading is live...")
    run_trading_bot()
    time.sleep(5)
    st.rerun()

