import Dict     # Custom Replacements (local file)
import queryBuilder # Dynamically builds query (local file)
import nltk     # For Parsing
import sys      # for sys.exit
import mysql.connector # for querying db
from mysql.connector import errorcode # for handling bad connections, etc.


def ReplaceNotFirst(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


 GoodDb = False
 while GoodDb is False:
     DB = input("Select Database to use or \"Exit\" to quit\n")
     if DB.lower() == "exit":
         sys.exit("Have a nice Day :)")
      else
        try: # try statement to ensure connection is valid
          dbcon = mysql.connector.connect(user='Dakota', password='******',
            host='127.0.0.1' database=DB) #CHANGE password and host port LATER
        except mysql.connector.Error as err:
            GoodDb = False # since connecting threw error
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Invalid creds connecting to ", DB)
            elif err.errno == errcode.ER_BAD_DB_ERROR:
                print("Invalid database ", DB) # maybe print name of valid db?
            else
                print("Error with connecting to db:" err)
          #send "use" + DB to Sql
        else
            GoodDb = True # no errors caught, db is good
            cursor = dbcon.cursor() # used to query db
          if output returned true GoodDb = True

quit = 0
# while True:
# s = input("Please enter a Query or \"Exit\" to quit\n")
s = "Give me a list of all the games in the game database that were made by nintendo before 2000"
if s.lower() == "exit":
    sys.exit("Have a nice Day :)")

s = Dict.DoReplacing(s)

if s.lower().find("from database") != -1:
    print("Please select a valid Database Table (Tables are listed below)")
    # MySQL Query show tables (using https://dev.mysql.com/doc/refman/5.7/en/information-schema.html)
    showTablesQuery = "SELECT table_name FROM information_schema.tables;"
    # or use "SHOW TABLES FROM {db_name}"
    cursor.execute(showTablesQuery) # executes query, we could also just have a static list to print out
    allTables = cursor.fetchall()
    print (allTables)
    # continue

s = ReplaceNotFirst(s, 'where', 'and', s.count('where') - 1)

tokens = nltk.word_tokenize(s)
tagged = nltk.pos_tag(tokens)
print(tagged)
print("\n")
print(s)

sqlStmt = queryBuilder.buildQuery(s) # should be of form select..from..where
if s.lower() == "err"
    print("Query ", s, "Could not be formed into valid sql")
else
    cursor.execute(sqlStmt)
    output = cursor.fetchall
    print(output)
# Create MySQL Syntax
# print(s)
cursor.close() # close cursor, bad form to keep open
dbcon.close() # close connection, bad form to keep open
