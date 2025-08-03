"""
Task 2: Airport Luggage Tracker
At Jos Airport, the luggage department tracked passengers and their luggage weights:

luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]

- you need to map each user to its corresponding luggage weight value.

Before the flight took off:
- A late passenger "Daisy" checked in with 20kg of luggage.
- Bob’s luggage went missing.
- The staff prepared a daily report before resetting for the next flight.
"""

luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]
my_luggage = dict(luggage)
print("Total Luggage at airport:\n", my_luggage)

my_luggage["Daisy"] = 20
print("Added Daisy's Luggage:\n", my_luggage)

my_luggage["Bob"] = 0
print("Bob's Luggage went missing:\n", my_luggage)

print("\nDaily Report")
print("Alice Luggage:", my_luggage["Alice"], "kg")
print("Charlie's Luggage:", my_luggage["Charlie"], "kg")
print("Daisy's Luggage:", my_luggage["Daisy"], "kg")
print("Bob is missing his 18kg Luggage:", my_luggage["Bob"], "kg")

