import queryBuilder     # Dynamically builds query (local file)

import sys              # for sys.exit
import mysql.connector  # for querying db
from mysql.connector import errorcode   # for handling bad connections, etc.
# from getpass import getpass             # For Getting password without echoing


class txt:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    n = '\033[0m'       # Normal
    b = '\033[1m'       # Bold
    u = '\033[4m'       # Underline


# Connect to Server
GoodCon = False
while not GoodCon:
    # IP = input("Select Server IP or \"Exit\" to quit: ")
    # if IP.lower() == "exit":
    #     sys.exit("Have a nice Day :)")
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
            print("Invalid credentials\n")
        else:
            print("Error with connecting to db: ", err, '\n')
    else:
        GoodCon = True  # no errors caught, db is good
        cursor = dbcon.cursor()  # used to query db

# Select Database
GoodDB = False
while not GoodDB:
    # print('\n')
    # cursor.execute('show databases')
    # output = cursor.fetchall()
    # for row in output:
    #     print(row[0])
    # DB = input("Select Database to use from the list above: ")
    DB = 'Gamedb'
    try:
        cursor.execute('use ' + DB)
    except mysql.connector.Error:
        print(DB + " is an invalid database")
    else:
        GoodDB = True

# while True:
# s = input("Please enter a Query or \"Exit\" to quit\n")
s = 'Show me when Sonic first came out.'
if s.lower() == "exit":
    sys.exit("Have a nice Day :)")

s = queryBuilder.buildQuery(s)  # should be of form select..from..where
print('\nYour Query was compiled to: \n' + txt.b + s + txt.n + '\nIf This is not what you meant, try re-wording your query.\n')
try:
    cursor.execute(s)
except mysql.connector.Error:
    print(txt.red + "Query Failed to Execute." + txt.n)
else:
    print('Query Results:')
    output = cursor.fetchall()
    for row in output:
        print(row[0])

cursor.close()  # close cursor, bad form to keep open
dbcon.close()   # close connection, bad form to keep open
