import sqlite3

# Connect to or create an SQLite database
conn = sqlite3.connect('voting_analysis.db')
cursor = conn.cursor()

def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CandidateVotes (
            CandidateName TEXT PRIMARY KEY,
            Votes INT
        )
    ''')

def update_database(candidate_votes):
    for candidate, votes in candidate_votes.items():
        cursor.execute("INSERT OR IGNORE INTO CandidateVotes VALUES (?, ?)", (candidate, 0))
        cursor.execute("UPDATE CandidateVotes SET Votes = Votes + ? WHERE CandidateName = ?", (votes, candidate))

    conn.commit()

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

    # Update the database with the vote tally
    update_database(candidate_votes)

if __name__ == "__main__":
    print("Welcome to the Voting Polls Tally System")
    create_tables()  # Ensure tables are created in the database
    tally_votes()

    # Close the database connection
    conn.close()
