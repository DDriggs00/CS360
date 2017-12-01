import queryBuilder     # Dynamically builds query (local file)
import Dict             # Custom Replacements (local file)

import nltk             # For Parsing
import sys              # for sys.exit
import mysql.connector  # for querying db
from mysql.connector import errorcode  # for handling bad connections, etc.


def ReplaceNotFirst(s, old, new):
    li = s.rsplit(old, s.count(old) - 1)
    return new.join(li)


GoodDb = False
while GoodDb is False:
    # IP = input("Select Server IP or \"Exit\" to quit: ")
    # if IP.lower() == "exit":
    #     sys.exit("Have a nice Day :)")
    # User = input("Username: ")
    # Pass = input("Password: ")
    # DB = input("Select Database to use: ")
    User = 'root'
    Pass = 'Password1'
    IP = 'localhost'
    DB = 'Gamedb'
    try:  # try statement to ensure connection is valid
        dbcon = mysql.connector.connect(user=User, password=Pass, host=IP, database=DB)  # CHANGE password and host port LATER
    except mysql.connector.Error as err:
        GoodDb = False  # since connecting threw error
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials\n")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(DB + " is an invalid database name\n")  # maybe print name of valid db?
            # Query: show databases?
        else:
            print("Error with connecting to db: ", err, '\n')
    else:
        GoodDb = True  # no errors caught, db is good
        cursor = dbcon.cursor()  # used to query db

quit = 0
# while True:
# s = input("Please enter a Query or \"Exit\" to quit\n")
s = "Give me a list of all the games in the database that were made by nintendo before 2000"
if s.lower() == "exit":
    sys.exit("Have a nice Day :)")

s = Dict.DoReplacing(s)

if s.lower().find("from database") != -1:
    print("Please select a valid Database Table (Tables are listed below)")
    showTablesQuery = "show tables;"
    cursor.execute(showTablesQuery)  # executes query, we could also just have a static list to print out
    allTables = cursor.fetchall()
    print('\n', allTables, '\n')
    # continue

s = ReplaceNotFirst(s, 'where', 'and')

tokens = nltk.word_tokenize(s)
tagged = nltk.pos_tag(tokens)
print(tagged)
print("\n")
print(s)

s = s.strip()   # Remove Leading and Trailing Whitespace
sqlStmt = queryBuilder.buildQuery(s)  # should be of form select..from..where

try:
    cursor.execute(sqlStmt)
except mysql.connector.Error as err:
    print("Query \"", s, "\" Could not be formed into valid sql")
else:
    output = cursor.fetchall
    print(output)

cursor.close()  # close cursor, bad form to keep open
dbcon.close()   # close connection, bad form to keep open
