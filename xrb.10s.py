#!/usr/bin/env python
# coding=utf-8
#
# <bitbar.title>NANO coin Ticker</bitbar.title>
# <bitbar.version>v1.1</bitbar.version>
# <bitbar.author>dizda</bitbar.author>
# <bitbar.author.github>dizda</bitbar.author.github>
# <bitbar.desc>Displays current NANO stats from Binance and CMC</bitbar.desc>
#
# by dizda

import urllib2
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

req_binance = urllib2.Request('https://api.binance.com/api/v1/ticker/24hr?symbol=NANOBTC', headers={ 'User-Agent': 'Mozilla/5.0' })
req_cmc_nano = urllib2.Request('https://api.coinmarketcap.com/v1/ticker/nano/?convert=BTC', headers={ 'User-Agent': 'Mozilla/5.0' })
req_cmc_btc = urllib2.Request('https://api.coinmarketcap.com/v1/ticker/bitcoin/', headers={ 'User-Agent': 'Mozilla/5.0' })
binance = urllib2.urlopen(req_binance).read()
cmc_nano = urllib2.urlopen(req_cmc_nano).read()
cmc_btc = urllib2.urlopen(req_cmc_btc).read()

import json
result_binance = json.loads(binance)
result_cmc_nano = json.loads(cmc_nano)
result_cmc_btc = json.loads(cmc_btc)

def flow():
    if result_cmc_nano[0]['percent_change_1h'] > '0':
        print (' %.8f ($%.2f) | image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QAyQACAALwzISXAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACkSBTjB+AAAALNJREFUOMvVk70NAjEMhb87WYiGBZAQU7ABNSVSWpZgEEagsJDoKBELUCEKFuBuCKTw0xyQC0lICe5i+/k9/wT+3opUUJQhcAUqa8I5ZQT4tANwioGTCkQZA9vmOQE2oUJFhL0DXBz33RpKUfCLfLTQJMx9IlEWuQr6QB3prGtNS1lwiMvEYo7ekNsKRBkB+y+rH1hDFVOwy7ids+gbVzrsM6CXeYDTF85xroB1ZoHb73ymB5RhJkpZTihGAAAAAElFTkSuQmCC color=#000000'% (float(result_binance['lastPrice']), float(result_cmc_nano[0]['price_usd'])) )
    else:
        print (' %.8f ($%.2f) | image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QABACnAADQ9FZaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACQ1FZwK3gAAAMRJREFUOMvNkjEKAjEQRZ+jKNjYKh5AbzCdjVcQj+BFPIKlp7EMeAJrUbASQVCEr80uG9cNbqe/Cgn/5WUI/DqNfBHM+kCzbs+lPUAr2pwBq5qABbB+M8gszkDvS/kOdAG5VBgEM4ApsP0CGLukjxlEoA0wSZR3Lo0qhxhZDIBDAmDA0wsBLD51CZeOwLKivHbprZx6AkAHuEXbD5fawYwywMqAzOKeDTTPvKqcTGZBMLsGs0utn5gADYEHcKp9e9ni//MCDtNCE3qjsIwAAAAASUVORK5CYII= color=#000000'% (float(result_binance['lastPrice']), float(result_cmc_nano[0]['price_usd'])) )

#print (' %.8f | color=#000000'% float(result_binance['lastPrice']))
flow()

print '---'

print ('NANO')

print ('buy: %.8f | color=green'% float(result_binance['bidPrice']))
print ('sell: %.8f | color=red'% float(result_binance['askPrice']))

print ('vol: %.0f BTC (%s) | color=#000000'% (float(result_cmc_nano[0]['24h_volume_btc']), locale.currency(float(result_cmc_nano[0]['24h_volume_usd']), grouping=True)))
print ('change-24h: %.1f%% | color=#000000'% float(result_cmc_nano[0]['percent_change_24h']))

high_usd = float(result_cmc_btc[0]['price_usd']) * float(result_binance['highPrice'])
low_usd = float(result_cmc_btc[0]['price_usd']) * float(result_binance['lowPrice'])

print ('high:   %.8f (%s) | color=#000000'% (float(result_binance['highPrice']), locale.currency(high_usd, grouping=True)))
print ('low:    %.8f (%s) | color=#000000'% (float(result_binance['lowPrice']), locale.currency(low_usd, grouping=True)))


print ('price:  $%.2f | color=#000000'% float(result_cmc_nano[0]['price_usd']))
print ('rank:   #%.0f | color=#000000'% float(result_cmc_nano[0]['rank']))

print '---'
print ('NANO daily-trading')

spread24hBTC = float(result_binance['highPrice']) - float(result_binance['lowPrice'])
spread24hUSD = spread24hBTC * float(result_cmc_btc[0]['price_usd'])
# gain if we swingtrade with 50k NANO
possible_gain = spread24hBTC * 50000

print ('spread:   %.8f (%s) | color=#000000'% (spread24hBTC, locale.currency(spread24hUSD, grouping=True)))
print ('possible gain:   %.2f BTC (%s) | color=#000000'% (possible_gain, locale.currency(possible_gain * float(result_cmc_btc[0]['price_usd']), grouping=True)))

print '---'

print ('Bitcoin')

print ('price:  $%.2f | color=#000000'% float(result_cmc_btc[0]['price_usd']))
print ('change 1h: %.1f%% | color=#000000'% float(result_cmc_btc[0]['percent_change_1h']))
print ('change 24h: %.1f%% | color=#000000'% float(result_cmc_btc[0]['percent_change_24h']))
print ('change 7d: %.1f%% | color=#000000'% float(result_cmc_btc[0]['percent_change_7d']))

print '---'

print 'Show CoinMarketCap | color=#123def href=https://coinmarketcap.com/currencies/nano/'
print 'Show KuCoin | color=purple href=https://www.kucoin.com/#/trade.pro/XRB-BTC'
print 'Show Binance | color=#ff9933 href=https://www.binance.com/tradeDetail.html?symbol=NANO_BTC'