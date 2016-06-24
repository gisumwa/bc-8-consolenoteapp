"""
NoteBook
Usage:
    note createnote <note_content>
    note create_note <note_content>
    note searchnotes <query_string>
    note next
    note viewnote <note_id>
    note listnotes [--limit]
    note deletenote <note_id>
    note syncnotes
    note create_json_file
    note quit
    note (-i | --interactive)
    note (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from database import MyDatabase
from functionalitites import NoteFunctionalities
from pyfiglet import figlet_format
from termcolor import cprint, colored


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyNotes(cmd.Cmd):
    def __init__(self):
        self.note_obj = NoteFunctionalities()
        cmd.Cmd.__init__(self)
        self.what_function = []
        self.limit = 0
        self.offset = 0

    def intros(self):
        print('\t ')
        cprint(figlet_format("MAKE A NOTE"), 'green')
        print('-------------------------------------------------------------------------')
        print('\t\t Hello, Welcome to NoteBook')
        print('\t A Simple interactive console app for making and modifying notes')
        print('. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ')
        print('\t\t For any help please print help then enter')
        print('-------------------------------------------------------------------------')

    intro = intros('Welcome')
    prompt = 'NoteBook>> '
    file = None

    def do_createnote(self, note_content):
        """
        Usage: createnote <note_content>
        """
        return self.note_obj.createnote(note_content)

    def do_deletenote(self, note_id):
        """
        Usage: deletenote <note_id>
        """
        self.what_function.append("deletenote")
        return self.note_obj.deletenote(note_id)

    def do_create_note(self, note_content):
        """
            Usage: create_note <note_content>
            """
        self.what_function.append("createnote")
        return self.note_obj.createnote(note_content)

    def do_listnotes(self, limit):
        """
        Usage: listnotes [--limit]
        """
        if limit == '':
            self.what_function.append('list')
            return self.note_obj.listnotes(limit, offset='')
        else:
            self.limit = int(limit)
            if isinstance(self.limit, int):
                self.offset += self.limit
                self.what_function.append('list')
                return self.note_obj.listnotes(self.limit, self.offset)
            else:
                print("The limit must be an integer value")

    def do_syncnotes(self,arg):
        """
        Usage: syncnotes
        """
        return self.note_obj.syncnotes(arg)

    def do_create_json_file(self, arg):
        """
        Usage: create_json_file
        """
        return self.note_obj.create_json_file(arg)

    def do_searchnotes(self, search_arg):
        """
        Usage: searchnotes <query_string> [--limit]
        """
        parameters = search_arg.split(' ')
        print(parameters)
        print(len(parameters))
        if len(parameters) < 2:
            search_arg = parameters[0]
            return self.note_obj.searchnotes(search_arg, limit='', offset='')
        else:
            search_arg = parameters[0]
            limit = int(parameters[1])
            print(type(limit))
            if isinstance(limit, int):
                self.limit = limit
                self.offset += limit
                self.what_function.append('search')
                return self.note_obj.searchnotes(search_arg, self.limit, self.offset)

    def do_viewnote(self, note_id):
        """
        Usage: viewnote <note_id>
        """
        self.what_function.append("viewnote")
        return self.note_obj.viewnote(note_id)

    def do_next(self, search_string):
        """
        Usage: next
        """
        self.what_function.append('next')
        if len(self.what_function) > 1 and len(set(self.what_function)) > 1:
            if self.what_function[-2] == 'search':
                """Next will return the next specified number of files for the
                searchnotes method
                """
                return self.note_obj.searchnotes(search_string, self.limit, self.offset)
                # print("Next for the search functionality")
            elif self.what_function[-2] == 'list':
                """Next will return the next specified number of files for the
                    searchnotes method
                    """
                return self.note_obj.listnotes(self.limit, self.offset)
                # print("Next for list functionality")
            elif self.what_function[-1] == 'next':
                function_list = [x for x in reversed(self.what_function)]
                for function in function_list:
                    if function == 'search':
                        return self.note_obj.searchnotes(search_string, self.search_limit, self.search_offset)
                    else:
                        return self.note_obj.listnotes(self.list_limit, self.list_offset)
            else:
                print("Next only preceeds listnotes or search notes")

        else:
            print("Next cannot be the first command")
            # return self.note_obj.next(arg)

    def do_quit(self):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyNotes().cmdloop()

print(opt)
