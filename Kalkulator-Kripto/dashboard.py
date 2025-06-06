import requests
import time
import os

def get_indodax_data(pair):
    try:
        url = f"https://indodax.com/api/ticker/{pair}"
        response = requests.get(url)
        data = response.json()['ticker']
        return {
            'last': float(data['last']),
            'buy': float(data['buy']),
            'sell': float(data['sell']),
            'high': float(data['high']),
            'low': float(data['low']),
            'volume': float(data.get('vol_' + pair[:3], 0))
        }
    except Exception as e:
        return f"Gagal ambil data Indodax {pair.upper()}: {e}"

def get_binance_data(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        response = requests.get(url)
        data = response.json()
        return {
            'last': float(data['lastPrice']),
            'buy': float(data['bidPrice']),
            'sell': float(data['askPrice']),
            'high': float(data['highPrice']),
            'low': float(data['lowPrice']),
            'volume': float(data['volume']),
            'priceChangePercent': float(data['priceChangePercent'])
        }
    except Exception as e:
        return f"Gagal ambil data Binance {symbol}: {e}"

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    print(" DASHBOARD BTC, ETH, SOL (Indodax + Binance)")
    print("=" * 60)

    # Indodax
    for asset, pair in {
        'BTC': 'btcidr',
        'ETH': 'ethidr',
        'SOL': 'solidr'
    }.items():
        data = get_indodax_data(pair)
        print(f"\n[Indodax] {asset}/IDR")
        if isinstance(data, str):
            print(f"  {data}")
        else:
            print(f"  - Harga Terakhir : Rp{data['last']:,}")
            print(f"  - Beli Tertinggi : Rp{data['buy']:,}")
            print(f"  - Jual Terendah  : Rp{data['sell']:,}")
            print(f"  - Tertinggi 24H  : Rp{data['high']:,}")
            print(f"  - Terendah 24H   : Rp{data['low']:,}")
            if data['volume'] > 0:
                print(f"  - Volume         : {data['volume']:.2f} {asset}")
            else:
                print(f"  - Volume         : Tidak tersedia")

    # Binance
    for asset, symbol in {
        'BTC': 'BTCUSDT',
        'ETH': 'ETHUSDT',
        'SOL': 'SOLUSDT'
    }.items():
        data = get_binance_data(symbol)
        print(f"\n[Binance] {asset}/USDT")
        if isinstance(data, str):
            print(f"  {data}")
        else:
            print(f"  - Harga Terakhir : ${data['last']:,}")
            print(f"  - Beli Tertinggi : ${data['buy']:,}")
            print(f"  - Jual Terendah  : ${data['sell']:,}")
            print(f"  - Tertinggi 24H  : ${data['high']:,}")
            print(f"  - Terendah 24H   : ${data['low']:,}")
            print(f"  - Volume         : {data['volume']:.2f} {asset}")
            print(f"  - Perubahan 24H  : {data['priceChangePercent']:.3f}%")

    time.sleep(20)