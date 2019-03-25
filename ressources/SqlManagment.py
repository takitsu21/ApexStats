#coding: utf-8
#!/usr/bin/python3
import psycopg2, os

def createTables():
    sql =""" CREATE TABLE IF NOT EXISTS users (
            id BIGSERIAL,
            username VARCHAR,
            platform VARCHAR
        )
        """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

try:
    conn = psycopg2.connect(host=os.environ['host'],
                        database=os.environ['database'],
                        user=os.environ['user'],
                        password=os.environ['password'])
    createTables()
except Exception as e:
    print(f'{type(e).__name__} {e}')

def addUser(id_number,user,platform: str = 'pc'):
    cursor = conn.cursor()
    sql = 'INSERT INTO users(id,username, platform) VALUES(%s, %s, %s);'
    cursor.execute(sql, (id_number, user, platform,))
    conn.commit()


def select(user_id):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users WHERE id=%s""",(user_id,))
    rows = cursor.fetchall()
    return rows

def change(table,user,value,newValue):
    cursor = conn.cursor()
    sql_command = '''UPDATE ''' + table + ''' SET ''' + value + '''='''+"'"+ newValue +"'"+''' WHERE id=''' + "'" + user + "'" + ''';'''
    cursor.execute(sql_command, (table, value, newValue, user))
    conn.commit()

    print("Changed " + user + "'s " + value + " value to " + newValue)

def unlink(value):
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id={}".format(value))
    conn.commit()


def createLeaderboard():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    leaderboard_data = {}
    for row in rows:
        leaderboard_data[row[1]] = row[2]
    return leaderboard_data
