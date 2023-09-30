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



