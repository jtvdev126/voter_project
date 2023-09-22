import pandas as pd

# Create total to represent all of voting population
# Create totals for all political parties voters
voter_total = 0 
democratic_voter_total, republican_voter_total, independent_voter_total, unregistered_voter_total = 0
political_affiliation = ["Democratic", "Republican", "Independent", "Unregistered"]

# Totals for age groups
genz_voter_total, millenial_voter_total, genx_voter_total, boomer_voter_total = 0
ages = ["Generation_Z", "Millenial", "Generation_X", "Boomer"]

# Totals for ethnic groups
white, black, hispanic, asian, other = 0
races = ["white", "black", "hispanic", "asian", "other"]

# Totals for genders
male, female, nonbinary = 0
genders = ["male", "female", "nonbinary"]

# Totals for income brackets
poor, middle_class, upper_middle, wealthy = 0

# Totals for education
no_education, high_school_graduate, college_graduate = 0

# Totals for macro geography
urban, suburban, rural = 0

