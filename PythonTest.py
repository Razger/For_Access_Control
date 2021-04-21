import pyodbc
conn = pyodbc.connect("""
Driver={ODBC Driver 17 for SQL Server};
Server=tcp:DESKTOP-RPQNDU8,49172;
Database=For_Access_Control;
UID=Guest;
PWD=Guest;
""")

con = 'y'
ID_REG = 0
LOGIN = 0
loginned = False
while ((con == 'y') and (not loginned)):

    #cursor = conn.cursor()
    #cursor.execute('SELECT * FROM dbo.Reg')

    #print("Input login", end = ' ')
    #str_l = input()
    #print("Input password", end = ' ')
    #str_p = input()
    
    #for row in cursor:
    #    if((str_l == row.Login) and (str_p == row.Password)):
    #        print("IN login")
    #        loginned = True
    #        break
    #if not loginned:
    #    print("Try again (y/n)?")
    #    con = input()

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.NFC_Card')

    print("Attach your card")
    ID_CARD = int(input())

    for row in cursor:
        #print(row.Id_Card, end = ' = ')
        #print(ID_CARD)
        if ID_CARD == row.Id_Card:
            ID_REG = row.Id_Reg
            cursor.commit()
            #cursor = conn.cursor()
            cursor.execute('SELECT * FROM dbo.Reg')


            for row in cursor:
                if ID_REG == row.Id_Reg:
                    LOGIN = row.Login
            cursor.commit()

            print("Entry allowed ",LOGIN)
            loginned = True
            break


    if not loginned:
        print("Try again (y/n)?")
        con = input()
conn.close()

