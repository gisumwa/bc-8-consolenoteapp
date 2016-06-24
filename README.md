#NOTEBOOK
This repo only contains the project files for the Note taking console application Introduction

NoteBook is a simple console app to record your thoughts and events Some of its features include: Creating a new note Searching for a journal using an id Viewing a specific note entry Viewing all note entries Deleting note entries Installation and Setup

Read the instructions below to run ThoughtBook

Install python

Download Python onto your computer by using the following links

Windows - Python Downloads Mac - Python for Mac OS X Ubuntu - install python2.x and python2.x-dev packages Other systems - see the general download page To ensure you have Python on your computer:

Open the Command Prompt Type Python. If you have Python installed, you should see a response that includes the version number. Clone the repository to your local folder of your choice

On GitHub navigate the main page of the repository. https://github.com/gisumwa/bc-8-consolenoteapp/ automatic! Under the repository name, click on the URL and copy it Open Git Bash Change the working directory on cmd to the location where you want your clone made Type 'git clone ' and paste the URL Press Enter* to finish creating your cloned repository Install the virtual environment

To install globally with pip type the command $ pip install virtualenv Install required modules

Open the requirements.txt file and pip install the required modules using pip install -r requirements.txt Run ThoughtBook app

On your console type in python my_journal.py -i to run the app interactively App Functions

The app enables a user to do certain processes by using the following commands

create_note (enables a user to enter a journal entry's body) searchnote --limit viewnote (opens a specific journal entry based on ID) listnotes --limit delete (delete a journal based on the text) Dependencies

To run the app you need to install all the modules used in the code. Install the modules by installing the requirements.py
