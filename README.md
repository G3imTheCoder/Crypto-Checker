# 🚀 Crypto-Checker

A full-stack data engineering pipeline that tracks cryptocurrency prices in real-time, saves historical data, and sends email alerts when buying opportunities (dips) are detected. It also includes a live interactive dashboard.

## 📊 Features
* **Live Data Extraction:** Fetches real-time prices for BTC, ETH, SOL, and BNB.
* **Persistent Storage:** Saves all price history to a local CSV database.
* **Algorithmic Trading Alerts:** analyzing trends and sending email notifications when prices drop below the 5-point moving average.
* **Spam Protection:** Built-in cooldown logic prevents duplicate alerts within the same hour.
* **Interactive Dashboard:** A Streamlit web app to visualize price trends and volatility.

## 🛠️ Tech Stack
* **Python** (Core Logic)
* **Pandas** (Data Analysis)
* **Streamlit** (Web Dashboard)
* **YFinance** (Market Data API)
* **SMTP** (Email Automation)

## ⚙️ Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/G3imTheCoder/Crypto-Checker.git](https://github.com/G3imTheCoder/Crypto-Checker.git)
    cd Crypto-Checker
    ```

2.  **Install dependencies**
    ```bash
    pip install pandas yfinance streamlit python-dotenv
    ```

3.  **Setup Security (.env)**
    Create a file named `.env` in the root folder and add your credentials:
    ```ini
    EMAIL_USER=your_email@gmail.com
    EMAIL_PASSWORD=your_app_password_here  # Generate this in Google Account > Security
    TO_EMAIL=your_email@gmail.com
    ```

## 🚀 Usage

**1. Start the Tracker & Bot**
This script runs in the background, collecting data and sending alerts.
```bash
python main.py
