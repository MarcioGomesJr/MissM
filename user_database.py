import sqlite3

def saveUser(Id, nome, username):
    conexao = sqlite3.connect('userRegister.db')
    cursor = conexao.cursor()
    #table = "CREATE TABLE IF NOT EXISTS users(Id INTEGER PRIMARY KEY, Nome TEXT, Username TEXT)"
    #cursor.execute(table) 
    
    QUERY = 'INSERT or IGNORE INTO users (Id, Nome, Username) VALUES (?, ?, ?)'
    data_tuple = (Id, nome, '@'+username)

    cursor.execute(QUERY, data_tuple)
    conexao.commit()

    cursor.close()
    conexao.close()

def saveTask(userId, task):
    conexao = sqlite3.connect('userRegister.db')
    cursor = conexao.cursor() 
    #table = "CREATE TABLE IF NOT EXISTS tasks(userId INTEGER, Tasks TEXT, FOREIGN KEY(userId) REFERENCES users(id))"
    #cursor.execute(table)

    QUERY = 'INSERT OR IGNORE INTO tasks (userId, Tasks) VALUES (?, ?)'
    data_tuple = (userId, task)

    cursor.execute(QUERY, data_tuple)
    conexao.commit()

    cursor.close()
    conexao.close()


def fetchTasks(userId):
    conexao = sqlite3.connect('userRegister.db')
    cursor = conexao.cursor() 
    QUERY = 'SELECT * FROM tasks WHERE userId=?'
    task_list = cursor.execute(QUERY, (userId,)).fetchall()

    cursor.close()
    conexao.close()
    return task_list

def deleteTask(userId, task):
    conexao = sqlite3.connect('userRegister.db')
    cursor = conexao.cursor() 
    QUERY = 'DELETE FROM tasks WHERE userId=? AND Tasks=?'
    
    cursor.execute(QUERY,(userId, task))
    conexao.commit()

    cursor.close()
    conexao.close()
    return False

