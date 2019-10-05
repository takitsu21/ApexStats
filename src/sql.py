# coding:utf-8
import psycopg2
import os
from src.config import _dbu_token

try:
    conn = psycopg2.connect(_dbu_token())
except Exception as e:
    print(type(e).__name__, e)

def create_roles_rank():
    sql = """CREATE TABLE IF NOT EXISTS rank (
            id BIGSERIAL,
            username VARCHAR,
            platform VARCHAR,
            rank VARCHAR
    )
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def addUser(id_number, user, platform: str = 'pc'):
    cursor = conn.cursor()
    sql = "INSERT INTO users(id,username, platform) VALUES(%s, %s, %s);"
    cursor.execute(sql, (id_number, user, platform,))
    conn.commit()

def select(table, row, value):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM {} WHERE {} = {}".format(table, row, value))
    rows = cursor.fetchall()
    return rows

def change(table, user, value, newValue):
    cursor = conn.cursor()
    sql_command = f"UPDATE {table} SET {value} = '{newValue}' WHERE id={user};"
    print(sql_command)
    cursor.execute(sql_command, (table, value, newValue, user,))
    conn.commit()

def unlink(value):
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = {}".format(value))
    conn.commit()

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

def add_rank(id, username, platform, rank):
    cur = conn.cursor()
    sql = f"INSERT INTO rank(id, username, platform, rank) VALUES({id}, '{username}', '{platform}', '{rank}')"
    cur.execute(sql)
    conn.commit