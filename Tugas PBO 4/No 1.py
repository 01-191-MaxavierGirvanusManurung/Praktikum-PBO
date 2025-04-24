import tkinter as tk
from tkinter import messagebox, ttk
import datetime

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Catatan")
        self.root.geometry("600x400")
        
        # List untuk menyimpan catatan
        self.notes = []
        
        # Setup GUI
        self.create_menu()
        self.create_widgets()
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # Menu File
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Keluar", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Menu Help
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Tentang", command=self.show_about)
        menubar.add_cascade(label="Bantuan", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def create_widgets(self):
        # Frame input
        input_frame = ttk.LabelFrame(self.root, text="Input Catatan", padding=10)
        input_frame.pack(padx=10, pady=5, fill="x")
        
        # Judul
        ttk.Label(input_frame, text="Judul:").grid(row=0, column=0, sticky="w", pady=2)
        self.title_entry = ttk.Entry(input_frame, width=50)
        self.title_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        
        # Isi Catatan
        ttk.Label(input_frame, text="Isi:").grid(row=1, column=0, sticky="w", pady=2)
        self.content_entry = tk.Text(input_frame, height=10, width=50)
        self.content_entry.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)

        # Frame untuk tombol
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=2, column=1, sticky="e", pady=5)        
        
        # Tombol Tambah
        ttk.Button(button_frame, text="Tambah Catatan", command=self.add_note).pack(side="left", padx=5)
        
        # Tombol Hapus
        ttk.Button(button_frame, text="Hapus Catatan", command=self.delete_note).pack(side="left", padx=5)
        
        # Frame daftar catatan
        list_frame = ttk.LabelFrame(self.root, text="Daftar Catatan", padding=10)
        list_frame.pack(padx=10, pady=5, fill="both", expand=True)
        
        # Treeview untuk daftar catatan
        columns = ("No", "Judul", "Tanggal")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        self.tree.heading("No", text="No")
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Tanggal", text="Tanggal")
        self.tree.column("No", width=50)
        self.tree.column("Judul", width=200)
        self.tree.column("Tanggal", width=150)
        self.tree.pack(fill="both", expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Bind double-click untuk melihat detail
        self.tree.bind("<Double-1>", self.show_note_details)
    
    def validate_input(self, title, content):
        if not title.strip():
            messagebox.showerror("Error", "Judul tidak boleh kosong!")
            return False
        if not content.strip():
            messagebox.showerror("Error", "Isi catatan tidak boleh kosong!")
            return False
        return True
    
    def add_note(self):
        title = self.title_entry.get()
        content = self.content_entry.get("1.0", tk.END).strip()
        
        if self.validate_input(title, content):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note = {"title": title, "content": content, "timestamp": timestamp}
            self.notes.append(note)
            
            # Update treeview
            self.tree.insert("", tk.END, values=(len(self.notes), title, timestamp))
            
            # Clear input
            self.title_entry.delete(0, tk.END)
            self.content_entry.delete("1.0", tk.END)
            
            messagebox.showinfo("Sukses", "Catatan berhasil ditambahkan!")
    
    def delete_note(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih catatan yang ingin dihapus!")
            return
            
        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus catatan ini?"):
            # Dapatkan index dari item yang dipilih
            item = self.tree.item(selected_item)
            note_number = int(item["values"][0]) - 1
            self.notes.pop(note_number)
            
            # Update treeview
            self.tree.delete(selected_item)
            
            # Update nomor urut
            for i, item in enumerate(self.tree.get_children(), 1):
                self.tree.item(item, values=(i, self.tree.item(item)["values"][1], self.tree.item(item)["values"][2]))
            
            messagebox.showinfo("Sukses", "Catatan berhasil dihapus!")
    
    def show_note_details(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            note_number = int(item["values"][0]) - 1
            note = self.notes[note_number]
            
            # Buat window baru untuk detail
            detail_window = tk.Toplevel(self.root)
            detail_window.title("Detail Catatan")
            detail_window.geometry("400x300")
            
            ttk.Label(detail_window, text=f"Judul: {note['title']}").pack(padx=10, pady=5)
            ttk.Label(detail_window, text=f"Tanggal: {note['timestamp']}").pack(padx=10, pady=5)
            
            text_frame = ttk.Frame(detail_window)
            text_frame.pack(padx=10, pady=5, filll="both", expand=True)

            content_text = tk.Text(detail_window, height=10, width=50)
            content_text.insert(tk.END, note["content"])
            content_text.config(state="disabled")
            content_text.pack(side="left", fill="both", expand=True)

            scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=content_text.yview)
            scrollbar.pack(side="right", fill="y")
            content_text.configure(yscrollcommand=scrollbar.set)

            ttk.Button(detail_window, text="Tutup", command=detail_window.destroy).pack(pady=5)
    
    def show_about(self):
        messagebox.showinfo("Tentang", "Aplikasi Catatan\nVersi 1.0\nDibuat dengan Python dan Tkinter\n© 2025")
    
    def exit_app(self):
        if messagebox.askyesno("Keluar", "Yakin ingin keluar dari aplikasi?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
