from queryBuilder import buildQuery    # Dynamically builds query (local file)

import os                               # for clearing screen
import mysql.connector                  # for querying db
from mysql.connector import errorcode   # for handling bad connections, etc.
from sys import exit                    # for sys.exit
from time import sleep                  # for waiting 1 sec before clearing screen
from getpass import getpass             # For Getting password without echoing


class txt:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    n = '\033[0m'       # Normal
    b = '\033[1m'       # Bold
    u = '\033[4m'       # Underline


Intro = '''This program is designed to convert a natural language input query, such as
\"show me the games that were made in 2017\", convert it into a SQL query, such
as \"select game from games where year = 2017;\", and execute it in MySQL.

This program is designed to read from a database, NOT write to it.

Made by Devin Driggs and Dakota Jackson'''


# Intro Dialogue
print(Intro)
input("Press Enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

# Connect to Server
GoodCon = False
while not GoodCon:
    # IP = input("Select Server IP or \"Exit\" to quit: ")
    # if IP.lower() == "exit":
    #     exit(txt.green + "Have a nice Day :)" + txt.n)
    # User = input("Username: ")
    # Pass = getpass("Password: ")
    User = 'root'
    Pass = 'Password1'
    IP = 'localhost'
    try:  # try statement to ensure connection is valid
        dbcon = mysql.connector.connect(user=User, password=Pass, host=IP)
    except mysql.connector.Error as err:
        GoodCon = False  # since connecting threw error
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(txt.red + "Invalid credentials\n" + txt.n)
        else:
            print(txt.red + "Error with connecting to db: ", err, '\n' + txt.n)
    else:
        GoodCon = True  # no errors caught, db is good
        cursor = dbcon.cursor()  # used to query db

# Select Database
GoodDB = False
while not GoodDB:
    # print(txt.b)
    # cursor.execute('show databases')
    # output = cursor.fetchall()
    # for row in output:
    #     print(row[0])
    # print(txt.n)
    # DB = input("Select Database to use from the list above: ")
    DB = 'Gamedb'
    try:
        cursor.execute('use ' + DB)
    except mysql.connector.Error:
        print(txt.red + DB + " is an invalid database" + txt.n)
    else:
        GoodDB = True

print(txt.green + "Database Connected!" + txt.n)
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

cursor.execute('show tables')
tables = cursor.fetchall()

while True:
    # s = input("Please enter a Query or \"Exit\" to quit\n")
    # if s.lower() == "exit":
    #     exit(txt.green + "Have a nice Day :)" + txt.n)
    s = 'What games were made for systems made by Nintendo'

    s = buildQuery(s, tables)  # should be of form select..from..where
    print('\nYour Query was compiled to: \n' + txt.b + s + txt.n + '\nIf This is not what you meant, try re-wording your query.\n')
    try:
        cursor.execute(s)
    except mysql.connector.Error:
        print(txt.red + "Query Failed to Execute." + txt.n)
    else:
        if s.find("Price") != -1:
            Price = True
        else:
            Price = False
        print('Query Results:' + txt.b)
        output = cursor.fetchall()
        if output:
            for row in output:
                if Price is True:
                    print('$', end='')
                print(row[0])
        else:
            print("No Results")
        print(txt.n)
    exit()

cursor.close()  # close cursor, bad form to keep open
dbcon.close()   # close connection, bad form to keep open
