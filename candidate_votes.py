def tally_votes():
    candidate_votes = {}  # Dictionary to store candidate names and their respective votes

    while True:
        candidate_name = input("Enter candidate's name (or 'done' to finish): ").strip().lower()

        if candidate_name == 'done':
            break

        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

    print("Vote tally:")
    for candidate, votes in candidate_votes.items():
        print(f"{candidate}: {votes} votes")

if __name__ == "__main__":
    print("Welcome to the Voting Polls")
    tally_votes()
