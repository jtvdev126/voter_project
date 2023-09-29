#import pandas as pd

# Create total to represent all of voting population
# Create totals for all political parties voters
voter_total = 0 
#democratic_voter_total, republican_voter_total, independent_voter_total, unregistered_voter_total = 0

def tally_voters(user_choice):
    political_affiliation = ("Democrat", "Republican")
    democratic_voter_total = 0
    republican_voter_total = 0
    if user_choice == political_affiliation[0]:
        democratic_voter_total += 1
        return democratic_voter_total
    elif user_choice == political_affiliation[1]:
        republican_voter_total += 1
        return republican_voter_total
    else:
        print("Invalid choice!")
    #print("Dem vote: ", democratic_voter_total)
    #print("Dem vote: ", republican_voter_total)

user_choice = str(input("Enter your choice (Democrat, Republican): "))
count = tally_voters(user_choice)
print("Count:", count)

"""
def count_matching_input(user_input, political_affiliation):
    democratic_voter_total = 0  # Initialize the count variable to 0
    for index in political_affiliation:
        if user_input == political_affiliation:  # Check if the user input matches the current element
            democratic_voter_total += 1  # Increase the count by 1 if there is a match
    return democratic_voter_total

# Example usage:
user_input = input("Enter your input: ")  # Prompt the user for input
political_affiliation = ("Democrat", "Republican", "Independent", "Unregistered")

matching_count = count_matching_input(user_input, political_affiliation)
print("Matching count:", matching_count)
"""


# Totals for age groups
#genz_voter_total, millenial_voter_total, genx_voter_total, boomer_voter_total = 0
#ages = ["Generation_Z", "Millenial", "Generation_X", "Boomer"]

# Totals for ethnic groups
#white, black, hispanic, asian, other = 0
#races = ["white", "black", "hispanic", "asian", "other"]

# Totals for genders
#male, female, nonbinary = 0
#genders = ["male", "female", "nonbinary"]

# Totals for income brackets
#poor, middle_class, upper_middle, wealthy = 0

# Totals for education
#no_education, high_school_graduate, college_graduate = 0

# Totals for macro geography
#urban, suburban, rural = 0

