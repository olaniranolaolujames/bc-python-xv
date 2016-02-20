import unittest

from notes_taking_app import *

class NoteAppTestSuite(unittest.TestCase):

    def test_create_note_content(self):
        create_note = NotesApplication(["You are presented with two arrays, all containing positive integers. One of the arrays will have one extra number, see below"])
        self.assertEqual(
            create_note.create(),
            ["You are presented with two arrays, all containing positive integers. One of the arrays will have one extra number, see below"],
            msg='should create a new list')

    def test_list_note_content(self): 
    	list_notes =  NotesApplication()
    	self.assertEqual(
    		list_notes.list(),
    		)
    def test_edit(self):
        test = NotesApplication("Akinde",["All will be alright at the end if it is not alright then it mot the end"])
        self.assertEqual(test.edit(0,"All will be alright at the end if it is not alright then it mot the end"),"All will be alright at the end if it is not alright then it mot the end")
​
    def test_empty_add(self):
        test = NotesApplication("Ireti",[])
        self.assertEqual(test.create(""),"Supply your value")
​
    def test_noneValue_in_add(self):
        test = NotesApplication("",[])
        self.assertEqual(test.create(None),"Supply your Value")
​
    def test_addedSuccessfully(self):
        test = NotesApplication("",[])
        self.assertEqual(test.create("Samuel Notes"),test.get(0)+" added")
​
    def test_getIndex(self):
        test = NotesApplication("Chidi",["Is a trainer"])
        test.create("Chidi is a light guy")
        test.create("It is good to be good")
        self.assertEqual(test.get(2),"t is good to be good")
​
    def test_getIndexFalseEntry(self):
        test = NotesApplication("Alake",["Is my oriki"])
        test.create("It is good to be good")
        test.create("It is bad to be bad")
        self.assertNotEqual(test.get(1),"It is bad to be bad")
​
if __name__== "__main__":

    unittest.main()