import sqlite3

# Connect to or create an SQLite database
conn = sqlite3.connect('voting_analysis.db')
cursor = conn.cursor()

def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Votes (
            CandidateName TEXT PRIMARY KEY,
            Party TEXT,
            AgeGroup TEXT,
            Race TEXT,
            IncomeLevel TEXT,
            Votes INT
        )
    ''')

def update_database(candidate_votes):
    for candidate, data in candidate_votes.items():
        party = data.get('party', None)
        age = data.get('age', None)
        race = data.get('race', None)
        income = data.get('income', None)
        votes = data.get('votes', 0)

        cursor.execute("INSERT OR IGNORE INTO Votes (CandidateName, Party, AgeGroup, Race, IncomeLevel, Votes) VALUES (?, ?, ?, ?, ?, ?)",
                       (candidate, party, age, race, income, votes))
        
        # Removed for causing double vote error
        #cursor.execute("UPDATE Votes SET Votes = Votes + ? WHERE CandidateName = ?", (votes, candidate))

    conn.commit()

def analyze_votes():
    candidate_votes = {}  # Dictionary to store candidate names and their respective votes

    while True:
        candidate_name = input("Enter candidate's name (or 'done' to finish): ").strip().lower()

        if candidate_name == 'done':
            break

        party = input("Enter voter's political party (democrat/republican/independent): ").strip().lower()
        age = input("Enter voter's age group (18-30/31-50/51+): ").strip().lower()
        race = input("Enter voter's race (white/black/asian/other): ").strip().lower()
        income = input("Enter voter's income level (low/middle/high): ").strip().lower()
        votes = int(input("Enter number of votes for this candidate: ").strip())

        # Update candidate_votes for database update
        candidate_votes[candidate_name] = {
            'party': party,
            'age': age,
            'race': race,
            'income': income,
            'votes': votes
        }

    print("Vote analysis based on demographics:")
    print("Candidate Name | Party | Age Group | Race | Income Level")
    for candidate, data in candidate_votes.items():
        print(f"{candidate.capitalize()} | {data['party']} | {data['age']} | {data['race']} | {data['income']}")

    # Update the database with the vote tally
    update_database(candidate_votes)

if __name__ == "__main__":
    print("Welcome to the Voting Polls Demographic Analysis")
    create_tables()  # Create or update the table structure
    analyze_votes()  # Analyze votes and update the database

    # Close the database connection
    conn.close()
