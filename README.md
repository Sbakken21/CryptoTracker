# CryptoTracker
This is a python script that utilizes the coinmarketcap API in order to monitor the prices of numerous cryptocurrencies at once. If the user selected values are reached the script will send an email notification to alert the user that it is either time to buy or sell the selected currencies.
## Getting started
### Prerequisites
This script uses python 3.6.

Use the included requirements.txt:
```
pip install -r requirements.txt
```
### User Setup
 In `config.example.cfg` change the values to indicate the coins you wish to monitor, and set the prices at which you would like the coins to reach in order to sell and buy them. 
 
 *Note: do NOT use commas for inputting numerical values, only to separate items.  
 ex: sell_price = 1000 NOT sell_price = 1,000* 
 
 * set `from_address` to the email you are using to send this script from
 * set `password` to the password for the email used for `from_address`
 * set `to_address` to the email that you wish the notifications to be sent (this can be the same as the `from_address`)
  
Once all the values are entered, save `config.example.cfg` as `config.cfg`.
  
 #### Quick Example of config.cfg
 ```
[watch]

tickers_list = Bitcoin, Ark, Ripple
sell_price = 20000.00, 8.00, 5.00
buy_price = 15000.00, 2.00, 2.00

[email]

from_address = bob@gmail.com
password = ***********
to_address = joe@gmail.com
```
 

 
 