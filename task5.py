"""
Task 5: Online Shopping Cart
Two friends, Daniella and Godiya, walk into a mall and pick up just one cart to shop with.
Once inside, they split up and go to different wings of the mall, 
but since they share the same cart, everything either of them adds goes into the same cart.

cart = {}
godiya = ???
daniella = ???

During shopping:
- Daniella finds and adds "Shoes" (2 quantity).
- Godiya picks up "Watch" (1 quantity).
- Daniella later changes her mind and removes "Shoes" from the cart.
- Godiya also adds a "Bag" (1 quantity), then later removes it.

At checkout:
- The store takes a snapshot of the final order as an order summary for records.
- The shared cart is then emptied to prepare it for the next customer.
"""


# print(godiya)
# print(daniella)
# print(godiya == daniella) # should return true
# print(summary_of_cart)
# print(cart)

cart = {}
cart["watch"] = 1
godiya = cart
print("Godiya added a watch:", godiya)

cart["shoes"] = 2
print(cart)
daniella = cart
print("Daniella added a shoe:", daniella)

print(id(cart))
print(id(godiya))
print(id(daniella))

print(godiya == daniella)

daniella.pop("shoes")
print("Daniella removed shoes:", daniella)

godiya.update({"bag": 1})
print("Godiya added a bag:", godiya)

godiya.pop("bag")
print("Godiya removed the bag:", godiya)

summary = cart.copy()
print("Snapshot of checkout:", summary)

cart.clear()
print("Emptied cart for next customer", cart)


