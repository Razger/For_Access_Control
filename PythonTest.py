import pyodbc
conn = pyodbc.connect("""
Driver={ODBC Driver 17 for SQL Server};
Server=tcp:DESKTOP-RPQNDU8,49172;
Database=For_Access_Control;
UID=Black;
PWD=1156383;
""")

con = 'y'
loginned = False
while ((con == 'y') and (not loginned)):

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.Reg')

    print("Input login", end = ' ')
    str_l = input()
    print("Input password", end = ' ')
    str_p = input()

    for row in cursor:
        if((str_l == row.Login) and (str_p == row.Password)):
            print("IN login")
            loginned = True
            break
    if not loginned:
        print("Try again (y/n)?")
        con = input()
