import sqlite3
import json
import collections
from firebase import firebase
from datetime import datetime
import requests

"""
global method that is going to be visible throughout the program
    """

fbase = firebase.FirebaseApplication("https://noteconsoleapp.firebaseio.com/")


def note_display_format(formatted_output, note):
    formatted_output += "\n {}. Created at: {}\n\t\t  Title:  {}\n\t\tContent: {} \n".format(note[0], note[1],
                                                                                             note[2], note[3])
    return formatted_output


class MyDatabase(object):
    def __init__(self):
        """Connecting to the Database"""
        self.connection = sqlite3.connect('notes.db')
        if self.connection:
            '''Creating a cursor object for sql statement execution'''
            self.cursor = self.connection.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS NotesEntries(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                " time_created TIMESTAMP, note_title TEXT, note_content TEXT)")
            self.connection.commit()
        else:
            print("Could not connect to the database")

    def create_json_file(self, arg):
        """
        Gets current data on DB and saves in a JSON file with JSON format
        """
        with self.connection:
            note_rows = self.cursor.execute("SELECT * FROM NotesEntries")
            notes_list = []
            for note in note_rows:
                d = collections.OrderedDict()
                d['id'] = note[0]
                d['created_at'] = note[1]
                d['title'] = note[2]
                d['note'] = note[3]
                notes_list.append(d)
            with open('noteconsoleapp.json', 'w') as file:
                file.write(json.dumps(notes_list))

    def createnote(self, note_title,
                   note_content):
        """Inserting a note into the database
        :rtype: object
        :param note_content:
        :param note_title:
        """
        with self.connection:
            self.cursor.execute(
                "INSERT INTO NotesEntries(time_created,note_title,note_content) VALUES ('{}','{}','{}')".format(
                    datetime.now(), note_title, note_content))

    def searchnotes(self, search_string, limit, offset):
        """Searching for a given record or records
        :param limit:
        :param offset:
        :param search_string:
        """
        if isinstance(limit, int) and limit > 0:
            with self.connection:
                print("SELECT * FROM NotesEntries WHERE note_content LIKE '%{0}%' or note_title LIKE '%{0}%'"
                      " LIMIT '{1}' OFFSET '{2}'".format(
                    search_string, limit, offset))
                search_list = self.cursor.execute(
                    "SELECT * FROM NotesEntries WHERE note_content LIKE '%{0}%' or note_title LIKE '%{0}%'"
                    " LIMIT '{1}' OFFSET '{2}'".format(
                        search_string, limit, offset))
            formatted_output = ''
            for note in search_list:
                formatted_output = note_display_format(formatted_output, note)
            if len(formatted_output) > 0:
                print(formatted_output)
            else:
                print("OOPS, you are out of records!")

        else:
            print("Executed other")
            with self.connection:
                search_list = self.cursor.execute(
                    "SELECT * FROM NotesEntries WHERE note_title LIKE '%{0}%' or note_content LIKE '%{0}%'".format(
                        search_string))
            formatted_output = ''
            for note in search_list:
                formatted_output = note_display_format(formatted_output, note)
            if len(formatted_output) > 0:
                print(formatted_output)
            else:
                print("{} could not be found".format(search_string))

    def viewnote(self, note_id):
        try:
            note = self.cursor.execute("SELECT * FROM NotesEntries WHERE id = '{}' LIMIT 1".format(note_id))
            formatted_output = ''
            for note in note:
                formatted_output = note_display_format(formatted_output, note)
            print(formatted_output)
        except IndexError:
            print("The note you are trying to access is not available")

    def listnotes(self, limit, offset):
        if isinstance(limit, int) and limit > 0:
            with self.connection:
                notes_list = self.cursor.execute(
                    "SELECT * FROM NotesEntries LIMIT '{}' OFFSET '{}'".format(limit, offset))
        else:
            with self.connection:
                notes_list = self.cursor.execute("SELECT * FROM NotesEntries")
        formatted_output = ''
        for note in notes_list:
            formatted_output = note_display_format(formatted_output, note)
        if len(formatted_output) == 0:
            print("Your Notes list is empty")
        else:
            print(formatted_output)

    def deletenote(self, note_id):
        print(note_id['<note_id>'])
        q = "DELETE FROM NotesEntries WHERE id = {}".format(note_id)
        print(type(self.cursor.execute(q)))
        self.cursor.execute(q)
        self.connection.commit()
        print("Deletion Successful")

    def syncnotes(self, arg):
        with self.connection:
            note_rows = self.cursor.execute("SELECT * FROM NotesEntries")
            notes_list = []
            for note in note_rows:
                d = collections.OrderedDict()
                d['id'] = note[0]
                d['created_at'] = note[1]
                d['title'] = note[2]
                d['note'] = note[3]
                notes_list.append(d)
        try:
            if fbase.put('/noteconsoleapp', 'note3', notes_list):
                print("sync successful, check your firebase to view the changes")
        except:
            raise ConnectionError

    def upload_json_file(self, arg):

        if fbase.put('/noteconsoleapp', 'note', 'noteconsoleapp.json'):
            print("Congrats!! file upload successful")
        else:
            print("upload failed,please check your internet connectivity")
