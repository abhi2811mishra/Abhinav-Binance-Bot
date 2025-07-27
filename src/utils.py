# src/utils.py
import logging
import os

def setup_logging():
    log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'bot.log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def validate_input(symbol, quantity, price=None):
    """
    Validates common inputs for trading orders.
    """
    if not isinstance(symbol, str) or not symbol.strip():
        return False, "Symbol cannot be empty."
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        return False, "Quantity must be a positive number."
    if price is not None and (not isinstance(price, (int, float)) or price <= 0):
        return False, "Price must be a positive number if provided."
    return True, "Validation successful."