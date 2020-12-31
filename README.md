# Pathfinder Spellbook

This will be a web app designed to facilitate keeping track of spells known and memorized spells for characters in the Pathfinder tabletop RPG.

## Dependencies

See requirements.txt file:
- Python==3.9.0
- Flask==1.1.2
- Werkzeug==1.0.1

## Installation instructions

Upon cloning the git repository, open the command line and navigate to the cloned directory. You will need to have the above dependencies installed.

There will be two ways to run the flask server for the website on a local system:

1) Run the python script 'run.py' from the command line.
- Currently this option works for Windows systems only.

2) Alternatively, for Windows you can use the following commands in sequence:
'set FLASK_APP=flaskr'
'flask run'

For Linux or Mac, navigate use the commands in sequence:
'export FLASK_APP=flaskr'
'flask run'

Further information on running a flask program can be found in the documentation:
https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application

## Testing

Currently, the following python scripts utilize the python unittests library to help with regression testing for the codebase:

- unittests.py
-- This file includes the class TestConvertJSONtoSQL that tests the script which creates a database from a json file of spell data.  In particular, this script is utilized to convert PathfinderSpells.json to pathfinderSpellbook.db.  If ANY changes are made to the script convertJSONtoSQL.py, then this test script should be run to ensure no bugs were inserted into the codebase.  If all tests pass, then convertJSONtoSQL.py should be run as follows (on Windows cmd) to rebuild the database:
'del pathfinderSpellbook.db'
'py convertJSONtoSQL PathfinderSpells.json pathfinderSpellbook.db'
