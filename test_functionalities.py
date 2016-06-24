import unittest
from functionalities import NoteFunctionalities


class TestNoteFunctionalities(unittest.TestCase):
    def setUp(self):
        self.test_list = ['note1', 'Note2', 'Note3']
        self.test_output = ''

    def test_whether_create_note_parameter_is_empty(self):
        functionality_obj = NoteFunctionalities()
        return self.assertNotEqual('', functionality_obj.create_note, msg="The Note cannot be empty")

    def test_whether_functionality_obj_ia_an_object(self):
        return self.assertIsInstance(object, type(NoteFunctionalities))

    def test_view_note_search_criteria(self):
        return self.assertRaises(Exception, NoteFunctionalities.view_note, '')

    def test_view_note_search_criteria_data_type(self):
        return self.assertEquals(int, type(NoteFunctionalities.view_note(1)))

    def test_delete_note_parameter_data_type(self):
        return self.assertRaises(Exception, NoteFunctionalities.delete_note, int)

    def test_whether_delete_deletes_a_note(self):
        NoteFunctionalities.create_note('note1')
        NoteFunctionalities.create_note('note2')
        len1 = len(NoteFunctionalities.notes_list)
        NoteFunctionalities.delete_note()
        len2 = len(NoteFunctionalities.notes_list)
        self.assertNotEqual(len1, len2, msg="Seems like your delete function aint working")

    def test_whether_create_actually_creates_a_note(self):
        len1 = len(NoteFunctionalities.notes_list)
        NoteFunctionalities.create_note('note1')
        len2 = len(NoteFunctionalities.notes_list)
        return self.assertNotEqual(len1, len2, msg="Seems like your create note function aint working")
    def test_whether_list_prints_all_items(self):
        len1=len(NoteFunctionalities.formatted_note)
        NoteFunctionalities.create_note('note1')
        NoteFunctionalities.create_note('note2')
        len2=len(NoteFunctionalities.formatted_note)
        return self.assertNotEqual(len2,len1,msg="Your list is not returning all the items")
    def test_search_note_parameter_type(self):
        return self.assertRaises(ValueError,NoteFunctionalities.search_notes(criteria=''or isinstance(criteria,int)),int or str)
    def test_whether_search_note_parameter_is_empty(self):
        self.assertRaises(Exception,NoteFunctionalities.search_notes,'')



