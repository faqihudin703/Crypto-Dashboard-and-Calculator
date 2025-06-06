import tkinter as tk
from tkinter import ttk

FEE_MAKER = 0.2322 / 100
FEE_TAKER = 0.3322 / 100

def hitung_fee(nominal, is_maker):
    fee_percent = FEE_MAKER if is_maker else FEE_TAKER
    return nominal * fee_percent

def rupiah(val):
    return f"Rp{val:,.0f}".replace(",", ".")

def proses():
    try:
        mode = mode_var.get()
        is_maker = fee_type.get() == "maker"
        nominal1 = float(entry_n1.get())
        harga1 = float(entry_h1.get())
        nominal2 = float(entry_n2.get())
        harga2 = float(entry_h2.get())
        selisih_eth = float(entry_selisih.get())

        if mode == "beli_jual":
            eth_beli = nominal1 / harga1
            eth_jual = nominal2 / harga2
            eth_sisa = eth_beli - eth_jual

            nilai_modal_jual = eth_jual * harga1
            nilai_penjualan = eth_jual * harga2

            fee_beli = hitung_fee(nominal1, is_maker)
            fee_jual = hitung_fee(nominal2, is_maker)

            keuntungan_kotor = nilai_penjualan - nilai_modal_jual
            keuntungan_bersih = keuntungan_kotor - fee_beli - fee_jual

            hasil = f"""
=== Mode: BELI → JUAL (ETH) ===
ETH Dibeli  : {eth_beli:.8f}
ETH Dijual  : {eth_jual:.8f}
ETH Sisa    : {eth_sisa:.8f}

Modal ETH Dijual : {rupiah(nilai_modal_jual)}
Penjualan ETH    : {rupiah(nilai_penjualan)}

Fee Beli  : {rupiah(fee_beli)}
Fee Jual  : {rupiah(fee_jual)}
Keuntungan Bersih : {rupiah(keuntungan_bersih)}
"""
        else:
            eth_jual = nominal1 / harga1
            eth_beli = nominal2 / harga2
            eth_selisih = eth_beli - eth_jual

            fee_jual = hitung_fee(nominal1, is_maker)
            fee_beli = hitung_fee(nominal2, is_maker)

            nilai_selisih = eth_selisih * harga2

            hasil = f"""
=== Mode: JUAL → BELI (ETH) ===
ETH Dijual       : {eth_jual:.8f}
ETH Dibeli Kembali: {eth_beli:.8f}
Selisih ETH       : {eth_selisih:.8f}

Fee Jual : {rupiah(fee_jual)}
Fee Beli : {rupiah(fee_beli)}
Nilai Selisih (akumulasi ETH): {rupiah(nilai_selisih)}
"""

        nilai_selisih_eth = selisih_eth * harga2
        hasil += f"\nNilai {selisih_eth} ETH = {rupiah(nilai_selisih_eth)}"

        output.delete("1.0", tk.END)
        output.insert(tk.END, hasil.strip())
    except:
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Masukkan angka yang valid.")

# === GUI ===
root = tk.Tk()
root.title("Kalkulator Keuntungan ETH")

mode_var = tk.StringVar(value="beli_jual")
tk.Label(root, text="Mode Transaksi:").grid(row=0, column=0, sticky="w")
ttk.Radiobutton(root, text="Beli → Jual", variable=mode_var, value="beli_jual").grid(row=0, column=1, sticky="w")
ttk.Radiobutton(root, text="Jual → Beli", variable=mode_var, value="jual_beli").grid(row=0, column=2, sticky="w")

fee_type = tk.StringVar(value="taker")
tk.Label(root, text="Jenis Order:").grid(row=1, column=0, sticky="w")
ttk.Radiobutton(root, text="Market (Taker)", variable=fee_type, value="taker").grid(row=1, column=1, sticky="w")
ttk.Radiobutton(root, text="Limit (Maker)", variable=fee_type, value="maker").grid(row=1, column=2, sticky="w")

tk.Label(root, text="Nominal 1 (Rp):").grid(row=2, column=0)
entry_n1 = tk.Entry(root)
entry_n1.grid(row=2, column=1)

tk.Label(root, text="Harga 1 (Rp):").grid(row=3, column=0)
entry_h1 = tk.Entry(root)
entry_h1.grid(row=3, column=1)

tk.Label(root, text="Nominal 2 (Rp):").grid(row=4, column=0)
entry_n2 = tk.Entry(root)
entry_n2.grid(row=4, column=1)

tk.Label(root, text="Harga 2 (Rp):").grid(row=5, column=0)
entry_h2 = tk.Entry(root)
entry_h2.grid(row=5, column=1)

tk.Label(root, text="Selisih ETH (misal 0.00000001):").grid(row=6, column=0)
entry_selisih = tk.Entry(root)
entry_selisih.grid(row=6, column=1)

tk.Button(root, text="Hitung", command=proses).grid(row=7, column=0, columnspan=2, pady=10)

output = tk.Text(root, height=15, width=65)
output.grid(row=8, column=0, columnspan=3)

root.mainloop()
