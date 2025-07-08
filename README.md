# udbhav-binance-bot
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<div class="container">
  <h1 class="mb-4">💹 Binance Futures Trading Bot (Testnet)</h1>
  <h1>Resume: <a href="https://drive.google.com/file/d/1crAIpjemM6ipPbqYd4xYrGyBhlW2PLjg/view?usp=sharing" target="_blank"><u>Click Here</u></a></h1>
  <p>
    A command-line and web-based trading bot that places <strong>Market</strong>, <strong>Limit</strong>, and
    <strong>Stop-Limit</strong> orders on the <strong>Binance USDT-M Futures Testnet</strong>.
    Built with Python, Flask, Bootstrap, and the official Binance API.
  </p>

  <div class="alert alert-success">
    ✅ Created as part of an internship task to demonstrate API integration, backend logic, and optional UI skills.
  </div>

  <h2>🚀 Features</h2>
  <ul>
    <li>🔄 Place <strong>Buy/Sell</strong> orders</li>
    <li>📈 Supports:
      <ul>
        <li>Market Orders</li>
        <li>Limit Orders</li>
        <li>Stop-Limit Orders</li>
      </ul>
    </li>
    <li>🧾 Command-Line Interface (CLI)</li>
    <li>🌐 Web UI (Flask + Bootstrap)</li>
    <li>✅ Input Validation & Error Handling</li>
    <li>🪵 Structured Logging (<code>bot.log</code>)</li>
    <li>🧪 Uses Binance Testnet (safe for testing)</li>
  </ul>

  <h2>🏗️ Project Structure</h2>
  <pre><code>
binance-bot/
│
├── src/
    |── bot.log             # API actions and error logs
│   ├── bot.py              # Core Binance order logic
│   ├── views/
│   │   └── trading.py      # Flask class-based view
│   ├── templates/
│   │   └── index.html      # Frontend order form
│   └── app.py              # Flask app runner
│               
├── .env                    # API keys and secret key (not uploaded)
├── README.md               # You're reading it
└── requirements.txt        # Python dependencies
  </code></pre>

  <h2>⚙️ Setup Instructions</h2>

  <h4>1. 🔑 Get Binance Testnet API Keys</h4>
  <p>
    Visit: <a href="https://testnet.binancefuture.com" target="_blank">https://testnet.binancefuture.com</a><br>
    Login and generate an API Key and Secret.
  </p>

  <h4>2. 🧪 Clone This Repo</h4>
  <pre><code>git clone https://github.com/your-username/binance-bot.git
cd binance-bot</code></pre>

  <h4>3. 📦 Install Dependencies</h4>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h4>4. 🔐 Create .env File</h4>
  <pre><code>
API_Key=your_testnet_api_key
Secret_Key=your_testnet_secret_key
flask_key=your_secret_flask_key
  </code></pre>
  <p><strong>Tip:</strong> Generate Flask key using:</p>
  <pre><code>python -c "import secrets; print(secrets.token_hex(32))"</code></pre>

  <h2>🖥️ Usage</h2>

  <h4>🔧 CLI Mode</h4>
  <pre><code>
# Market Order
python src/bot.py BTCUSDT BUY MARKET 0.01

# Limit Order
python src/bot.py BTCUSDT SELL LIMIT 0.01 31000

# Stop-Limit Order
python src/bot.py BTCUSDT BUY STOP_LIMIT 0.01 31000 30500
  </code></pre>

  <h5>CLI Args:</h5>
  <pre><code>symbol side order_type quantity [price] [stop_price]</code></pre>

  <h4>🌐 Web UI Mode</h4>
  <pre><code>python src/app.py</code></pre>
  <p>Visit <strong>http://localhost:8000</strong> in your browser</p>

  <h2>📁 Logging</h2>
  <p>All API actions and errors are logged to <code>bot.log</code> with timestamps and tracebacks.</p>

  <h2>🧪 Screenshots</h2>
  <p>Add screenshots of:</p>
  <ul>
    <li>CLI commands and output</li>
    <li>Web UI form</li>
    <li>Success and error alerts</li>
  </ul>

  <h2>📚 Resources</h2>
  <ul>
    <li><a href="https://binance-docs.github.io/apidocs/futures/en/" target="_blank">Binance Futures API Docs</a></li>
    <li><a href="https://testnet.binancefuture.com" target="_blank">Binance Futures Testnet</a></li>
    <li><a href="https://getbootstrap.com/" target="_blank">Bootstrap Docs</a></li>
  </ul>

  <h2>📌 Notes</h2>
  <ul>
    <li>⚠️ Use only with Binance Testnet — <strong>never real funds</strong></li>
    <li>❌ Never push your <code>.env</code> or API keys to GitHub</li>
    <li>⭐ Bonus features like TWAP, Grid, and OCO can be added later</li>
  </ul>

  <h2>🙋‍♂️ Author</h2>
  <p>
    <strong>Udbhav Saxena</strong><br>
    Backend Developer Intern Candidate<br>
    Email: <a href="mailto:udbhavsaxena.dev@gmail.com">udbhavsaxena.dev@gmail.com</a><br>
    GitHub: <a href="https://github.com/your-username" target="_blank">github.com/your-username</a>
  </p>

  <h2>📃 License</h2>
  <p>This project is for educational/internship use only. Not intended for financial trading or production deployment.</p>

</div>

</body>
</html>
