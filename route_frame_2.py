import tkinter as tk
from tkinter import ttk, messagebox
import math

class RouteFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ffffff")
        self.controller = controller
        
        # Colors
        self.PRIMARY_COLOR = "#27ae60"
        self.TEXT_COLOR = "#2c3e50"
        self.LIGHT_TEXT = "#7f8c8d"
        self.BG_COLOR = "#f5f5f5"
        
        # Create sidebar
        self.create_sidebar()
        
        # Main content
        main_frame = tk.Frame(self, bg="#ffffff")
        main_frame.pack(side="left", fill="both", expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Content area
        self.create_content(main_frame)
    
    def create_sidebar(self):
        """Create left sidebar"""
        sidebar = tk.Frame(self, bg="#f0f0f0", width=200)
        sidebar.pack(side="left", fill="y", padx=0, pady=0)
        sidebar.pack_propagate(False)
        
        # Logo
        logo_frame = tk.Frame(sidebar, bg="#f0f0f0", height=120)
        logo_frame.pack(fill="x", padx=20, pady=20)
        logo_frame.pack_propagate(False)
        
        tk.Label(logo_frame, text="⛩️", font=("Arial", 40), bg="#f0f0f0", fg=self.PRIMARY_COLOR).pack()
        tk.Label(logo_frame, text="GoTravel", font=("Segoe UI", 14, "bold"), bg="#f0f0f0", fg=self.TEXT_COLOR).pack()
        tk.Label(logo_frame, text="Kota Madiun", font=("Segoe UI", 8), bg="#f0f0f0", fg=self.LIGHT_TEXT).pack()
        
        # Menu
        menu_items = [
            ("🏠 Beranda", "DashboardFrame"),
            ("🎟️ Beli Tiket Wisata", "TicketFrame"),
            ("🏨 Booking Homestay", "HomestayFrame"),
            ("🗺️ Cek Rute & Cuaca", "RouteFrame"),
            ("❌ Pembatalan Booking", "CancellationFrame"),
        ]
        
        for text, frame_name in menu_items:
            is_active = (frame_name == "RouteFrame")
            bg_color = "#e8f5e9" if is_active else "#f0f0f0"
            
            btn = tk.Button(sidebar, text=text, font=("Segoe UI", 9), bg=bg_color, fg=self.TEXT_COLOR,
                           border=0, anchor="w", cursor="hand2", padx=15, pady=12,
                           command=lambda f=frame_name: self.controller.show_frame(f))
            btn.pack(fill="x")
        
        # Divider
        ttk.Separator(sidebar, orient="horizontal").pack(fill="x", padx=15, pady=20)
        
        # Logout
        logout_frame = tk.Frame(sidebar, bg="#f0f0f0")
        logout_frame.pack(fill="x", padx=15, pady=10, side="bottom")
        
        tk.Button(logout_frame, text="🚪 Logout", font=("Segoe UI", 10, "bold"), bg="#e74c3c", fg="white",
                 border=0, cursor="hand2", command=self.logout_action, width=22).pack(fill="x", ipady=6)
    
    def create_header(self, parent):
        """Create page header"""
        header_frame = tk.Frame(parent, bg="#ffffff")
        header_frame.pack(fill="x", padx=30, pady=20)
        
        # Title dengan icon
        title_frame = tk.Frame(header_frame, bg="#ffffff")
        title_frame.pack(anchor="w", pady=(0, 10))
        
        tk.Label(title_frame, text="🗺️", font=("Arial", 32), bg="#ffffff", fg=self.PRIMARY_COLOR).pack(side="left", padx=(0, 15))
        tk.Label(title_frame, text="Cek Rute & Cuaca", font=("Segoe UI", 24, "bold"),
                bg="#ffffff", fg=self.TEXT_COLOR).pack(side="left")
        
        # Description
        tk.Label(header_frame, text="Informasi rute ke tempat wisata dan cuaca terkini di Kota Madiun.",
                font=("Segoe UI", 10), bg="#ffffff", fg=self.LIGHT_TEXT).pack(anchor="w")
    
    def create_content(self, parent):
        """Create main content area"""
        content_frame = tk.Frame(parent, bg="#ffffff")
        content_frame.pack(fill="both", expand=True, padx=30, pady=20)
        
        # Left panel - Form
        left_panel = tk.Frame(content_frame, bg="#ffffff")
        left_panel.pack(side="left", fill="y", padx=(0, 20), pady=0)
        
        self.create_form_panel(left_panel)
        
        # Center panel - Map
        center_panel = tk.Frame(content_frame, bg="#ffffff")
        center_panel.pack(side="left", fill="both", expand=True, padx=(0, 20))
        
        self.create_map_panel(center_panel)
        
        # Right panel - Weather
        right_panel = tk.Frame(content_frame, bg="#ffffff")
        right_panel.pack(side="left", fill="y", padx=0)
        
        self.create_weather_panel(right_panel)
    
    def create_form_panel(self, parent):
        """Create left form panel"""
        form_frame = tk.Frame(parent, bg="#ffffff")
        form_frame.pack(fill="y")
        
        # Pilih Destinasi
        tk.Label(form_frame, text="Pilih Destinasi", font=("Segoe UI", 10, "bold"),
                bg="#ffffff", fg=self.TEXT_COLOR).pack(anchor="w", pady=(0, 8))
        
        destinations = ["Alun-Alun Kota Madiun", "Pahlawan Street Center", "Suncity Waterpark", 
                       "Wana Wisata Grape", "Museum Kretek"]
        
        self.combo_dest = ttk.Combobox(form_frame, values=destinations, font=("Segoe UI", 10), 
                                       state="readonly", width=28)
        self.combo_dest.set("Alun-Alun Kota Madiun")
        self.combo_dest.pack(fill="x", pady=(0, 20), ipady=8)
        
        # Lokasi Saya
        tk.Label(form_frame, text="Lokasi Saya", font=("Segoe UI", 10, "bold"),
                bg="#ffffff", fg=self.TEXT_COLOR).pack(anchor="w", pady=(0, 8))
        
        locations = ["Stasiun Madiun", "Alun-Alun Kota Madiun", "Pasar Madiun", 
                    "Rumah Sakit", "Kantor Pemerintah"]
        
        self.combo_location = ttk.Combobox(form_frame, values=locations, font=("Segoe UI", 10),
                                          state="readonly", width=28)
        self.combo_location.set("Stasiun Madiun")
        self.combo_location.pack(fill="x", pady=(0, 20), ipady=8)
        
        # Tampilkan Rute button
        tk.Button(form_frame, text="Tampilkan Rute", font=("Segoe UI", 11, "bold"),
                 bg=self.PRIMARY_COLOR, fg="white", border=0, cursor="hand2", padx=25, pady=10,
                 command=self.show_route).pack(fill="x")
    
    def create_map_panel(self, parent):
        """Create center map panel"""
        map_frame = tk.Frame(parent, bg="#ffffff", relief="solid", bd=1)
        map_frame.pack(fill="both", expand=True)
        
        # Canvas untuk map
        self.canvas = tk.Canvas(map_frame, bg="#e8f0e0", height=400, cursor="hand2")
        self.canvas.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Draw initial map
        self.draw_map()
        
        # Bottom info
        bottom_info = tk.Frame(parent, bg="#ffffff")
        bottom_info.pack(fill="x", pady=(15, 0))
        
        # Time & distance
        time_frame = tk.Frame(bottom_info, bg="#ffffff")
        time_frame.pack(anchor="w")
        
        tk.Label(time_frame, text="⏱️ 15 menit", font=("Segoe UI", 10, "bold"),
                bg="#ffffff", fg=self.TEXT_COLOR).pack(side="left", padx=(0, 20))
        tk.Label(time_frame, text="(5.2 km)", font=("Segoe UI", 9),
                bg="#ffffff", fg=self.LIGHT_TEXT).pack(side="left")
        
        # Source
        tk.Label(bottom_info, text="Sumber: BMKG", font=("Segoe UI", 8),
                bg="#ffffff", fg=self.LIGHT_TEXT).pack(anchor="w", pady=(5, 0))
    
    def draw_map(self):
        """Draw simple map on canvas"""
        self.canvas.delete("all")
        
        # Background
        self.canvas.create_rectangle(0, 0, 500, 400, fill="#e8f0e0", outline="none")
        
        # Draw river/stream (blue)
        points = [250, 50, 280, 100, 270, 150, 290, 200, 260, 250, 280, 300, 250, 350]
        for i in range(0, len(points)-2, 2):
            self.canvas.create_line(points[i], points[i+1], points[i+2], points[i+3],
                                   fill="#87ceeb", width=8, smooth=True)
        
        # Draw route path (green line)
        route_points = [450, 100, 400, 150, 350, 200, 300, 250, 250, 300]
        self.canvas.create_line(route_points, fill=self.PRIMARY_COLOR, width=5, smooth=True)
        
        # Start marker (red pin)
        self.canvas.create_oval(440, 90, 460, 110, fill="#e74c3c", outline="white", width=2)
        self.canvas.create_text(450, 75, text="Alun-Alun", font=("Segoe UI", 9, "bold"),
                               fill=self.TEXT_COLOR)
        self.canvas.create_text(450, 90, text="Kota Madiun", font=("Segoe UI", 8),
                               fill=self.TEXT_COLOR)
        
        # End marker (green pin)
        self.canvas.create_oval(240, 290, 260, 310, fill=self.PRIMARY_COLOR, outline="white", width=2)
        
        # Grid lines untuk map feel
        for i in range(0, 500, 50):
            self.canvas.create_line(i, 0, i, 400, fill="#e0e0e0", dash=(2, 2))
            self.canvas.create_line(0, i, 500, i, fill="#e0e0e0", dash=(2, 2))
    
    def create_weather_panel(self, parent):
        """Create right weather panel"""
        weather_frame = tk.Frame(parent, bg="#ffffff", width=220)
        weather_frame.pack(fill="y", padx=(20, 0))
        weather_frame.pack_propagate(False)
        
        # Title
        tk.Label(weather_frame, text="Cuaca Saat Ini", font=("Segoe UI", 12, "bold"),
                bg="#ffffff", fg=self.TEXT_COLOR).pack(anchor="w", pady=(0, 20))
        
        # Temperature - Large
        temp_frame = tk.Frame(weather_frame, bg="#ffffff")
        temp_frame.pack(anchor="w", pady=(0, 20))
        
        tk.Label(temp_frame, text="☀️", font=("Arial", 40), bg="#ffffff").pack(anchor="w", pady=(0, 10))
        tk.Label(temp_frame, text="28°C", font=("Segoe UI", 32, "bold"),
                bg="#ffffff", fg=self.PRIMARY_COLOR).pack(anchor="w")
        tk.Label(temp_frame, text="Cerah", font=("Segoe UI", 12),
                bg="#ffffff", fg=self.TEXT_COLOR).pack(anchor="w")
        
        # Divider
        ttk.Separator(weather_frame, orient="horizontal").pack(fill="x", pady=20)
        
        # Weather details
        details = [
            ("💧 Kelembaban", "65%"),
            ("💨 Kecepatan Angin", "10 km/jam"),
            ("🌤️ Prakiraan", "Cerah sepanjang hari"),
        ]
        
        for icon_text, value in details:
            detail_frame = tk.Frame(weather_frame, bg="#ffffff")
            detail_frame.pack(fill="x", pady=(0, 12))
            
            tk.Label(detail_frame, text=icon_text, font=("Segoe UI", 9, "bold"),
                    bg="#ffffff", fg=self.TEXT_COLOR).pack(anchor="w")
            tk.Label(detail_frame, text=value, font=("Segoe UI", 9),
                    bg="#ffffff", fg=self.LIGHT_TEXT).pack(anchor="w", pady=(3, 0))
    
    def show_route(self):
        """Show route on map"""
        dest = self.combo_dest.get()
        location = self.combo_location.get()
        
        if dest and location:
            self.draw_map()  # Redraw map
            messagebox.showinfo("Info", f"Rute dari {location}\nke {dest}\nberhasil ditampilkan!")
        else:
            messagebox.showwarning("Peringatan", "Pilih destinasi dan lokasi terlebih dahulu!")
    
    def logout_action(self):
        """Logout"""
        if messagebox.askyesno("Logout", "Apakah Anda yakin ingin logout?"):
            self.controller.active_user = None
            self.controller.show_frame("LoginFrame")
    
    def refresh(self):
        """Refresh frame"""
        pass