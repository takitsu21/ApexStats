#!/usr/bin/env python3
#coding:utf-8
import psycopg2, os

def create_leaderboard():
    sql =""" CREATE TABLE IF NOT EXISTS leaderboard (
            position VARCHAR,
            username VARCHAR,
            level VARCHAR
        )
        """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def create_users():
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
    create_users()
except Exception as e:
    print(f'{type(e).__name__} {e}')

def addUser(id_number,user,platform: str = 'pc'):
    cursor = conn.cursor()
    sql = 'INSERT INTO users(id,username, platform) VALUES(%s, %s, %s);'
    cursor.execute(sql, (id_number, user, platform,))
    conn.commit()

def add_position_leaderboard(position, user, level):
    cursor = conn.cursor()
    sql = 'INSERT INTO leaderboard(position, username, level) VALUES(%s, %s, %s);'
    cursor.execute(sql, (position, user, level,))
    conn.commit()

def select(table, row, value):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM {} WHERE {}={}""".format(table, row, value))
    rows = cursor.fetchall()
    return rows

def change(table,user,value,newValue):
    cursor = conn.cursor()
    sql_command = '''UPDATE ''' + table + ''' SET ''' + value + '''='''+"'"+ newValue +"'"+''' WHERE id=''' + "'" + user + "'" + ''';'''
    print(sql_command)
    cursor.execute(sql_command, (table, value, newValue, user))
    conn.commit()


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
        if row[1] != 'NAN':
            leaderboard_data[row[1]] = row[2]
    return leaderboard_data

def read_table(table):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows
#
def delete_table(table):
    cur = conn.cursor()
    sql = f"DROP TABLE {table}"
    cur.execute(sql)
    conn.commit()
#
# delete_table('leaderboard')
# create_leaderboard()
# for i in range(10):
#     add_position_leaderboard(str(i+1),'NAN', 'NAN')
