import tkinter as tk
from tkinter import ttk

FEE_MAKER = 0.2322 / 100
FEE_TAKER = 0.3322 / 100

def rupiah(val):
    return f"Rp{val:,.0f}".replace(",", ".")

def hitung_fee(nominal, is_maker):
    fee_percent = FEE_MAKER if is_maker else FEE_TAKER
    return nominal * fee_percent

def proses():
    try:
        aset = aset_var.get()
        is_maker = fee_type.get() == "maker"

        total_beli = 0
        total_eth_beli = 0
        for i in range(3):
            nominal = float(entry_beli[i][0].get() or 0)
            harga = float(entry_beli[i][1].get() or 1)
            eth = nominal / harga
            total_beli += nominal
            total_eth_beli += eth

        total_jual = 0
        total_eth_jual = 0
        for i in range(3):
            nominal = float(entry_jual[i][0].get() or 0)
            harga = float(entry_jual[i][1].get() or 1)
            eth = nominal / harga
            total_jual += nominal
            total_eth_jual += eth

        avg_beli = total_beli / total_eth_beli if total_eth_beli else 0
        avg_jual = total_jual / total_eth_jual if total_eth_jual else 0

        fee_beli = hitung_fee(total_beli, is_maker)
        fee_jual = hitung_fee(total_jual, is_maker)

        modal_untuk_jual = total_eth_jual * avg_beli
        hasil_penjualan = total_eth_jual * avg_jual
        keuntungan_bersih = hasil_penjualan - modal_untuk_jual - fee_beli - fee_jual

        hasil = f"""
=== ANALISA {aset.upper()} ===
Total Dibeli: {total_eth_beli:.8f} {aset.upper()} (modal: {rupiah(total_beli)})
Harga Rata-rata Beli: {rupiah(avg_beli)}

Total Dijual: {total_eth_jual:.8f} {aset.upper()} (hasil: {rupiah(total_jual)})
Harga Rata-rata Jual: {rupiah(avg_jual)}

Fee Beli Total: {rupiah(fee_beli)}
Fee Jual Total: {rupiah(fee_jual)}

Keuntungan Bersih: {rupiah(keuntungan_bersih)}
"""
        output.delete("1.0", tk.END)
        output.insert(tk.END, hasil.strip())
    except Exception as e:
        output.delete("1.0", tk.END)
        output.insert(tk.END, f"Error: {e}")

# === GUI Setup ===
root = tk.Tk()
root.title("Kalkulator Bertahap BTC/ETH/SOL")

# Pilihan Aset
aset_var = tk.StringVar(value="BTC")
tk.Label(root, text="Aset:").grid(row=0, column=0)
ttk.Combobox(root, textvariable=aset_var, values=["BTC", "ETH", "SOL"], width=5).grid(row=0, column=1)

# Pilihan Fee
fee_type = tk.StringVar(value="taker")
ttk.Radiobutton(root, text="Taker", variable=fee_type, value="taker").grid(row=0, column=2)
ttk.Radiobutton(root, text="Maker", variable=fee_type, value="maker").grid(row=0, column=3)

# Input Beli
tk.Label(root, text="Transaksi Beli (Nominal & Harga):").grid(row=1, column=0, columnspan=4)
entry_beli = []
for i in range(3):
    entry_nom = tk.Entry(root, width=10)
    entry_harga = tk.Entry(root, width=12)
    entry_nom.grid(row=2+i, column=1)
    entry_harga.grid(row=2+i, column=2)
    tk.Label(root, text=f"Beli {i+1}").grid(row=2+i, column=0)
    entry_beli.append((entry_nom, entry_harga))

# Input Jual
tk.Label(root, text="Transaksi Jual (Nominal & Harga):").grid(row=6, column=0, columnspan=4)
entry_jual = []
for i in range(3):
    entry_nom = tk.Entry(root, width=10)
    entry_harga = tk.Entry(root, width=12)
    entry_nom.grid(row=7+i, column=1)
    entry_harga.grid(row=7+i, column=2)
    tk.Label(root, text=f"Jual {i+1}").grid(row=7+i, column=0)
    entry_jual.append((entry_nom, entry_harga))

# Tombol dan Output
tk.Button(root, text="Hitung", command=proses).grid(row=10, column=0, columnspan=4, pady=10)
output = tk.Text(root, height=12, width=60)
output.grid(row=11, column=0, columnspan=4)

root.mainloop()
