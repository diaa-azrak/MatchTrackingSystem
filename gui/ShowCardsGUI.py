import tkinter as tk
from tkinter import messagebox
import sqlite3  # or use psycopg2 for PostgreSQL

def get_connection():
    # Replace with your DB connection, this example uses SQLite:
    return sqlite3.connect("../sports.db")

class ShowCardsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cards List")
        self.root.geometry("500x400")

        # Listbox with scrollbar to display cards
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set, width=70, height=20)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Button to refresh cards list
        self.refresh_btn = tk.Button(root, text="Show Cards", command=self.show_cards)
        self.refresh_btn.pack(pady=10)

        self.show_cards()  # load cards at start

    def show_cards(self):
        self.listbox.delete(0, tk.END)  # Clear current list

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Query to get card info
            cursor.execute("SELECT card_id, card_name, card_type, card_description FROM cards ORDER BY card_name")
            cards = cursor.fetchall()

            if not cards:
                messagebox.showinfo("Info", "No cards found.")
                return

            # Display cards in the listbox with details
            for card in cards:
                card_id, name, ctype, desc = card
                display_text = f"ID: {card_id} | Name: {name} | Type: {ctype} | Description: {desc}"
                self.listbox.insert(tk.END, display_text)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch cards:\n{e}")
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = ShowCards(root)
    root.mainloop()