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

flow()

print '---'

print ('NANO | image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAABRUExURUxpcVSJykmQ4kaS3lKLzWyUxESF2V+W0FKV7lGJyU6O4EmR3k6P3lSU6EyP3kmT30qP4keU3kCT5kWS4UiR4VKL4EOT40OQ6ESS5UWQ5kiQ4v2G/RwAAAAKdFJOUwDr///+EP4F/tfCPIxYAAAAQ0lEQVQY02NgoBngkoAy+ATBFIukFITPzs0LJDlEGBkYmJiAXGFxsDAHMztEgJNZFMQVgGpnFWMD0/w8UAEhLto5GgDaMgGRTwkAAgAAAABJRU5ErkJggg==')

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
print ('NANO daily-trading | image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAABRUExURUxpcVSJykmQ4kaS3lKLzWyUxESF2V+W0FKV7lGJyU6O4EmR3k6P3lSU6EyP3kmT30qP4keU3kCT5kWS4UiR4VKL4EOT40OQ6ESS5UWQ5kiQ4v2G/RwAAAAKdFJOUwDr///+EP4F/tfCPIxYAAAAQ0lEQVQY02NgoBngkoAy+ATBFIukFITPzs0LJDlEGBkYmJiAXGFxsDAHMztEgJNZFMQVgGpnFWMD0/w8UAEhLto5GgDaMgGRTwkAAgAAAABJRU5ErkJggg==')

spread24hBTC = float(result_binance['highPrice']) - float(result_binance['lowPrice'])
spread24hUSD = spread24hBTC * float(result_cmc_btc[0]['price_usd'])
# gain if we swingtrade with 50k NANO
possible_gain = spread24hBTC * 50000

print ('spread:   %.8f (%s) | color=#000000'% (spread24hBTC, locale.currency(spread24hUSD, grouping=True)))
print ('possible gain:   %.2f BTC (%s) | color=#000000'% (possible_gain, locale.currency(possible_gain * float(result_cmc_btc[0]['price_usd']), grouping=True)))

print '---'

print ('Bitcoin | image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAC3klEQVR4nGWTTWicVRSGn3Pv/b75sWkSaTQmNSWgiHZjS6DGFCd2pRTcaDcRFy5MaNq6UXCnuNdFF7ZaEUFUsCgIWkTB2lmISN0IdiH+1AaZSir9SSeZmfvde46LQVRcHDiL8/DCeXkEwAwRwQDih48ueO+XVa2l2aYAxEuncHKuyvnN8onPvv43I38vF99u1XeONF4RZMUXEiwqKSuYEooSKYSccjKzU+Fm/zl5ut03Q8ROH/JMrBfVleJMsa08MLg+MEwVcOKCEOpY76ohTvE1VxsrperGs8VEdZArt1UC0H938URtvHZ4cLUfRSgJdYg3kcm9uJmHscvnIfXJnW/B12NtvCzjjXiitvTVEYnv798H7htTU8N5qi7uzocIe1dBPDa4jtRGSd8dR3/7EpoTJpZVnDjQeafZjhXBRHMCrSA00LU2utZGxmYBgcat+PuXkTvmIHZFVRkydsyhqaWxAlOHZTDFqk2oj0PqET8+RPzgEdyO3RQLL4JGsOw0VqDVYkDzZKUgMCxSDClHcJNz4MshlPqQ+uj696AJMZUqKWY26UyTDJMzAGytI+UIsn2a/Ovn2GADv3sJLJMvvAdmw1sdjhPLfxSimKlRbeKm5/F7VkAc+Yd3qD49SvzkKQgN/H1LUG1hqlaI4tDLAdNzLvAkfVPywMv0PG7nfkAID7yAv+sx3O17QBx27WcwBc3qSvPW17bEt+7dh9mwRgnOuh3x9zxOmHsWi11kbBa79gv25wXS+ePDHziXxeEq5UEB2Hr97tcao361dyNHUq/0My0ITfxMi/zjR+SLXyC17RCaGBIbY6HsbeSTzZWfVsVO49ncVcQYzpTb5EBvw4zUV0ydNHcIqYcZBiimrjHqJHbtbFmmg9xyqfpHppd21aem7VVnLIfgQ06QqgrEEbzgCyElS8Abv3d4fvblS0OZ/qfzyZkF7/WZlFnUzBQY3ktHHG1Td6o8vPYfnf8CyHGVDNs26GQAAAAASUVORK5CYII=')


print ('price:  $%.2f | color=#000000'% float(result_cmc_btc[0]['price_usd']))
print ('change 1h: %.1f%% | color=#000000'% float(result_cmc_btc[0]['percent_change_1h']))
print ('change 24h: %.1f%% | color=#000000'% float(result_cmc_btc[0]['percent_change_24h']))
print ('change 7d: %.1f%% | color=#000000'% float(result_cmc_btc[0]['percent_change_7d']))

print '---'

print 'Show CoinMarketCap | color=#123def href=https://coinmarketcap.com/currencies/nano/'
print 'Show KuCoin | color=purple href=https://www.kucoin.com/#/trade.pro/XRB-BTC'
print 'Show Binance | color=#ff9933 href=https://www.binance.com/tradeDetail.html?symbol=NANO_BTC'