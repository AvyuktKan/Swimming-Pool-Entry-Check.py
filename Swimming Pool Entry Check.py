print("=== Swimming Pool Entry Check ===")
print("Answer 3 questions and I will tell you which pool you can use. \n")

age = int(input("Enter your age: "))
if age < 5:
    print("You are too young to enter the pool.")
else:
    print("You are eligible to enter the pool.")
choice = input("Can you swim 25 meters? (yes/no): ").lower()
if choice == "yes":
    print("You can use the deep pool.")
else:
    print("You cannot use the deep pool.")