from flask import Flask,Blueprint,render_template,flash,redirect,request
from flask.views import MethodView
from src.bot import BinanceBot


trading_bp = Blueprint("trading",__name__,template_folder="../templates")
class TradingView(MethodView):
    """
        TradingView is a Flask class-based view that handles displaying and processing
        Binance Futures orders through a web form interface.

        This view supports both GET and POST methods:

        Methods:
        --------
        - GET:
            Renders the order form page using a Bootstrap-styled HTML template.
            The form allows users to input symbol, order side, type, quantity, price, and stop price.

        - POST:
            Processes the submitted form data to place a Binance Futures order.
            Supports MARKET, LIMIT, and STOP_LIMIT order types for BUY or SELL sides.
            Validates input data, handles exceptions, and provides feedback using Flask flash messages.

        Dependencies:
        -------------
        - Requires a properly configured BinanceBot instance with testnet credentials.
        - Uses `request.form` to retrieve form data.
        - Uses `flash()` for success and error messages.
        - Redirects back to the main form page after submission.

        Expected Form Fields:
        ---------------------
        - symbol (str): Trading pair symbol (e.g., BTCUSDT)
        - side (str): BUY or SELL
        - order_type (str): MARKET, LIMIT, or STOP_LIMIT
        - quantity (float): Quantity to trade
        - price (float, optional): Required for LIMIT and STOP_LIMIT
        - stop_price (float, optional): Required for STOP_LIMIT

        Example Usage:
        --------------
        Register the view in your Flask app:
            app.add_url_rule('/', view_func=TradingView.as_view('trading'))

        Environment:
        ------------
        Requires SECRET_KEY and Binance API credentials in `.env`.

        Templates:
        ----------
        - `templates/index.html`: The form for submitting orders.
    """
    def __init__(self):
        self.bot = BinanceBot()

    def get(self):
        return render_template("index.html")
    
    def post(self):
        try:
            symbol = request.form['symbol']
            side = request.form['side']
            order_type = request.form['order_type']
            quantity = float(request.form['quantity'])
            price = request.form.get('price')
            stop_price = request.form.get('stop_price')

            price = float(price) if price else None
            stop_price = float(stop_price) if stop_price else None
            is_buy = side.upper() == 'BUY'

            order = self.bot.create_order_future(
                symbol=symbol,
                quantity=quantity,
                price=price,
                order_type=order_type,
                site=is_buy,
                stop_price=stop_price
            )

            if order:
                flash(f'{order_type} order placed successfully!', 'success')
            else:
                flash(f'Failed to place {order_type} order.', 'danger')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')

        return redirect('/')
