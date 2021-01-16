import sqlite3
from sqlite3 import Error

def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        
        return conn

def kill_kon(conn):
    conn.close()

def execute(conn, bouise):
    try:
        cursor = conn.cursor()
        cursor.execute(bouise)
        conn.commit()
    except Error as e:
        print(e)

def add_peep(peep):
    database = "dateDecider.db"
    conn = create_connection(database)
    cursor = conn.cursor()
    if conn is not None:
        command = """INSERT INTO people (name) VALUES ('"""+ peep +"""')"""
        cursor.execute(command)
        conn.commit()

        cursor2 = conn.cursor()
        command2 = """select * from people"""
        cursor2.execute(command2)
        rows = cursor2.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        print("peep:  added")
        kill_kon(conn)
    else:
        print("Nope")

def add_domain_key(domain_key):
    database = "dateDecider.db"
    conn = create_connection(database)
    cursor = conn.cursor()
    if conn is not None:
        command = """INSERT INTO domainKey (description) VALUES ('"""+ domain_key +"""')"""
        cursor.execute(command)
        conn.commit()

        cursor2 = conn.cursor()
        command2 = """select * from domainKey"""
        cursor2.execute(command2)
        rows = cursor2.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        print("key: " + domain_key + " added")
        kill_kon(conn)
    else:
        print("Nope")


def createDB():

    database = "dateDecider.db"

    # sql_little_bobby = """DROP TABLE IF EXISTS people"""

    sql_create_people_table = """ CREATE TABLE IF NOT EXISTS people(
        id integer PRIMARY KEY,
        name text NOT NULL
    ); """  
    
    sql_create_domainKey_table = """ CREATE TABLE IF NOT EXISTS domainKey(
        id integer PRIMARY KEY,
        description text NOT NULL
    ); """

    sql_create_domain_table = """ CREATE TABLE IF NOT EXISTS domain(
        id integer PRIMARY KEY,
        description text NOT NULL,
        groupDescription integer NOT NULL
    ); """    

    sql_create_activities_table = """ CREATE TABLE IF NOT EXISTS activities(
        id integer PRIMARY KEY,
        description text NOT NULL,
        cost integer NOT NULL,
        weather integer NOT NULL,
        minTime integer NOT NULL,
        location integer NOT NULL,
        timeToOrganise integer NOT NULL,
        familyFriendly boolean NOT NULL
    ); """    

    sql_create_mapping_table = """ CREATE TABLE IF NOT EXISTS mapping(
        id integer PRIMARY KEY,
        person integer NOT NULL,
        activity integer NOT NULL,
        vibe integer NOT NULL
    ); """

    conn = create_connection(database)

    if conn is not None:
        #execute(conn, sql_little_bobby)
        execute(conn, sql_create_people_table)
        execute(conn, sql_create_domainKey_table)
        execute(conn, sql_create_domain_table)
        execute(conn, sql_create_activities_table)
        execute(conn, sql_create_mapping_table)
        print("created?")
    else:
        print("Error: connection borked")

    kill_kon(conn)    

    

