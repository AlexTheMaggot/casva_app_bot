import sqlite3

db = sqlite3.connect('db.sqlite3')


def create_user(id):
    db.cursor().execute('INSERT into users (user_id, is_admin) VALUES ({0}, false)'.format(id))
    db.commit()


def check_user(id):
    user = db.cursor().execute('SELECT * FROM users WHERE user_id = {0}'.format(id)).fetchall()
    if user:
        return True
    else:
        return False


def check_admin(id):
    user = db.cursor().execute('SELECT * FROM users WHERE user_id = {0}'.format(id)).fetchall()
    if user[0][1]:
        return True
    else:
        return False


def get_user_list():
    users = db.cursor().execute('SELECT * FROM users').fetchall()
    user_list = []
    for item in users:
        user_list.append(item[0])
    return user_list




def create_file(id):
    db.cursor().execute('DELETE FROM file')
    db.cursor().execute('INSERT INTO file (file_id) VALUES ("{0}")'.format(id))
    db.commit()
    return True


def get_file():
    file = db.cursor().execute('SELECT * FROM file').fetchall()
    return file[0][1]
