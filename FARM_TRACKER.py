import tkinter as tk
from tkinter import messagebox

# ----------------------
# Backend / Logic Layer
# ----------------------
def calculate_total_cost(seed_cost, labour_cost):
    """Sum all production costs"""
    return seed_cost + labour_cost

def calculate_revenue(yield_kg, price_per_kg):
    """Calculate total sales revenue"""
    return yield_kg * price_per_kg

def assess_profit(total_cost, total_revenue):
    """Return profit amount and performance category"""
    profit = total_revenue - total_cost
    if profit > 0:
        status = " PROFIT – Good job! Plan to expand next season."
    elif profit < 0:
        status = f" LOSS – You lost {abs(profit):,.2f} SLL. Review costs carefully."
    else:
        status = " BREAK‑EVEN – No profit, no loss."
    return profit, status

# ----------------------
# GUI Layer
# ----------------------
def clear_fields():
    """Reset all input and output fields"""
    for entry in entries:
        entry.delete(0, tk.END)
    output_text.delete("1.0", tk.END)

def process_data():
    """Get inputs, validate, compute, show results"""
    try:
        # Get and convert inputs
        farmer_name = entries[0].get().strip()
        crop_type = entries[1].get().strip()
        land_size = float(entries[2].get())
        seed_cost = float(entries[3].get())
        labour_cost = float(entries[4].get())
        yield_kg = float(entries[5].get())
        price_per_kg = float(entries[6].get())

        # Basic validation
        if not farmer_name or not crop_type:
            raise ValueError("Name and Crop Type cannot be blank.")
        for val in [land_size, seed_cost, labour_cost, yield_kg, price_per_kg]:
            if val < 0:
                raise ValueError("All numeric values must be zero or positive.")

        # Use our functions
        total_cost = calculate_total_cost(seed_cost, labour_cost)
        total_revenue = calculate_revenue(yield_kg, price_per_kg)
        net_profit, status = assess_profit(total_cost, total_revenue)

        # Format output
        report = f"""
FARM RECORD SUMMARY
Farmer Name   : {farmer_name}
Crop Type     : {crop_type}
Land Size     : {land_size:.2f} acres
--------------------------------
Total Cost    : {total_cost:,.2f} SLL
Total Revenue : {total_revenue:,.2f} SLL
Net Profit    : {net_profit:,.2f} SLL
--------------------------------
Result: {status}
        """
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, report)

    except ValueError as err:
        messagebox.showerror("Input Error", str(err))

# Main window setup
root = tk.Tk()
root.title("Sierra Leone Farm Tracker")
root.geometry("550x600")
root.resizable(False, False)

# Labels + Entry list
labels_text = [
    "Farmer Full Name:",
    "Crop Type (e.g. Rice, Cassava):",
    "Land Size (acres):",
    "Seed Cost (SLL):",
    "Labour Cost (SLL):",
    "Total Harvest (kg):",
    "Selling Price per kg (SLL):"
]

entries = []
for idx, txt in enumerate(labels_text):
    tk.Label(root, text=txt, anchor="w").pack(fill="x", padx=10, pady=2)
    ent = tk.Entry(root)
    ent.pack(fill="x", padx=10, pady=2)
    entries.append(ent)

# Buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Calculate & View Report", command=process_data, bg="#2ecc71", fg="white").pack(side="left", padx=5)
tk.Button(btn_frame, text="Clear All", command=clear_fields, bg="#f39c12", fg="white").pack(side="left", padx=5)
tk.Button(btn_frame, text="Exit", command=root.quit, bg="#e74c3c", fg="white").pack(side="left", padx=5)

# Output area
tk.Label(root, text="Result Summary:", anchor="w").pack(fill="x", padx=10, pady=(10, 2))
output_text = tk.Text(root, height=12, width=60)
output_text.pack(padx=10, pady=5)

root.mainloop()