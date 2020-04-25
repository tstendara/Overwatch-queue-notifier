import os 
import helper 
import unittest
import subprocess

class testingMethods(unittest.TestCase):
        
    def test_creatingEmailFile(self):
        helper.email("s", "s", "s", "s")
        self.assertTrue(helper.findFile())

    def test_creatingTextFile(self):
        helper.text("", "", "", "", "")
        self.assertTrue(helper.findFile())

    def test_runningWatchingQueue(self):
        res = os.system("python watchingQueue.py")
        print('oi')
        boolean = ("..Training bot will let you know when you're in a game!" == res)
        self.assertTrue(res)

    # def test_deletion(self):
    #     os.system("del credentials.txt")
    #     self.assertFalse(helper.findFile())


        


if __name__ == '__main__':
    unittest.main()