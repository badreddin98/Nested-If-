# Task 1: Code Correction:
#need to convert the input to an integer for comparison.
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
# Task 2: Venue Selection:
if attendees > 60:
  print("Recommend audio system")
if attendees <= 60:
  print("recommend projector")
# Task 3: Catering Choices
food = input("Do you wand vegetarian? ")
if food == "yes":
  print("Recommend Veggie Delight Caterers")
elif food == "no":
  print("Recommend Gourmet Meals Caterers")
else:
  print("Invalid choice")