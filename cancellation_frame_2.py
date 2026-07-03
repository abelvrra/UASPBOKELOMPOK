import tkinter as tk
from tkinter import messagebox
from data_store_2 import DataStore
from colors import BACKGROUND, CARD, PRIMARY

class CancellationFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BACKGROUND)
        self.controller = controller
        
        tk.Label(self, text="Tiket & Booking Saya", font=("Arial", 20, "bold"), bg=BACKGROUND).pack(pady=20, padx=40, anchor="w")
        
        # 1. Canvas dengan Scrollbar untuk menampung kartu tiket
        self.canvas = tk.Canvas(self, bg=BACKGROUND, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=BACKGROUND)
        
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True, padx=40)
        self.scrollbar.pack(side="right", fill="y")
        
        self.items_to_display = []

    def refresh(self):
        # Bersihkan frame sebelum diisi ulang
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        self.items_to_display = []
        
        # Menampilkan data sebagai "Struk/Tiket"
        all_items = [("ticket", t) for t in DataStore.tickets if t["username"] == DataStore.active_user] + \
                    [("homestay", h) for h in DataStore.homestays if h["username"] == DataStore.active_user]
        
        for idx, (item_type, data) in enumerate(all_items):
            self.items_to_display.append((item_type, data))
            
            # Membuat Kartu Bergaya Struk
            card = tk.Frame(self.scrollable_frame, bg=CARD, padx=20, pady=15, highlightbackground="#D1D5DB", highlightthickness=1)
            card.pack(fill="x", pady=10, padx=5)
            
            # Isi Tiket
            if item_type == "ticket":
                tk.Label(card, text="--- TIKET WISATA ---", font=("Courier", 10, "bold"), bg=CARD).pack()
                tk.Label(card, text=f"KODE: {data['kode']}", font=("Courier", 12, "bold"), bg=CARD).pack()
                tk.Label(card, text=f"Destinasi: {data['destinasi']}", bg=CARD).pack()
                tk.Label(card, text=f"Jml: {data['jumlah']} Orang", bg=CARD).pack()
            else:
                tk.Label(card, text="--- BOOKING HOMESTAY ---", font=("Courier", 10, "bold"), bg=CARD).pack()
                tk.Label(card, text=f"Tempat: {data['nama_homestay']}", font=("Courier", 12, "bold"), bg=CARD).pack()
            
            # Tombol Batalkan di setiap kartu
            tk.Button(card, text="Batalkan", bg="#EF4444", fg="white", borderwidth=0,
                      command=lambda i=idx: self.hapus_pesanan(i)).pack(pady=5)

    def hapus_pesanan(self, index):
        item_type, item_data = self.items_to_display[index]
        if item_type == "ticket":
            DataStore.tickets.remove(item_data)
        else:
            DataStore.homestays.remove(item_data)
        messagebox.showinfo("Sukses", "Pesanan dibatalkan.")
        self.refresh()