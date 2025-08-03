"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""

# print(participants_snapshot)
# print(participants)

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}
total_participant = participants
print("\nTotal number of participants:", total_participant)

print("\n================================")
guest = participants["Guest"] = "Daisy"
print("\nNew guest:", guest)
print("\nNew total number after adding a guest:", total_participant)

remove_participants =  participants.pop("Student")
print("\nRemove student from the list of participants:", remove_participants)
print("\nTotal number of participants after removing students:", participants)
print("\n==================================")
today_records = total_participant.copy()
print("\ntoday's records", today_records)

del total_participant["Guest"]
print("After removing Daisy (Guest) from the live stream:", total_participant)
