import sqlite3

db = sqlite3.connect("players.db")

def createTables():
    sql = '''CREATE TABLE IF NOT EXISTS `users` (
	`id` int(18) NOT NULL,
	`user` varchar(255),
    `platform` varchar(255)
            );'''
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

createTables()

def add_user(id_number,user,platform='pc'):
    cursor = db.cursor()
    sql = '''INSERT INTO users(id,user, platform) VALUES(?,?,?)'''
    cursor.execute(sql,(id_number,user,platform))
    db.commit()

    print("Added " + str(id_number) + " To database!")


def select(user_id):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM users WHERE id=?""",(user_id,))
    rows = cursor.fetchall()
    return rows

def change(table,user,value,newValue):
    cursor = db.cursor()
    sql_command = '''UPDATE ''' + table + ''' SET ''' + value + '''='''+"'"+ newValue +"'"+''' WHERE id=''' + "'" + user + "'" + ''';'''
    cursor.execute(sql_command)
    db.commit()
    # print("Changed " + user + "'s " + value + " value to " + newValue)
