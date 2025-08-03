"""
Task 6: Electronics Store Nested Cart
Three friends, Tobi, Lami, and Chinedu, visit an electronics store together. 
They decide to share **one big smart cart** that can group items by the department they are picked from.
The cart keeps track of each department with the items selected inside it.

cart = {
    "phones": {},
    "laptops": {},
    "accessories": {}
}

Each product in the store is represented as a tuple: (product_name, price) because these details never change.

During shopping:
- Tobi picks up an iPhone for 750000 Naira in the "phones" department.
- Lami adds a Dell XPS Laptop for 1200000 Naira in the "laptops" department.
- Chinedu adds Wireless Earbuds for 50000 Naira in the "accessories" department.
- Tobi changes his mind and removes the iPhone from the cart.
- Lami then adds another accessory: a Gaming Mouse for 35000 Naira.

At checkout:
- A snapshot of the nested cart is taken as the order summary for the store record.
- The shared smart cart is then completely emptied to reset for the next customers.
"""

cart = {
   "phones": {},
   "laptops": {},
   "accessories": {}
}

cart["phones"]["iphone"] = 750000
Tobi = cart
print("\nTobi Added an iphone to the cart:", Tobi)

cart["laptops"]["Dell XPS"] = 1200000
Lami = cart
print("\nLami added a Dell laptop to the cart:", Lami)

cart["accessories"]["Earbuds"] = 50000
Chinedu = cart
print("\nChinedu added an earbud to the cart:", Chinedu)

del Tobi["phones"]["iphone"]
print("\nTobi removed the iphone added to the cart:", Tobi)

Lami["accessories"]["Gaming_Mouse"] = 35000
print("\nLami added a gaming mouse:", Lami)

order_summary = cart.copy()
print("\nSnapshot of order summary:", order_summary)

cart["laptops"].clear()
cart["accessories"].clear()
print("\nCart emptied for the next customer:", cart) 
