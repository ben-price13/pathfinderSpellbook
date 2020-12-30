import sys
import sqlite3
import json

# Check if no argument was provided
if len(sys.argv) <= 2:
    print("Please provide both arguments: py convertJSONtoSQL.py {filename}.json {databasename}.db")

# Check if argument provided is anything besides .json file
elif not sys.argv[1].endswith(".json"):
    print("First argument must be a .json file: py convertJSONtoSQL.py {filename}.json {databasename}.db")

# Check if second argument is anything besides .db file extension
elif not sys.argv[2].endswith(".db"):
    print("Second argument must be a .db name: py convertJSONtoSQL.py {filename}.json {databasename}.db")

else:

    # --- Prepare data from argument file ---
    # Open and read json file
    with open(sys.argv[1], encoding="utf8") as json_data:
        # Convert json to Python dictionary
        data = json.load(json_data)

    # --- Create/Open connection to database ---
    # create connection to database
    conn = sqlite3.connect(sys.argv[2])
    # create cursor to the database
    c = conn.cursor()

    # --- Create the table ---
    # Check if table 'spells' already exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='spells'")
    # if table 'spells' does not already exist
    if not c.fetchall():
        # Create table
        query_string = '''CREATE TABLE spells
            (duration, components, saving_throw, school, spell_level, name,
            range, description, source, targets, casting_time, alchemist,
            antipaladin, bard, bloodrager, cleric/oracle, druid, inquisitor,
            magus, mesmerist, occultist, paladin, psychic, ranger, shaman,
            spiritualist, sorcerer/wizard, summoner, witch)'''
        c.execute('''CREATE TABLE spells
            (duration, components, saving_throw, school, spell_level, name,
            range, description, source, targets, casting_time, alchemist,
            antipaladin, bard, bloodrager, cleric, druid, inquisitor,
            magus, mesmerist, occultist, paladin, psychic, ranger, shaman,
            spiritualist, sorcerer, summoner, witch)''')

    # --- Enter data into the table ---
    # Loop through data dictionary and enter into database
    for entry in data:
        # Check if data exists in table for the given spell entry
        c.execute("SELECT name FROM spells WHERE name=?", (entry["name"],) )
        if len(c.fetchall()) < 1:
            # Create class dictionary
            classes = {
                "alchemist": "-1",
                "antipaladin": "-1",
                "bard": "-1",
                "bloodrager": "-1",
                "cleric/oracle": "-1",
                "druid": "-1",
                "inquisitor": "-1",
                "magus": "-1",
                "mesmerist": "-1",
                "occultist": "-1",
                "paladin": "-1",
                "psychic": "-1",
                "ranger": "-1",
                "shaman": "-1",
                "spiritualist": "-1",
                "sorcerer/wizard": "-1",
                "summoner": "-1",
                "witch": "-1"
            }

            # Update class dictionary based on entry[spell_level]
            # split string into individual class/level "magus 3, paladin 2" -> "magus 3", "paladin 2"
            spell_level_list = entry["spell_level"].split(", ")
            for i in spell_level_list:
                # split class and level by whitespace "magus 3" -> "magus", "3"
                class_and_level_list = i.split()
                # add to classes dictionary with class as key
                classes[class_and_level_list[0]] = class_and_level_list[1]
            # Insert a row of data
            c.execute("INSERT INTO spells VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                entry["duration"], entry["components"],
                entry["saving_throw"], entry["school"],
                entry["spell_level"], entry["name"],
                entry["range"], entry["description"],
                entry["source"], entry["targets"],
                entry["casting_time"],
                classes["alchemist"], classes["antipaladin"],
                classes["bard"], classes["bloodrager"],
                classes["cleric/oracle"], classes["druid"],
                classes["inquisitor"], classes["magus"],
                classes["mesmerist"], classes["occultist"],
                classes["paladin"], classes["psychic"],
                classes["ranger"], classes["shaman"],
                classes["spiritualist"], classes["sorcerer/wizard"],
                classes["summoner"], classes["witch"]
            ))
            # Save (commit) the changes
            conn.commit()

    # Close the connection to the database
    conn.close()
