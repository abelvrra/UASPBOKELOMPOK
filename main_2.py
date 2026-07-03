import tkinter as tk
from tkinter import ttk

# 
from login_frame_2 import LoginFrame2
from register_frame_2 import RegisterFrame2
from dashboard_frame_2 import DashboardFrame2
from ticket_frame_2 import TicketFrame2
from homestay_frame_2 import HomestayFrame2
from route_frame_2 import RouteFrame2
from cancellation_frame_2 import CancellationFrame2

class GoTravelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GoTravel - Sistem Pemesanan Tiket Wisata")
        self.geometry("1400x800")
        self.resizable(True, True)
        self.minsize(1200, 700)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # User context
        self.active_user = None
        self.user_id = None
        
        # Container
        container = tk.Frame(self, bg="#ffffff")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        # Register all frames
        frame_classes = [
            ("LoginFrame2", LoginFrame2),
            ("RegisterFrame2", RegisterFrame2),
            ("DashboardFrame2", DashboardFrame2),
            ("TicketFrame2", TicketFrame2),
            ("HomestayFrame2", HomestayFrame2),
            ("RouteFrame2", RouteFrame2),
            ("CancellationFrame2", CancellationFrame2),
        ]
        
        for name, cls in frame_classes:
            frame = cls(container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show login first
        self.show_frame("LoginFrame2")
    
    def show_frame(self, name):
        """Display frame and refresh if needed"""
        if name in self.frames:
            frame = self.frames[name]
            frame.tkraise()
            
            if hasattr(frame, 'refresh'):
                frame.refresh()

if __name__ == "__main__":
    app = GoTravelApp()
    app.mainloop()