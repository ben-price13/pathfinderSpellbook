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
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='spells'")
        self.assertEqual(1, len(self.c.fetchall()))

    def test_spell_names(self):
        self.c.execute("SELECT description FROM spells WHERE name='Aid'")
        correct_description = "Aid grants the target a +1 morale bonus on attack rolls and saves against fear effects, plus temporary hit points equal to 1d8 + caster level (to a maximum of 1d8+10 temporary hit points at caster level 10th)."
        self.assertEqual(correct_description, self.c.fetchone()[0])

    def test_num_spells(self):
        self.c.execute("SELECT name FROM spells")
        self.assertEqual(4, len(self.c.fetchall()) )

    def test_rowid(self):
        self.c.execute("SELECT ROWID FROM spells WHERE name='Acid Fog'")
        self.assertEqual(2, self.c.fetchone()[0])

    def test_class_and_level(self):
        self.c.execute("SELECT name, sorcerer FROM spells WHERE sorcerer IS NOT '-1'")
        self.assertEqual([('Acid Arrow', '2'), ('Acid Fog', '6'), ('Acid Splash', '0')], self.c.fetchall())

    def tearDown(self):
        print("---> deleting test.db...\n")
        self.conn.close()
        os.system('del test.db')


if __name__ == '__main__':
    unittest.main()
