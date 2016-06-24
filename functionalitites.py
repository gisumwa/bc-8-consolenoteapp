from datetime import datetime
from database import MyDatabase


class NoteFunctionalities(object):
    def __init__(self):
        self.NoteObject = MyDatabase()

    def createnote(self, note):
        """
        Adding a note to the database
        """
        # print(note)
        # note = (" ".join(note['<note>']))
        title = input("Title: ").upper()
        self.NoteObject.createnote(title, note)
        print("Note Successfully Created")

    def viewnote(self, note_id):
        print("Here")
        noteobject = MyDatabase()
        noteobject.viewnote(note_id)

    def deletenote(self, note_id):
        note_id = note_id['<note_id>']
        noteobject = MyDatabase()
        noteobject.deletenote(note_id)

    def listnotes(self, limit, offset):
        noteobject = MyDatabase()
        noteobject.listnotes(limit, offset)
        print("Open records.json to view the notes in a file")

    def searchnotes(self, search_string, limit, offset):
        noteobject = MyDatabase()
        if limit == '':
            noteobject.searchnotes(search_string, limit='', offset='')
        else:
            limit = int(limit)
            offset = int(offset)
            noteobject.searchnotes(search_string, limit, offset)

    def create_json_file(self, arg):
        noteobject = MyDatabase()
        return noteobject.create_json_file(arg)

    def syncnotes(self,arg):
        noteobject = MyDatabase()
        noteobject.syncnotes(arg)

    def upload_json_file(self, arg):
        noteobject = MyDatabase()
        noteobject.upload_json_file(arg)



# NA = NoteFunctionalities()
# NA.create_note("Sample","Sample for person 1")
# NA.list_all('')
# print(type(NA.list_all('')))
# print((NA.search_notes("WORK")))
# NA.search_notes("work")
"""
NA2 = NoteFunctionalities()
NA2.create_note("Sample2","Sample Note 1 for person 2")
NA.create_note("Sample3","Sample Note 2 for person 1")
"""
# print("Notes before delete", NA.list_notes())
# print(NA.view_note(2))
# NA.delete_note(1)
# print("Notes after delete", NA.list_notes())
# print(NA.notes_list.count("Sample Note 3"))
# print(NA.view_note(""))
# print(NA.view_note(5))
