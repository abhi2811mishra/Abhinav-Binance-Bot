# src/basic_bot.py

from binance.um_futures import UMFutures  # ✅ Correct class name from official binance-connector
from binance.error import ClientError
import logging
from src.utils import setup_logging, validate_input

logger = setup_logging()

class BasicBot:
    def __init__(self, testnet=True):
        api_key = "689120f8552fa49c29a3257683bfd4158bf4196876c75dd41bf40def86be7b42"
        api_secret = "d9689841e141f422624d29afb1c758ef2586a50f147b51b6f07b248538980e6b"

        base_url = "https://testnet.binancefuture.com" if testnet else "https://fapi.binance.com"

        self.client = UMFutures(key=api_key, secret=api_secret, base_url=base_url)
        logger.info(f"Initialized Binance USDT-M Futures client for {'testnet' if testnet else 'live'}.")

    def _log_and_return_error(self, message, e):
        logger.error(f"{message}: {e}")
        return {"status": "error", "message": f"{message}: {e}"}

    def place_market_order(self, symbol, quantity, side):
        is_valid, message = validate_input(symbol, quantity)
        if not is_valid:
            logger.warning(f"Market order validation failed for {symbol}: {message}")
            return {"status": "error", "message": f"Validation Error: {message}"}

        try:
            order = self.client.new_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logger.info(f"Market {side} order placed for {quantity} {symbol}. Order ID: {order['orderId']}")
            return {"status": "success", "order": order}
        except ClientError as e:
            return self._log_and_return_error("Binance Client error placing market order", e)
        except Exception as e:
            return self._log_and_return_error("Unexpected error placing market order", e)

    def place_limit_order(self, symbol, quantity, price, side):
        is_valid, message = validate_input(symbol, quantity, price)
        if not is_valid:
            logger.warning(f"Limit order validation failed for {symbol}: {message}")
            return {"status": "error", "message": f"Validation Error: {message}"}

        try:
            order = self.client.new_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            logger.info(f"Limit {side} order placed for {quantity} {symbol} at {price}. Order ID: {order['orderId']}")
            return {"status": "success", "order": order}
        except ClientError as e:
            return self._log_and_return_error("Binance Client error placing limit order", e)
        except Exception as e:
            return self._log_and_return_error("Unexpected error placing limit order", e)

    def get_account_balance(self):
        try:
            balances = self.client.balance()
            usdt_balance = [b for b in balances if b['asset'] == 'USDT']
            logger.info(f"USDT Balance: {usdt_balance}")
            return {"status": "success", "balance": usdt_balance}
        except ClientError as e:
            return self._log_and_return_error("Binance Client error fetching balance", e)
        except Exception as e:
            return self._log_and_return_error("Unexpected error fetching balance", e)
