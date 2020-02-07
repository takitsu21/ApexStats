# coding:utf-8
import psycopg2
from src.config import _dbu_token
import logging

logger = logging.getLogger("apex-stats")

try:
    conn = psycopg2.connect(_dbu_token())
except Exception as e:
    logger.error(f"{type(e).__name__} : {e}")

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
    sql = "INSERT INTO users(id, username, platform) VALUES(%s, %s, %s);"
    cursor.execute(sql, (id_number, user, platform,))
    conn.commit()

def select(table, row, value):
    cursor = conn.cursor()
    sql = "SELECT * FROM {} WHERE {} = %s;".format(table, row)
    cursor.execute(sql, (value,))
    rows = cursor.fetchall()
    return rows

def change(table, user, value, newValue):
    cursor = conn.cursor()
    sql_command = "UPDATE {} SET {} = %s WHERE id=%s;".format(table, value)
    logger.info(sql_command)
    cursor.execute(sql_command, (newValue, user,))
    conn.commit()

def unlink(value):
    cur = conn.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    cur.execute(sql, (value,))
    conn.commit()

def read_table(table):
    cur = conn.cursor()
    sql = "SELECT * FROM %s"
    cur.execute(sql, (table,))
    rows = cur.fetchall()
    return rows

def delete_table(table):
    cur = conn.cursor()
    sql = "DROP TABLE %s"
    cur.execute(sql, (table,))
    conn.commit()

def add_rank(_id, username, platform, rank):
    cur = conn.cursor()
    sql = "INSERT INTO rank(id, username, platform, rank) VALUES(%s, %s, %s, %s);"
    cur.execute(sql, (_id, username, platform, rank,))
    conn.commit()