import sys
import sqlite3
import json

# Check if no argument was provided
if len(sys.argv) <= 2:
    print("Please provide both arguments: py convertJSONtoSQL.py {filename}.json {databasename}.db")

# Check if argument provided is anything besides .json file
elif not sys.argv[1].endswith(".json"):
    print("First argument must be a .json file: py convertJSONtoSQL.py {filename}.json {databasename}.db")

elif not sys.argv[2].endswith(".db"):
    print("Second argument must be a .db name: py convertJSONtoSQL.py {filename}.json {databasename}.db")

else:

    # --- Prepare data from argument file ---
    # Open and read json file
    with open(sys.argv[1], encoding="utf8") as json_data:
        # Convert json to Python dictionary
        data = json.load(json_data)

    # --- Create/Open connection to database
    # create connection to database
    conn = sqlite3.connect(sys.argv[2])
    # create cursor to the database
    c = conn.cursor()

    # Check if table 'spells' already exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='spells'");
    # if table 'spells' does not already exist
    if not c.fetchall():
        # Create table
        c.execute('''CREATE TABLE spells
                     (duration, components, saving_throw, school, spell_level, name,
                     range, description, source, targets, casting_time)''')

    # Loop through data dictionary and enter into database
    for entry in data:
        # Check if data exists in table
        c.execute("SELECT name FROM spells WHERE name=?", (entry["name"],) )
        if len(c.fetchall()) < 1:
            # Insert a row of data
            c.execute("INSERT INTO spells VALUES (?,?,?,?,?,?,?,?,?,?,?)", (
                entry["duration"], entry["components"],
                entry["saving_throw"], entry["school"],
                entry["spell_level"], entry["name"],
                entry["range"], entry["description"],
                entry["source"], entry["targets"],
                entry["casting_time"]))
            # Save (commit) the changes
            conn.commit()

    # close the connection to the database
    conn.close()
