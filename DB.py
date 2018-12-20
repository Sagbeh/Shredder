__author__='Sam'
# Imports sqlite3 library for database use
import sqlite3
import datetime

# Define createDB function
def createDB():
        # Connect to the database file
        conn = sqlite3.connect('Shredder.db', isolation_level=None)

        print("\nOpened database successfully\n")

        while True:
                try:
                        # Query to create the Clients table
                        conn.execute('CREATE TABLE CLIENTS \
                                     (clientID INTEGER PRIMARY KEY NOT NULL, \
                                     userName TEXT NOT NULL, \
                                     password TEXT NOT NULL, \
                                     email TEXT NOT NULL);')
                # Catch sqlite error if query is executed and table already exists
                except sqlite3.OperationalError:
                        print("\nTable already exists\n")
                else:
                        print("Table created successfully\n")
                        # Closing the connection to the database file

                break

        while True:
                try:
                        # Query to create the Chest/Back table
                        conn.execute("CREATE TABLE CHESTBACK \
                                     (clientID INTEGER, \
                                     bench REAL NOT NULL, \
                                     seatedDip REAL NOT NULL, \
                                     unilateralRow REAL NOT NULL, \
                                     frontPulldown REAL NOT NULL, \
                                     latPulldown REAL NOT NULL, \
                                     rearFly REAL NOT NULL, \
                                     insertDate TEXT NOT NULL);")
                # Catch sqlite error if query is executed and table already exists
                except sqlite3.OperationalError:
                        print("\nTable already exists\n")
                else:
                        print("Table created successfully\n")
                        # Closing the connection to the database file

                break

        while True:
                try:
                        # Query to create the Arms table
                        conn.execute("CREATE TABLE ARMS \
                                     (clientID INTEGER, \
                                     curl REAL NOT NULL, \
                                     seatedHammer REAL NOT NULL, \
                                     latRaise REAL NOT NULL, \
                                     tricepExtension REAL NOT NULL, \
                                     shoulderRaise REAL NOT NULL, \
                                     insertDate TEXT NOT NULL);")
                # Catch sqlite error if query is executed and table already exists
                except sqlite3.OperationalError:
                        print("\nTable already exists\n")
                else:
                        print("Table created successfully\n")
                        # Closing the connection to the database file

                break

        while True:
                try:
                        # Query to create the Core table
                        conn.execute("CREATE TABLE CORE \
                                     (clientID INTEGER, \
                                     obliqueActivation REAL NOT NULL, \
                                     lowerBackActivation REAL NOT NULL, \
                                     abActivation REAL NOT NULL, \
                                     medicineBall REAL NOT NULL, \
                                     lowerBackPlank REAL NOT NULL, \
                                     sideSpin REAL NOT NULL, \
                                     insertDate TEXT NOT NULL);")
                # Catch sqlite error if query is executed and table already exists
                except sqlite3.OperationalError:
                        print("\nTable already exists\n")
                else:
                        print("Table created successfully\n")
                        # Closing the connection to the database file

                break

        while True:
                try:
                        # Query to create the Legs table
                        conn.execute("CREATE TABLE LEG \
                                     (clientID INTEGER, \
                                     lunges REAL NOT NULL, \
                                     horizontalCalf REAL NOT NULL, \
                                     mtsLegExtension REAL NOT NULL, \
                                     legCurl REAL NOT NULL, \
                                     hipAbduction REAL NOT NULL, \
                                     legPress REAL NOT NULL, \
                                     insertDate TEXT NOT NULL);")
                # Catch sqlite error if query is executed and table already exists
                except sqlite3.OperationalError:
                        print("\nTable already exists\n")
                else:
                        print("Table created successfully\n")
                        # Closing the connection to the database file...

                break

        while True:
                try:
                        # Query to create the Admin table
                        conn.execute('CREATE TABLE ADMIN \
                                     (adminID INTEGER PRIMARY KEY NOT NULL, \
                                     userName TEXT NOT NULL, \
                                     password TEXT NOT NULL);')
                # Catch sqlite error if query is executed and table already exists
                except sqlite3.OperationalError:
                        print("\nTable already exists\n")
                else:
                        print("Table created successfully\n")
                        # Closing the connection to the database file

                break

        sql = "INSERT OR IGNORE INTO ADMIN VALUES ('1', 'Shredder', 'admin')"
        # Executes the insert
        c = conn.cursor()
        c.execute(sql)
        conn.commit()



        conn.close()
# function to obtain cid value
def getCID(user):
    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)

    c = conn.cursor()
    sql = ("SELECT clientID FROM CLIENTS WHERE userName = ?;")
    arg = user
    #fetch one row of data
    row = c.execute(sql, [arg]).fetchone()
    # retreive the element for the first value in the row
    cid = row[0]
    conn.commit()
    conn.close()

    # return the value
    return cid

# function to insert record into clients table
def registerUser(user, password, email):

    try:
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        sql = "INSERT INTO CLIENTS (userName, password, email) \
                                 VALUES (?, ?, ?)"
        arg = (user, password, email)
        # Executes the insert
        c.execute(sql, arg)
        conn.commit()

    except:
        conn.rollback()
        msg = "error in insert operation"
        return msg
    finally:
        msg = "Registration successful!"
        conn.close()
        print('\nRecord updated successfully\n')
        return msg

# function to insert record into tables
def setStartingChestBackWeight(cid, bench, seatedDip, unilateralRow, frontPulldown, latPulldown, rearFly):

    try:
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database
        conn = sqlite3.connect(sqlite_file, isolation_level=None)
        chestC = conn.cursor()

        createdDate = str(datetime.datetime.today())
        print(createdDate)

        chestbackSQL = "INSERT INTO CHESTBACK (clientID, bench, seatedDip, unilateralRow, frontPulldown, latPulldown, rearFly, insertDate) \
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        chestbackARG = (cid, bench, seatedDip, unilateralRow, frontPulldown, latPulldown, rearFly, createdDate)
        # Executes the insert

        chestC.execute(chestbackSQL, chestbackARG)

    except:
        conn.rollback()
        msg = "error in insert operation"
        return msg
    finally:
        msg = "Starting Chest/Back Weights Set Successfully!"
        conn.close()
        print('\nRecord inserted successfully\n')
        return msg

def setStartingArmWeight(cid,curl, seatedHammer, lateralRaise,tricepExtension,shoulderRaise):

    try:
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database
        conn = sqlite3.connect(sqlite_file, isolation_level=None)
        armC = conn.cursor()

        createdDate = str(datetime.datetime.today())
        print(createdDate)

        armsSQL = "INSERT INTO ARMS (clientID, curl, seatedHammer, latRaise, tricepExtension, shoulderRaise, insertDate) \
                                         VALUES (?, ?, ?, ?, ?, ?, ?)"
        armsARG = (cid, curl, seatedHammer, lateralRaise,tricepExtension, shoulderRaise, createdDate)
        # Executes the insert
        armC.execute(armsSQL, armsARG)

    except:
        conn.rollback()
        msg = "error in insert operation"
        return msg
    finally:
        msg = "Starting Arm Weights Set Successfully!"
        print('\nRecord inserted successfully\n')
        return msg


def setStartingCoreWeight(cid,obliqueActivation, lowerBackActivation, abActivation, medicineBall, lowerBackPlank, sideSpin):

    try:
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database
        conn = sqlite3.connect(sqlite_file, isolation_level=None)
        coreC = conn.cursor()

        createdDate = str(datetime.datetime.today())
        print(createdDate)

        coreSQL = "INSERT INTO CORE (clientID, obliqueActivation, lowerBackActivation, abActivation,medicineBall,lowerBackPlank, sideSpin, insertDate) \
                                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        coreARG = (cid, obliqueActivation, lowerBackActivation, abActivation, medicineBall, lowerBackPlank, sideSpin, createdDate)
        # Executes the insert
        coreC.execute(coreSQL, coreARG)

    except:
        conn.rollback()
        msg = "error in insert operation"
        return msg
    finally:
        msg = "Starting Core Weights Set Successfully!"
        conn.close()
        print('\nRecord inserted successfully\n')
        return msg

def setStartingLegWeight(cid, lunges, horizontalCalf, mtsLegExtension, legCurl, hipAbduction, legPress):

    try:
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database
        conn = sqlite3.connect(sqlite_file, isolation_level=None)
        legC = conn.cursor()

        createdDate = str(datetime.datetime.today())
        print(createdDate)

        legSQL = "INSERT INTO LEG (clientID, lunges, horizontalCalf, mtsLegExtension, legCurl, hipAbduction, legPress, insertDate) \
                                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        legARG = (cid, lunges, horizontalCalf, mtsLegExtension, legCurl, hipAbduction, legPress, createdDate)
        # Executes the insert
        legC.execute(legSQL, legARG)
        conn.commit()

    except:
        conn.rollback()
        msg = "error in insert operation"
        return msg
    finally:
        msg = "Starting Leg Weights Set Successfully!"
        conn.close()
        print('\nRecord inserted successfully\n')
        return msg

# function to select all records in customers table

def updateChestBack(cid, pVal):

    try:
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file, isolation_level= None)
        conn.row_factory = sqlite3.Row
        createdDate = str(datetime.datetime.today())

        c = conn.cursor()
        sql = "SELECT * FROM CHESTBACK WHERE clientID = ? order by insertdate desc limit 1;"
        arg = cid

        c.execute(sql, arg)
        conn.commit()

        newBench = ''
        newSeatedDip = ''
        newUnilateralRow = ''
        newFrontpulldown =''
        newLatpulldown = ''
        newReafly = ''


        for row in c:
            newBench = str(int(row[1]) + int(pVal))
            newSeatedDip = str(int(row[2]) + int(pVal))
            newUnilateralRow = str(int(row[3]) + int(pVal))
            newFrontpulldown = str(int(row[4]) + int(pVal))
            newLatpulldown = str(int(row[5]) + int(pVal))
            newReafly = str(int(row[6]) + int(pVal))

        newC = conn.cursor()
        newSQL = "INSERT INTO CHESTBACK (clientID, bench, seatedDip, unilateralRow, frontPulldown, latPulldown, rearFly, insertdate) \
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        newARG = (cid, newBench, newSeatedDip, newUnilateralRow, newFrontpulldown, newLatpulldown, newReafly, createdDate)

        newC.execute(newSQL, newARG)

        conn.close()

    except:
            conn.rollback()
            msg = "error in insert operation"
            return msg
    finally:
        msg = "Update Successful!"
        conn.close()
        print('\nRecord inserted successfully\n')
        return msg



def updateArms(cid, pVal):

    try:
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file, isolation_level= None)
        conn.row_factory = sqlite3.Row
        createdDate = str(datetime.datetime.today())

        c = conn.cursor()
        sql = "SELECT * FROM ARMS WHERE clientID = ? order by insertdate desc limit 1;"
        arg = cid

        c.execute(sql, arg)
        conn.commit()

        newCurl = ''
        newSeatedHammer = ''
        newLatRaise = ''
        newTricepExtension =''
        newShoulderRaise = ''


        for row in c:
            newCurl = str(int(row[1]) + int(pVal))
            newSeatedHammer = str(int(row[2]) + int(pVal))
            newLatRaise = str(int(row[3]) + int(pVal))
            newTricepExtension = str(int(row[4]) + int(pVal))
            newShoulderRaise = str(int(row[5]) + int(pVal))

        newC = conn.cursor()
        newSQL = "INSERT INTO ARMS (clientID, curl, seatedHammer, latRaise, tricepExtension, shoulderRaise, insertdate) \
                 VALUES (?, ?, ?, ?, ?, ?, ?)"
        newARG = (cid, newCurl, newSeatedHammer, newLatRaise, newTricepExtension, newShoulderRaise, createdDate)

        newC.execute(newSQL, newARG)

        conn.close()

    except:
            conn.rollback()
            msg = "error in insert operation"
            return msg
    finally:
        msg = "Update Successful!"
        conn.close()
        print('\nRecord inserted successfully\n')
        return msg

def updateCore(cid, pVal):

    try:
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file, isolation_level= None)
        conn.row_factory = sqlite3.Row
        createdDate = str(datetime.datetime.today())

        c = conn.cursor()
        sql = "SELECT * FROM CORE WHERE clientID = ? order by insertdate desc limit 1;"
        arg = cid

        c.execute(sql, arg)
        conn.commit()

        newobliqueActivation = ''
        newlowerBackActivation = ''
        newabActivation = ''
        newmedicineBall =''
        newlowerBackPlank = ''
        newsideSpin = ''


        for row in c:
            newobliqueActivation = str(int(row[1]) + int(pVal))
            newlowerBackActivation = str(int(row[2]) + int(pVal))
            newabActivation = str(int(row[3]) + int(pVal))
            newmedicineBall = str(int(row[4]) + int(pVal))
            newlowerBackPlank = str(int(row[5]) + int(pVal))
            newsideSpin = str(int(row[6]) + int(pVal))

        newC = conn.cursor()
        newSQL = "INSERT INTO CORE (clientID, obliqueActivation, lowerBackActivation, abActivation, medicineBall, lowerBackPlank, sideSpin, insertdate) \
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        newARG = (cid, newobliqueActivation, newlowerBackActivation, newabActivation, newmedicineBall, newlowerBackPlank, newsideSpin, createdDate)

        newC.execute(newSQL, newARG)

        conn.close()

    except:
            conn.rollback()
            msg = "error in insert operation"
            return msg
    finally:
        msg = "Update Successful!"
        conn.close()
        print('\nRecord inserted successfully\n')
        return msg

def updateLeg(cid, pVal):

    try:
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file, isolation_level= None)
        conn.row_factory = sqlite3.Row
        createdDate = str(datetime.datetime.today())

        c = conn.cursor()
        sql = "SELECT * FROM LEG WHERE clientID = ? order by insertdate desc limit 1;"
        arg = cid

        c.execute(sql, arg)
        conn.commit()

        newlunges = ''
        newhorizontalCalf = ''
        newmtsLegExtension = ''
        newlegCurl =''
        newhipAbduction = ''
        newlegPress = ''


        for row in c:
            newlunges = str(int(row[1]) + int(pVal))
            newhorizontalCalf = str(int(row[2]) + int(pVal))
            newmtsLegExtension = str(int(row[3]) + int(pVal))
            newlegCurl = str(int(row[4]) + int(pVal))
            newhipAbduction = str(int(row[5]) + int(pVal))
            newlegPress = str(int(row[6]) + int(pVal))

        newC = conn.cursor()
        newSQL = "INSERT INTO LEG (clientID, lunges, horizontalCalf, mtsLegExtension, legCurl, hipAbduction, legPress, insertdate) \
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        newARG = (cid, newlunges, newhorizontalCalf, newmtsLegExtension, newlegCurl, newhipAbduction, newlegPress, createdDate)

        newC.execute(newSQL, newARG)

        conn.close()

    except:
            conn.rollback()
            msg = "error in insert operation"
            return msg
    finally:
        msg = "Update Successful!"
        conn.close()
        print('\nRecord inserted successfully\n')
        return msg

def displayClients():
    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row

    c = conn.cursor()
    c.execute("SELECT * FROM CLIENTS")
    conn.commit()

    result = c.fetchall()
    conn.close()

    return result

def displayChestBack():
    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row

    c = conn.cursor()
    sql = "SELECT * FROM CHESTBACK ORDER BY insertDate ASC;"
    c.execute(sql)
    conn.commit()

    result = c.fetchall()
    conn.close()

    return result

# function to select all arms table
def displayArms():
    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row

    c = conn.cursor()
    sql = "SELECT * FROM ARMS ORDER BY insertDate ASC;"
    c.execute(sql)
    conn.commit()

    result = c.fetchall()
    conn.close()

    return result

# function to select all Core table
def displayCore():
    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row

    c = conn.cursor()
    sql = "SELECT * FROM CORE ORDER BY insertDate ASC;"
    c.execute(sql)
    conn.commit()

    result = c.fetchall()
    conn.close()

    return result

# function to select all leg table
def displayLeg():
    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row

    c = conn.cursor()
    sql = "SELECT * FROM LEG ORDER BY insertDate ASC;"
    c.execute(sql)
    conn.commit()

    result = c.fetchall()
    conn.close()

    return result

# function to delete a record from the customers table
def deleteClient(cid):

    try:
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        sql = "DELETE FROM CLIENTS WHERE clientID = ?;"
        arg = (cid)
        c.execute(sql, arg)
        conn.commit()
    except:
        conn.rollback()
        msg = "Client ID doesn't exist"
        return msg
    finally:
        msg = "Client deleted successfully!"
        conn.close()
        print('\nClient deleted successfully\n')
        return msg
# function to search for a customer in the customers table
def searchCustomer(cid):

    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    #  Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql = "SELECT * FROM CLIENTS WHERE clientID = ?;"
    arg = (cid)
    c.execute(sql, arg)
    conn.commit()

    result = c.fetchall()
    conn.close()

    return result

def viewLegProgress(cid):

    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    #  Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql = "SELECT * FROM Leg WHERE clientID = ? ORDER BY insertdate asc;"
    arg = str(cid)
    c.execute(sql, arg)
    conn.commit()

    result = c.fetchall()
    conn.close()

    return result

def viewCoreProgress(cid):

    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    #  Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql = "SELECT * FROM CORE WHERE clientID = ? ORDER BY insertdate asc;"
    arg = str(cid)
    c.execute(sql, arg)
    conn.commit()

    result = c.fetchall()
    conn.close()

    return result

def viewArmsProgress(cid):

    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    #  Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql = "SELECT * FROM ARMS WHERE clientID = ? ORDER BY insertdate asc;"
    arg = str(cid)
    c.execute(sql, arg)
    conn.commit()

    result = c.fetchall()
    conn.close()

    return result

def viewChestBackProgress(cid):

    sqlite_file = 'Shredder.db'  # name of the sqlite database file
    #  Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql = "SELECT * FROM CHESTBACK WHERE clientID = ? ORDER BY insertdate asc;"
    arg = str(cid)
    c.execute(sql, arg)
    conn.commit()

    result = c.fetchall()
    conn.close()

    return result
