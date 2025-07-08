from .tradingview import trading_bp,TradingView

def register_views(app):
    trading_view = TradingView.as_view('trading_view')
    app.add_url_rule('/', view_func=trading_view, methods=['GET', 'POST'])
    app.register_blueprint(trading_bp)