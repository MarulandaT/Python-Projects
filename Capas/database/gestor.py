import sqlite3 
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor() 

    

def sql_table():

    cursorObj.execute("CREATE TABLE IF NOT EXISTS hospitales(id integer PRIMARY KEY AUTOINCREMENT, name text(100))")
    con.commit()

    cursorObj.execute("CREATE TABLE IF NOT EXISTS doctores (id integer PRIMARY KEY, id_hospital integer,  doctorname text(100), speciality text(100), foreign key(id_hospital) references hospitales(id))")
    con.commit()

def insert_hospitales(param): 

    cursorObj.execute("INSERT INTO hospitales(name) values (?)", param)
    con.commit()

def insert_medicos( params):  

    cursorObj.execute("INSERT INTO doctores(id,id_hospital,doctorname,speciality) values (?,?,?,?)", params)
    con.commit()

def buscar_hospital( nombre):

    cursorObj.execute("SELECT * FROM hospitales WHERE name = (?)", nombre)
    rows = cursorObj.fetchall()
    return rows 

def buscar_medico( dni): 
    
    param = (int(dni), )
    
    cursorObj.execute("SELECT * FROM doctores WHERE id = ?", param )
    rows = cursorObj.fetchall()
    
    return rows 

