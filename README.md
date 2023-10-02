<h1>Voter Project:</h1> <h2>A User Input Vote Tally Analysis</h2>

This Python script (`vote_tally_analysis.py`) allows you to analyze voting data based on demographics and store the results in an SQLite database (`voting_analysis.db`).

### Usage

#### Prerequisites

- Python 3.x installed
- SQLite3 installed (if you want to interact with the database manually)

#### Running the Script

1. Clone or download the repository to your local machine.

2. Open a terminal and navigate to the directory containing `vote_tally_analysis.py`.

3. Run the script using Python:

   ```bash
   python vote_tally_analysis.py

4. Follow the on-screen prompts to enter candidate and voter information for analysis.

The script will display a summary of the vote analysis based on demographics and update the voting_analysis.db database.

#### Viewing the Database
You can view the database using an SQLite viewer or the SQLite command-line interface.

SQLite Command-line Interface
1. Open a terminal and navigate to the directory containing voting_analysis.db.

2. Launch the SQLite CLI using:

    ```bash
    sqlite3 voting_analysis.db
  
3. Use SQL commands to query and view the database.

#### Database Schema
The SQLite database ('voting_analysis.db') contains the following tables:

Votes Table: Stores information about voters' choice in candidates and voter demographics including party, age group, race, income level, and the votes in favor of.

## License

This project is licensed under the [MIT License](LICENSE).
