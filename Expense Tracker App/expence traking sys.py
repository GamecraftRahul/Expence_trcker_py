import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import DateEntry
from tkinter import ttk, messagebox, filedialog
import mysql.connector
from datetime import datetime
import pandas as pd

# ------------------ DATABASE CONFIG ------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'RAHUL123',   # 🔹 Replace with your password
    'database': 'expense_manager_db'
}

# ------------------ DATABASE SETUP -------------------
def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        return None

def init_db():
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INT AUTO_INCREMENT PRIMARY KEY,
                date DATE NOT NULL,
                category VARCHAR(100) NOT NULL,
                description VARCHAR(255),
                amount DECIMAL(10,2) NOT NULL,
                payment_method VARCHAR(50),
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

# ------------------ MAIN APP CLASS -------------------
class ExpenseApp(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()
        self.refresh_data()

    def create_widgets(self):
        tb.Label(self, text="Expense Management System", font=("Helvetica", 20, "bold")).pack(pady=10)

        # Buttons
        btn_frame = tb.Frame(self)
        btn_frame.pack(pady=5)

        tb.Button(btn_frame, text="Add Expense", bootstyle="success", command=self.open_add_window).grid(row=0, column=0, padx=5)
        tb.Button(btn_frame, text="Delete Selected", bootstyle="danger", command=self.delete_selected).grid(row=0, column=1, padx=5)
        tb.Button(btn_frame, text="Show Summary", bootstyle="info", command=self.show_summary).grid(row=0, column=2, padx=5)
        tb.Button(btn_frame, text="Export CSV", bootstyle="secondary", command=self.export_csv).grid(row=0, column=3, padx=5)
        tb.Button(btn_frame, text="Insert Sample Data", bootstyle="warning", command=self.insert_sample_data).grid(row=0, column=4, padx=5)

        # Table
        cols = ("ID", "Date", "Category", "Description", "Amount", "Payment Method")
        self.tree = ttk.Treeview(self, columns=cols, show='headings', height=15)
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(fill=BOTH, expand=True, pady=10, padx=10)

    # ------------------ CRUD Operations ------------------
    def refresh_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT id, date, category, description, amount, payment_method FROM expenses ORDER BY date DESC")
            for row in cur.fetchall():
                self.tree.insert("", END, values=row)
            conn.close()

    def open_add_window(self):
        AddExpenseWindow(self.master, on_save=self.refresh_data)

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a record to delete.")
            return
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            for sel in selected:
                item_id = self.tree.item(sel)["values"][0]
                cur.execute("DELETE FROM expenses WHERE id=%s", (item_id,))
            conn.commit()
            conn.close()
        self.refresh_data()
        messagebox.showinfo("Deleted", "Selected record(s) deleted successfully!")

    def show_summary(self):
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
            rows = cur.fetchall()
            conn.close()

            if rows:
                summary = '\n'.join([f"{cat}: ₹{amt:.2f}" for cat, amt in rows])
                messagebox.showinfo("Expense Summary", summary)
            else:
                messagebox.showinfo("Expense Summary", "No data found!")

    def export_csv(self):
        conn = get_connection()
        if conn:
            df = pd.read_sql("SELECT * FROM expenses", conn)
            conn.close()
            if not df.empty:
                filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
                if filename:
                    df.to_csv(filename, index=False)
                    messagebox.showinfo("Exported", f"Data exported successfully to {filename}")
            else:
                messagebox.showinfo("No Data", "No data available to export.")

    def insert_sample_data(self):
        sample_data = [
            ("2025-10-01", "Food", "Lunch", 120.00, "Cash"),
            ("2025-10-02", "Transport", "Metro", 45.50, "Card"),
            ("2025-10-03", "Groceries", "Vegetables", 320.00, "UPI"),
            ("2025-10-05", "Bills", "Internet Bill", 699.00, "Online")
        ]
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.executemany("INSERT INTO expenses (date, category, description, amount, payment_method) VALUES (%s, %s, %s, %s, %s)", sample_data)
            conn.commit()
            conn.close()
        self.refresh_data()
        messagebox.showinfo("Success", "Sample data inserted successfully!")

# ------------------ ADD EXPENSE WINDOW ------------------
class AddExpenseWindow(tb.Toplevel):
    def __init__(self, master, on_save=None):
        super().__init__(master)
        self.title("Add Expense")
        self.geometry("400x350")
        self.on_save = on_save
        self.create_widgets()

    def create_widgets(self):
        frame = tb.Frame(self)
        frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

        tb.Label(frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky=W, pady=5)
        self.date_entry = DateEntry(frame, bootstyle="info", dateformat="%Y-%m-%d")
        self.date_entry.grid(row=0, column=1, pady=5)

        tb.Label(frame, text="Category:").grid(row=1, column=0, sticky=W, pady=5)
        self.category_entry = tb.Entry(frame)
        self.category_entry.grid(row=1, column=1, pady=5)

        tb.Label(frame, text="Description:").grid(row=2, column=0, sticky=W, pady=5)
        self.description_entry = tb.Entry(frame)
        self.description_entry.grid(row=2, column=1, pady=5)

        tb.Label(frame, text="Amount:").grid(row=3, column=0, sticky=W, pady=5)
        self.amount_entry = tb.Entry(frame)
        self.amount_entry.grid(row=3, column=1, pady=5)

        tb.Label(frame, text="Payment Method:").grid(row=4, column=0, sticky=W, pady=5)
        self.payment_entry = tb.Entry(frame)
        self.payment_entry.grid(row=4, column=1, pady=5)

        tb.Button(frame, text="Save", bootstyle="success", command=self.save_expense).grid(row=5, column=0, columnspan=2, pady=15)

    def save_expense(self):
        date = self.date_entry.entry.get()
        category = self.category_entry.get().strip()
        description = self.description_entry.get().strip()
        amount = self.amount_entry.get().strip()
        payment = self.payment_entry.get().strip()

        if not (date and category and amount):
            messagebox.showerror("Error", "Please fill all required fields (Date, Category, Amount).")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO expenses (date, category, description, amount, payment_method) VALUES (%s, %s, %s, %s, %s)",
                (date, category, description, amount, payment)
            )
            conn.commit()
            conn.close()

        messagebox.showinfo("Success", "Expense added successfully!")
        if self.on_save:
            self.on_save()
        self.destroy()

# ------------------ MAIN ------------------
def main():
    init_db()
    app = tb.Window(title="Expense Management System", themename="flatly")
    ExpenseApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()
