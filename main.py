from coinmarketcap import Market
import configparser
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_ticker_info(coinmarketcap, tickers_list, sell_price, buy_price):
    """Return coin information"""

    # Obtains all info from each ticker on the declared tickers list
    for ticker, sell_value, buy_value in zip(tickers_list, sell_price, buy_price):
        info = coinmarketcap.ticker(currency=ticker)[0]
        id = info.get('id')
        price_usd = info.get('price_usd')
        print('ID: %s\n' %id + 'Price (USD): %s' %price_usd)
        compare_info(price_usd, sell_value, buy_value, id)
        print('=====' * 10)

def compare_info(price_usd, selling, buying, id):
    """Compares the coin's current price and target price """

    # This is the target price for cryptocurrencies to be bought and sold
    if float(selling) <= float(price_usd):
        alert = f'This cryptocurrency is above the price indicated to sell: ${selling}'
        print(alert)
        notification(id, price_usd, alert)
    elif float(buying) >= float(price_usd):
        alert = f'This cryptocurrency is below the price indicated to buy ${buying}'
        print(alert)
        notification(id, price_usd, alert)
    else:
        print('not at target price yet')

def notification(id, price, alert):
    """Send email notification that target price has been reached"""

    # load config
    config = get_config()

    # Create Email notification
    from_address = config.get("email", "from_address")
    to_address = config.get("email", "to_address")
    password = config.get("email", "password")
    message = MIMEMultipart()
    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = str(id).upper()

    body = f'ID: {id}\nPrice (USD): ${price}\n{alert}'
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(
        from_address,
        password
    )
    text = message.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()
    print("Message has been sent")


def get_config():
    """Read from config file"""
    config = configparser.ConfigParser()
    config.read('config.cfg')
    return config

def main():
    # Load config
    config = get_config()

    # List of bitcoins to watch
    tickers_list = config.get("watch", "tickers_list").replace(", ", ",").replace(" ", "-").split(",")
    sell_price = config.get("watch", "sell_price").replace(", ", ",").split(",")
    buy_price = config.get("watch", "buy_price").replace(", ", ",").split(",")

    # Get market info using coinmarketcap API
    coinmarketcap = Market()

    get_ticker_info(coinmarketcap, tickers_list, sell_price, buy_price)

if __name__=="__main__":
    while True:
        try:
            main()
            time.sleep(600) # Interval in seconds that script updates
        except KeyboardInterrupt:
            break