import os 
import helper 
import unittest
import subprocess

class testingMethods(unittest.TestCase):
        
    def test_creatingEmailFile(self):
        helper.email("", "", "", "")
        self.assertTrue(helper.findFile())

    def test_creatingTextFile(self):
        helper.text("", "", "", "", "")
        self.assertTrue(helper.findFile())

    def test_deletion(self):
        os.system("del credentials.txt")
        self.assertFalse(helper.findFile())
