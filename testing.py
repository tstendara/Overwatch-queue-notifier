import os 
import helper 
import unittest
import subprocess

class testingMethods(unittest.TestCase):
        
    def test_creatingEmailFile(self):
        helper.email("test", "")
        self.assertTrue(helper.findFile())

    def test_creatingTextFile(self):
        helper.text("test", "", "", "", "")
        self.assertTrue(helper.findFile())

    def test_deletion(self):
        os.system("del credentials.txt")
        self.assertFalse(helper.findFile())

    def test_shouldnt_run(self):
        os.system("python watchingQueue.py")
        self.assertTrue(True)
        
