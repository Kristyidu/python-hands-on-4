"""
Task 3: Hotel Room Allocation
Hill View Hotel tracked room occupancy as follows:

rooms = {"101": "Alice", "102": "Bob", "103": "Charlie"}

During the evening:
- A new guest "Daisy" was checked into room 104.
- Room 102 was vacated after Bob checked out.
- A last-minute cancellation happened for the most recently allocated room just after the manager backed up the current allocation.
"""

rooms = {"101": "Alice", "102": "Bob", "103": "Charlie"}
print("Total number of occupants:", rooms)

rooms.update({"104": "Daisy"})
print("Daisy rented room 104:", rooms)

rooms["102"] = 0
print("Bob vacated room 102:", rooms)

current_allo =rooms.popitem() 
print("Daisy cancelled her reservation for a room:", current_allo)
print("Print backup report:", rooms)


