import sys
import sqlite3
import json

# Check if no argument was provided
if len(sys.argv) <= 1:
    print("Please provide an argument: py convertJSONtoSQL.py {filename}.json")

# Check if argument provided is anything besides .json file
elif not sys.argv[1].endswith(".json"):
    print("Argument must be a .json file: py convertJSONtoSQL.py {filename}.json")

else:

    # --- Prepare data from argument file ---
    # Open and read json file
    json_data = open(sys.argv[1])
    # Convert json to Python dictionary
    data = json.loads(json_data)
    # Close the file
    json_data.close()

    # --- Create/Open connection to database
    # create connection to database
    conn = sqlite3.connect('pathfinderSpellbook.db')
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
        row_info = (
            entry["duration"], entry["components"],
            entry["saving_throw"], entry["school"],
            entry["spell_level"], entry["name"],
            entry["range"], entry["description"],
            entry["source"], entry["targets"],
            entry["casting_time"])

        # Insert a row of data
        c.execute("INSERT INTO spells VALUES (?,?,?,?,?,?,?,?,?,?,?", row_info)
        # Save (commit) the changes
        conn.commit()

    # close the connection to the database
    conn.close()
