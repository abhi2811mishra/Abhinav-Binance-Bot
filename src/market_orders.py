# src/market_orders.py
import argparse
# import os # Removed: API keys are now handled in basic_bot.py
from src.basic_bot import BasicBot
from src.utils import setup_logging

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Place a Market Order on Binance Futures Testnet.")
    parser.add_argument('symbol', type=str, help='Trading pair (e.g., BTCUSDT)')
    parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side (BUY or SELL)')
    parser.add_argument('quantity', type=float, help='Quantity to trade')

    args = parser.parse_args()

    # Removed API key retrieval and validation as keys are now hardcoded in BasicBot
    # api_key = os.getenv("BINANCE_API_KEY")
    # api_secret = os.getenv("BINANCE_API_SECRET")
    #
    # if not api_key or not api_secret:
    #     logger.error("BINANCE_API_KEY and BINANCE_API_SECRET environment variables must be set.")
    #     print("Error: Please set BINANCE_API_KEY and BINANCE_API_SECRET environment variables.")
    #     return

    # Instantiate BasicBot without api_key and api_secret arguments
    bot = BasicBot(testnet=True)
    result = bot.place_market_order(args.symbol, args.quantity, args.side)

    if result["status"] == "success":
        print(f"Market order placed successfully! Order ID: {result['order']['orderId']}")
        print(f"Details: {result['order']}")
    else:
        print(f"Failed to place market order: {result['message']}")

if __name__ == "__main__":
    main()