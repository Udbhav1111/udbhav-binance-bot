import argparse
import os
import logging
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

class BinanceBot:
    def __init__(self):
        self.client = Client(
            api_key=os.getenv('API_Key'),
            api_secret=os.getenv('Secret_Key'),
            testnet=True
        )
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com'

    def create_order_future(self, symbol, quantity, price=None, order_type='MARKET', site=True, stop_price=None):
        """
        Places a futures order on Binance Testnet (USDT-M Futures).

        Supports MARKET, LIMIT, and STOP_LIMIT orders for both BUY and SELL sides.
        Automatically handles timeInForce for applicable order types, and logs 
        the outcome of the operation.

        Args:
            symbol (str): The trading pair symbol (e.g., 'BTCUSDT').
            quantity (float): The quantity to trade.
            price (float, optional): The limit price. Required for LIMIT and STOP_LIMIT orders.
            order_type (str): The type of order to place. One of 'MARKET', 'LIMIT', 'STOP_LIMIT'. Default is 'MARKET'.
            site (bool): True for 'BUY', False for 'SELL'. Default is True.
            stop_price (float, optional): The stop trigger price. Required for STOP_LIMIT orders.

        Returns:
            dict or None: The API response dictionary if order is successfully placed, else None.

        Raises:
            ValueError: If required parameters (e.g., price or stop_price) are missing for the selected order type.

        Logs:
            - Successful order placements to 'bot.log'
            - Any exceptions encountered during API interaction
        """

        side = 'BUY' if site else 'SELL'

        try:
            order_data = {
                'symbol': symbol,
                'side': side,
                'type': order_type.upper(),
                'quantity': quantity
            }

            if order_type.upper() in ['LIMIT', 'STOP_LIMIT']:
                order_data['timeInForce'] = 'GTC'

            if order_type.upper() == 'LIMIT':
                if price is None:
                    raise ValueError("! Price must be provided for LIMIT orders.")
                order_data['price'] = str(price)

            elif order_type.upper() == 'STOP_LIMIT':
                if not stop_price or not price:
                    raise ValueError("! Both stop_price and price must be provided for STOP_LIMIT orders.")
                order_data.update({
                    'stopPrice': str(stop_price),
                    'price': str(price)
                })

            order = self.client.futures_create_order(**order_data)
            logging.info(f"{order_type} order placed: {order}")
            print(f" '++' {order_type} order placed successfully!")
            print(order)
            return order

        except Exception as e:
            logging.error(f" 'X' Error placing order: {e}")
            print(f" 'X' Failed to place order: {e}")
            return None


def parse_arguments():
    parser = argparse.ArgumentParser(description='Binance Futures Order Bot CLI')
    parser.add_argument('symbol', type=str, help='Trading pair symbol (e.g., BTCUSDT)')
    parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('order_type', type=str, choices=['MARKET', 'LIMIT', 'STOP_LIMIT'], help='Order type')
    parser.add_argument('quantity', type=float, help='Quantity to trade')
    parser.add_argument('price', type=float, nargs='?', help='Price for LIMIT or STOP_LIMIT orders')
    parser.add_argument('stop_price', type=float, nargs='?', help='Stop price (only for STOP_LIMIT)')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    bot = BinanceBot()

    is_buy = args.side.upper() == 'BUY'

    bot.create_order_future(
        symbol=args.symbol,
        quantity=args.quantity,
        price=args.price,
        order_type=args.order_type,
        site=is_buy,
        stop_price=args.stop_price
    )
