# Crypto Calculator & Dashboard (BTC, ETH, SOL)
Kumpulan alat bantu Python untuk menghitung keuntungan bersih dari transaksi kripto dan memantau harga real-time.

## Fitur Utama
* Perhitungan fee maker dan taker
* Hitung cuan bersih dari dua transaksi (beli → jual / jual → beli)
* Mode transaksi bertahap : cocok untuk strategi DCA (Dollar Cost Averaging)
* Dashboard CLI real-time (Indodax : IDR, Binance : USDT)

## Isi Proyek
* calculator-BTC.py –> Kalkulator GUI transaksi BTC
* calculator-ETH.py –> Kalkulator GUI transaksi ETH
* calculator-SOL.py –> Kalkulator GUI transaksi SOL
* multi-transaction.py –> Kalkulator transaksi bertahap (multi-entry)
* dashboard.py –> CLI dashboard harga real-time dari Indodax & Binance

## Cara Menjalankan Skrip
```bash
python calculator-BTC.py          # atau ETH / SOL
python multi-transaction.py
python dashboard.py
```

## Contoh Perhitungan GUI
* Masukkan Nominal (Rp) dan Harga (Rp)
* Pilih Mode: Beli → Jual atau Jual → Beli
* Pilih Tipe Order: Maker / Taker
* Klik Hitung untuk melihat:
  * Total Koin
  * Fee
  * Keuntungan bersih

## Kebutuhan
- Python 3.x
- Modul requests (hanya untuk dashboard.py)
  ```bash
  pip install requests
  ```

