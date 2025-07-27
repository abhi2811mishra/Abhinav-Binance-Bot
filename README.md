📈 Binance Futures Order Bot (CLI-Based)
A command-line trading bot for Binance USDT-M Futures Testnet, supporting Market and Limit orders with robust input validation, logging, and error handling. This project is designed for the Junior Python Developer application task.

📚 Table of Contents
🚀 Features

🧰 Prerequisites

⚙️ Installation

🔐 API Key Setup

💡 Usage

Market Orders

Limit Orders

🗂️ Code Structure

📝 Logging

❗ Error Handling

🔮 Future Enhancements

📌 Submission Notes

🚀 Features
✅ Order Types

Place Market Orders (Buy/Sell)

Place Limit Orders (Buy/Sell)

✅ Input Validation

Validates trading pair symbol, quantity, and price before submission.

✅ Structured Logging

All actions and errors are logged in bot.log with timestamps and severity levels.

✅ Error Handling

Handles BinanceAPIException, BinanceRequestException, and general exceptions with informative console + log outputs.

✅ Modular Codebase

Organized for readability, reusability, and future extensibility.

✅ Testnet Support

Fully integrated with Binance Futures Testnet to avoid real fund risk.

🧰 Prerequisites
Ensure the following are installed:

 Python 3.8+ (tested with 3.13.1)

 pip (Python package manager)

⚙️ Installation
bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/your-username/Abhinav_binance_bot.git
cd Abhinav_binance_bot

# 2. Create virtual environment (recommended)
python -m venv venv

# 3. Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install python-binance
🔐 API Key Setup
⚠️ For educational use only. Never expose real API keys in production code.

Visit the Binance Futures Testnet:
https://testnet.binancefuture.com

Generate your Testnet API Key & Secret under API Management.

Ensure the following are enabled:

✅ Enable Futures

❌ Do NOT enable Withdrawals

In src/basic_bot.py, update your API credentials:

python
Copy
Edit
class BasicBot:
    def __init__(self, testnet=True):
        api_key = "YOUR_TESTNET_API_KEY"
        api_secret = "YOUR_TESTNET_SECRET_KEY"
        ...
💡 Usage
All commands must be run from the project root with the virtual environment activated.

📘 Market Orders
Syntax:
bash
Copy
Edit
python -m src.market_orders <SYMBOL> <SIDE> <QUANTITY>
Parameter	Description
<SYMBOL>	Trading pair (e.g., BTCUSDT)
<SIDE>	Order side: BUY or SELL
<QUANTITY>	Quantity of base asset (e.g., 0.001)

Examples:
powershell
Copy
Edit
python -m src.market_orders BTCUSDT BUY 0.001
python -m src.market_orders BTCUSDT SELL 0.001
📗 Limit Orders
Syntax:
bash
Copy
Edit
python -m src.limit_orders <SYMBOL> <SIDE> <QUANTITY> <PRICE>
Parameter	Description
<SYMBOL>	Trading pair (e.g., BTCUSDT)
<SIDE>	Order side: BUY or SELL
<QUANTITY>	Quantity of base asset
<PRICE>	Desired limit price

Examples:
powershell
Copy
Edit
python -m src.limit_orders BTCUSDT BUY 0.001 60000
python -m src.limit_orders BTCUSDT SELL 0.001 70000
✅ Ensure the quantity and price meet Binance Testnet's precision and minimum limits.

🗂️ Code Structure
bash
Copy
Edit
Abhinav_binance_bot/
│
├── src/
│   ├── basic_bot.py        # Binance client & core methods
│   ├── market_orders.py    # CLI entry for market orders
│   ├── limit_orders.py     # CLI entry for limit orders
│   ├── utils.py            # Logging & validation utilities
│   └── __init__.py         # Marks src as a Python package
│
├── venv/                   # Python virtual environment
├── bot.log                 # Auto-generated log file
├── README.md               # This documentation
└── report.pdf              # Detailed analysis (in progress)
📝 Logging
Logging is handled by Python’s logging module and stored in bot.log.

Each log includes:

Timestamp

Log Level (INFO, WARNING, ERROR)

Event Description

This allows easy debugging, backtracking failed orders, and monitoring bot activity.

❗ Error Handling
The bot implements robust try-except blocks across API interaction points:

Exception Type	Trigger
BinanceAPIException	Invalid parameters, permissions, rate limits
BinanceRequestException	Network issues, timeouts
Exception	Fallback for unexpected errors

All errors are logged and printed to the terminal.

🔮 Future Enhancements (Bonus Features)
Optional upgrades that showcase advanced functionality:

✅ Advanced Order Types
Stop-Limit Orders

OCO (One-Cancels-the-Other) Orders

TWAP Strategy – Break large orders into timed slices

Grid Orders – Automate market making with spaced orders

✅ UI Interface
CLI Enhancements (e.g., argparse interactivity)

Optional Tkinter or Flask based lightweight GUI

📌 Submission Notes
All API calls are directed to Binance Futures Testnet.

Ensure to update the API keys before testing.

For demonstration, screenshots, and logs, refer to report.pdf (to be added).

