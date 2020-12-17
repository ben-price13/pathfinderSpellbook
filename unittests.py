import unittest
import sqlite3
import sys
import os

class TestConvertJSONToSQL(unittest.TestCase):
    def setUp(self):
        print("\n---> setting up test.db...\n")
        os.system('py convertJSONtoSQL.py testData.json test.db')
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()

    def test_spells_table_exists(self):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='spells'");
        self.assertEqual(1, len(self.c.fetchall()))

    def tearDown(self):
        print("---> deleting test.db...\n")
        self.conn.close()
        os.system('del test.db')


if __name__ == '__main__':
    unittest.main()
