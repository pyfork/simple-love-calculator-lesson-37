# Welcome user
print("Welcome to the Love Calculator!")

# Get user's and their partner's name
name_1 = input("What is your name? \n")
name_2 = input("What is their name? \n")

# Turn names to lowercase to count characters using count()
# Remove whitespaces
# Combine names
name_1_in_lowercase = name_1.lower()
name_2_in_lowercase = name_2.lower()

name_1_no_whitespace = name_1_in_lowercase.replace(" ", "")
name_2_no_whitespace = name_2_in_lowercase.replace(" ", "")

combined_name = name_1_no_whitespace + name_2_no_whitespace

# print(name_1_no_whitespace)
# print(name_2_no_whitespace)
# print(combined_name)

# Count freq of TRUE characters
cal_true = combined_name.count("t") + combined_name.count("r") +combined_name.count("u") +combined_name.count("e") 
# print(cal_true)

# Count freq of LOVE characters
cal_love = combined_name.count("l") + combined_name.count("o") +combined_name.count("v") +combined_name.count("e") 
# print(cal_love)

# Convert the scores to strings
# Combine the two strings
lovemarks = str(cal_true) + str(cal_love)
# lovemarks = lovemarks_spaced.replace(" ", "")

# Convert string to integer
lovescore = int(lovemarks)

# Customise response based on score
if lovescore <10 or lovescore>90:
    print(f"Your score is {lovescore}, you go together like Coke and Mentos.")
elif lovescore >40 and lovescore<50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")

