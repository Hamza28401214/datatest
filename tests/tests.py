import unittest
from etl.etl import *


class TestReadFromDb(unittest.TestCase):
    def test1(self):
        con = sqlite3.connect(pat + '\\database//final_data.db')
        cur = con.cursor()
        querry = "SELECT * from tun_tab LIMIT 10"
        v = cur.execute(querry).fetchall()
        self.assertEqual(len(v), 10)
    def test2(self):
        con = sqlite3.connect(pat + '\\database//final_data.db')
        cur = con.cursor()
        querry = "SELECT * from tun_tab LIMIT 50"
        v = cur.execute(querry).fetchall()
        self.assertEqual(len(v), 50)

#python -m unittest     tests.tests.TestReadFromDb
if __name__ == '__main__':
    TestReadFromDb
