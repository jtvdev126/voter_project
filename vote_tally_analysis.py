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


def analyze_votes():
    # Dictionary to store vote tallies based on different demographics
    vote_data = {
        'parties': {'democrat': 0, 'republican': 0, 'independent': 0},
        'ages': {'under 18': 0, '18-30': 0, '31-50': 0, '51+': 0},
        'races': {'white': 0, 'black': 0, 'asian': 0, 'other': 0},
        'income_levels': {'low': 0, 'middle': 0, 'high': 0}
    }

    candidate_votes = {} # Dictionary to store candidate names and their respective votes

    while True:
        candidate_name = input("Enter candidate's name (or 'done' to finish): ").strip().lower()

        if candidate_name == 'done':
            break

        party = input("Enter voter's political party (democrat/republican/independent): ").strip().lower()
        age = input("Enter voter's age group (under 18/18-30/31-50/51+): ").strip().lower()
        race = input("Enter voter's race (white/black/asian/other): ").strip().lower()
        income = input("Enter voter's income level (low/middle/high): ").strip().lower()

        if party in vote_data['parties']:
            vote_data['parties'][party] += 1

        if age in vote_data['ages']:
            vote_data['ages'][age] += 1

        if race in vote_data['races']:
            vote_data['races'][race] += 1

        if income in vote_data['income_levels']:
            vote_data['income_levels'][income] += 1

        # Update candidate_votes for database update
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1
            
    print("Vote analysis based on demographics:")
    print("Political Party:")
    for party, votes in vote_data['parties'].items():
        print(f"{party.capitalize()}: {votes} votes")

    print("\nAge Group:")
    for age, votes in vote_data['ages'].items():
        print(f"{age.capitalize()}: {votes} votes")

    print("\nRace:")
    for race, votes in vote_data['races'].items():
        print(f"{race.capitalize()}: {votes} votes")

    print("\nIncome Level:")
    for income, votes in vote_data['income_levels'].items():
        print(f"{income.capitalize()}: {votes} votes")

    # Update the database with the vote tally
    update_database(candidate_votes)

if __name__ == "__main__":
    print("Welcome to the Voting Polls Demographic Analysis")
    analyze_votes()

    # Close the database connection
    conn.close()
