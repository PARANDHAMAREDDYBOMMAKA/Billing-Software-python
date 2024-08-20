from tkinter import *
from tkinter import messagebox
import random


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("Billing Software")

        # Variables
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.search_bill = StringVar()
        self.bill_no = StringVar()
        self.bill_no.set(str(random.randint(1000, 9999)))

        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.syrup = IntVar()
        self.cream = IntVar()
        self.thermal_gun = IntVar()

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.spices = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()

        self.sprite = IntVar()
        self.mineral = IntVar()
        self.juice = IntVar()
        self.coke = IntVar()
        self.lassi = IntVar()
        self.mountain_duo = IntVar()

        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
        self.total_price = StringVar()

        # Background color
        bg_color = "#07446b"
        fg_color = "#fff"
        title_color = "#1e90ff"

        # Title
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), bg=bg_color,
                      fg=fg_color)
        title.pack(fill=X)

        # Customer Details Frame
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1, height=120)

        cname_lbl = Label(F1, text="Customer Name", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        cname_lbl.grid(row=0, column=0, padx=10, pady=10)
        cname_entry = Entry(F1, textvariable=self.c_name, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        cname_entry.grid(row=0, column=1, padx=10, pady=10)

        cphone_lbl = Label(F1, text="Customer Phone", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        cphone_lbl.grid(row=0, column=2, padx=10, pady=10)
        cphone_entry = Entry(F1, textvariable=self.c_phone, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        cphone_entry.grid(row=0, column=3, padx=10, pady=10)

        search_lbl = Label(F1, text="Search Bill", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        search_lbl.grid(row=1, column=0, padx=10, pady=10)
        search_entry = Entry(F1, textvariable=self.search_bill, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        search_entry.grid(row=1, column=1, padx=10, pady=10)

        search_btn = Button(F1, text="Search", command=self.find_bill, font=('arial', 12, 'bold'), bd=5, width=10,
                            relief=GROOVE)
        search_btn.grid(row=1, column=2, padx=10, pady=10)

        # Billing Area
        F2 = LabelFrame(self.root, text="Billing Area", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F2.place(x=0, y=200, relwidth=1, height=300)

        self.txtarea = Text(F2, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Menu Frames
        F3 = LabelFrame(self.root, text="Medical Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F3.place(x=0, y=500, width=325, height=220)

        sanitizer_lbl = Label(F3, text="Sanitizer", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10)
        sanitizer_entry = Entry(F3, textvariable=self.sanitizer, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        sanitizer_entry.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F3, text="Mask", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        mask_lbl.grid(row=1, column=0, padx=10, pady=10)
        mask_entry = Entry(F3, textvariable=self.mask, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        mask_entry.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F3, text="Hand Gloves", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10)
        hand_gloves_entry = Entry(F3, textvariable=self.hand_gloves, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        hand_gloves_entry.grid(row=2, column=1, padx=10, pady=10)

        syrup_lbl = Label(F3, text="Syrup", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        syrup_lbl.grid(row=3, column=0, padx=10, pady=10)
        syrup_entry = Entry(F3, textvariable=self.syrup, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        syrup_entry.grid(row=3, column=1, padx=10, pady=10)

        cream_lbl = Label(F3, text="Cream", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        cream_lbl.grid(row=4, column=0, padx=10, pady=10)
        cream_entry = Entry(F3, textvariable=self.cream, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        cream_entry.grid(row=4, column=1, padx=10, pady=10)

        thermal_gun_lbl = Label(F3, text="Thermal Gun", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        thermal_gun_lbl.grid(row=5, column=0, padx=10, pady=10)
        thermal_gun_entry = Entry(F3, textvariable=self.thermal_gun, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        thermal_gun_entry.grid(row=5, column=1, padx=10, pady=10)

        F4 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F4.place(x=325, y=500, width=325, height=220)

        rice_lbl = Label(F4, text="Rice", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        rice_lbl.grid(row=0, column=0, padx=10, pady=10)
        rice_entry = Entry(F4, textvariable=self.rice, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        rice_entry.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F4, text="Food Oil", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10)
        food_oil_entry = Entry(F4, textvariable=self.food_oil, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        food_oil_entry.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F4, text="Wheat", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10)
        wheat_entry = Entry(F4, textvariable=self.wheat, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        wheat_entry.grid(row=2, column=1, padx=10, pady=10)

        spices_lbl = Label(F4, text="Spices", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        spices_lbl.grid(row=3, column=0, padx=10, pady=10)
        spices_entry = Entry(F4, textvariable=self.spices, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        spices_entry.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F4, text="Flour", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        flour_lbl.grid(row=4, column=0, padx=10, pady=10)
        flour_entry = Entry(F4, textvariable=self.flour, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        flour_entry.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F4, text="Maggi", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10)
        maggi_entry = Entry(F4, textvariable=self.maggi, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        maggi_entry.grid(row=5, column=1, padx=10, pady=10)

        F5 = LabelFrame(self.root, text="Cold Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F5.place(x=650, y=500, width=325, height=220)

        sprite_lbl = Label(F5, text="Sprite", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10)
        sprite_entry = Entry(F5, textvariable=self.sprite, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        sprite_entry.grid(row=0, column=1, padx=10, pady=10)

        mineral_lbl = Label(F5, text="Mineral Water", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        mineral_lbl.grid(row=1, column=0, padx=10, pady=10)
        mineral_entry = Entry(F5, textvariable=self.mineral, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        mineral_entry.grid(row=1, column=1, padx=10, pady=10)

        juice_lbl = Label(F5, text="Juice", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        juice_lbl.grid(row=2, column=0, padx=10, pady=10)
        juice_entry = Entry(F5, textvariable=self.juice, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        juice_entry.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F5, text="Coke", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        coke_lbl.grid(row=3, column=0, padx=10, pady=10)
        coke_entry = Entry(F5, textvariable=self.coke, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        coke_entry.grid(row=3, column=1, padx=10, pady=10)

        lassi_lbl = Label(F5, text="Lassi", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        lassi_lbl.grid(row=4, column=0, padx=10, pady=10)
        lassi_entry = Entry(F5, textvariable=self.lassi, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        lassi_entry.grid(row=4, column=1, padx=10, pady=10)

        mountain_duo_lbl = Label(F5, text="Mountain Duo", font=('arial', 12, 'bold'), bg=bg_color, fg=fg_color)
        mountain_duo_lbl.grid(row=5, column=0, padx=10, pady=10)
        mountain_duo_entry = Entry(F5, textvariable=self.mountain_duo, font=('arial', 12, 'bold'), bd=5, relief=SUNKEN)
        mountain_duo_entry.grid(row=5, column=1, padx=10, pady=10)

        # Bottom Frame
        F6 = LabelFrame(self.root, text="Bill Menu", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F6.place(x=0, y=710, relwidth=1, height=100)

        total_btn = Button(F6, text="Total", command=self.calculate_total, font=('arial', 12, 'bold'), bd=5, width=10,
                           relief=GROOVE)
        total_btn.grid(row=0, column=0, padx=10, pady=10)

        generate_bill_btn = Button(F6, text="Generate Bill", command=self.generate_bill, font=('arial', 12, 'bold'),
                                   bd=5, width=15, relief=GROOVE)
        generate_bill_btn.grid(row=0, column=1, padx=10, pady=10)

        clear_btn = Button(F6, text="Clear", command=self.clear, font=('arial', 12, 'bold'), bd=5, width=10,
                           relief=GROOVE)
        clear_btn.grid(row=0, column=2, padx=10, pady=10)

        exit_btn = Button(F6, text="Exit", command=self.exit_app, font=('arial', 12, 'bold'), bd=5, width=10,
                          relief=GROOVE)
        exit_btn.grid(row=0, column=3, padx=10, pady=10)

    def calculate_total(self):
        medical_total = (
                self.sanitizer.get() * 50 +
                self.mask.get() * 10 +
                self.hand_gloves.get() * 30 +
                self.syrup.get() * 100 +
                self.cream.get() * 150 +
                self.thermal_gun.get() * 500
        )

        grocery_total = (
                self.rice.get() * 60 +
                self.food_oil.get() * 120 +
                self.wheat.get() * 40 +
                self.spices.get() * 70 +
                self.flour.get() * 50 +
                self.maggi.get() * 20
        )

        cold_drinks_total = (
                self.sprite.get() * 50 +
                self.mineral.get() * 30 +
                self.juice.get() * 60 +
                self.coke.get() * 70 +
                self.lassi.get() * 80 +
                self.mountain_duo.get() * 90
        )

        self.medical_price.set("Rs. " + str(medical_total))
        self.grocery_price.set("Rs. " + str(grocery_total))
        self.cold_drinks_price.set("Rs. " + str(cold_drinks_total))

        total = medical_total + grocery_total + cold_drinks_total
        self.total_price.set("Rs. " + str(total))

    def generate_bill(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer Details are missing")
            return

        bill_details = f"""
        Bill Number: {self.bill_no.get()}
        Customer Name: {self.c_name.get()}
        Customer Phone: {self.c_phone.get()}

        Medical Items:
        Sanitizer: {self.sanitizer.get()} x 50 = Rs. {self.sanitizer.get() * 50}
        Mask: {self.mask.get()} x 10 = Rs. {self.mask.get() * 10}
        Hand Gloves: {self.hand_gloves.get()} x 30 = Rs. {self.hand_gloves.get() * 30}
        Syrup: {self.syrup.get()} x 100 = Rs. {self.syrup.get() * 100}
        Cream: {self.cream.get()} x 150 = Rs. {self.cream.get() * 150}
        Thermal Gun: {self.thermal_gun.get()} x 500 = Rs. {self.thermal_gun.get() * 500}

        Grocery Items:
        Rice: {self.rice.get()} x 60 = Rs. {self.rice.get() * 60}
        Food Oil: {self.food_oil.get()} x 120 = Rs. {self.food_oil.get() * 120}
        Wheat: {self.wheat.get()} x 40 = Rs. {self.wheat.get() * 40}
        Spices: {self.spices.get()} x 70 = Rs. {self.spices.get() * 70}
        Flour: {self.flour.get()} x 50 = Rs. {self.flour.get() * 50}
        Maggi: {self.maggi.get()} x 20 = Rs. {self.maggi.get() * 20}

        Cold Drinks:
        Sprite: {self.sprite.get()} x 50 = Rs. {self.sprite.get() * 50}
        Mineral Water: {self.mineral.get()} x 30 = Rs. {self.mineral.get() * 30}
        Juice: {self.juice.get()} x 60 = Rs. {self.juice.get() * 60}
        Coke: {self.coke.get()} x 70 = Rs. {self.coke.get() * 70}
        Lassi: {self.lassi.get()} x 80 = Rs. {self.lassi.get() * 80}
        Mountain Duo: {self.mountain_duo.get()} x 90 = Rs. {self.mountain_duo.get() * 90}

        --------------------------------------------
        Total Amount: {self.total_price.get()}
        """
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, bill_details)
        self.save_bill()

    def save_bill(self):
        bill = self.txtarea.get(1.0, END)
        with open(f"bills/{self.bill_no.get()}.txt", "w") as file:
            file.write(bill)

    def find_bill(self):
        bill_no = self.search_bill.get()
        try:
            with open(f"bills/{bill_no}.txt", "r") as file:
                bill = file.read()
                self.txtarea.delete(1.0, END)
                self.txtarea.insert(END, bill)
        except FileNotFoundError:
            messagebox.showerror("Error", "Bill not found")

    def clear(self):
        self.c_name.set("")
        self.c_phone.set("")
        self.search_bill.set("")
        self.sanitizer.set(0)
        self.mask.set(0)
        self.hand_gloves.set(0)
        self.syrup.set(0)
        self.cream.set(0)
        self.thermal_gun.set(0)
        self.rice.set(0)
        self.food_oil.set(0)
        self.wheat.set(0)
        self.spices.set(0)
        self.flour.set(0)
        self.maggi.set(0)
        self.sprite.set(0)
        self.mineral.set(0)
        self.juice.set(0)
        self.coke.set(0)
        self.lassi.set(0)
        self.mountain_duo.set(0)
        self.medical_price.set("")
        self.grocery_price.set("")
        self.cold_drinks_price.set("")
        self.total_price.set("")
        self.txtarea.delete(1.0, END)

    def exit_app(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = Bill_App(root)
    root.mainloop()
