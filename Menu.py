import tkinter as tk
from tkinter import ttk, messagebox


class RestaurantManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Restaurant Management App')
        self.menu_items = {"FRIES": 2, "LUNCH": 2, "BURGER": 3,
                           "PIZZA": 4, "CHEESE BURGER": 2.5, "DRINKS": 1}
        self.exchange_rate = 86
        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(frame, text="Restaurant Order Management", font=(
            'Arial', 20, 'bold')).grid(row=0, columnspan=3, padx=10, pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame, text=f"{item} (${price}):")
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry
        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="Currency", font=('Arial', 12)).grid(
            row=len(self.menu_items) + 1, column=0, padx=10, pady=5)
        currency_dropdown = ttk.Combobox(
            frame, textvariable=self.currency_var, state='readonly', width=18, values=('USD', 'INR'))
        currency_dropdown.grid(row=len(self.menu_items) +
                               1, column=1, padx=10, pady=5)
        currency_dropdown.current(0)
        self.currency_var.trace('w', self.update_menu_prices)
        order_button = ttk.Button(
            frame, text="Place Order", command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2,
                          columnspan=3, padx=10, pady=10)

    def setup_background(self, root):
        bg_width, bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()
        orignal_image = tk.PhotoImage(file='Background.png')
        background_image = orignal_image.subsample(
            orignal_image.width() // bg_width, orignal_image.height() // bg_height)
        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        canvas.image = background_image

    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == 'INR' else '$'
        rate = self.exchange_rate if currency == 'INR' else 1
        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == 'INR' else '$'
        rate = self.exchange_rate if currency == 'INR' else 1
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please Order At Least 1 Item")


if __name__ == '__main__':
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    root.geometry('800x600')
    root.mainloop()
