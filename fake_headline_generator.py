import random

subjects = [
    "Shahrukh Khan",
    "Virat Kholi",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "Prime Minister Modi",
    "Auto Rikshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "Declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of Samosa",
    "inside Parliament",
    "at Ganga arti",
    "during IPL match",
    "India Gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    print("You entered:", user_input)

    if user_input in ["no", "n"]:
        break

print("\nThanks for using the fake news headline generator. Have a fun day!")