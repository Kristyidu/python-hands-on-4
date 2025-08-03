"""
Task 1: Music Concert Ticketing System
During the Jos Summer Music Concert, ticket sales were recorded as follows:

tickets = {"VIP": 50, "Regular": 150, "Student": 75}

Later in the day:
- A new "Backstage" experience with 10 tickets was introduced.
- The "Student" category sold out completely.
- The team wanted to keep a record of the day’s sales before preparing for next week’s concert.
"""
tickets = {"VIP": 50, "Regular": 150, "Student": 75}
print("Total tickets for the concert", tickets)

tickets["Backstage"] = 10
print("Introduced backstage tickets:", tickets)

tickets["Student"] = 0
print("Sold out Tickets:", tickets)

print("\nSales record of the day")
print("  VIP:", tickets["VIP"])
print("  Regular:", tickets["Regular"])
print("  Student:", tickets["Student"], "(Sold out tikets)")
print("  Backstage:", tickets["Backstage"])

