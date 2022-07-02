import sqlite3

h=sqlite3.connect("test.db")

try:
    h.execute("CREATE TABLE MOVIES(NAME, ACTOR, ACTRESS, DIRECTOR, YEAR);")
except:
    pass

Di=''

while(Di !='4'):
    print(" 1-Insert \n 2-Search \n 3-Show \n 4-Quit ")
    
    Di = input("ENTER CHOICE:")
    if(Di == '1'):
        NAME =input("ENTER THE NAME:")
        ACTOR = input("NAME OF THE ACTORS:")
        ACTRESS =input("NAME OF THE ACTRES:")
        DIRECTOR = input("NAME OF THE DIRECTOR:")
        YEAR = input("YEAR:")
        h.execute(f'INSERT INTO MOVIES VALUES("{NAME}","{ACTOR}","{ACTRESS}","{DIRECTOR}","{YEAR}");')
        h.commit()
    elif(Di == '3'):
        print("(NAME, ACTOR, ACTRESS, DIRECTOR, YEAR)")
        for me in h.execute("SELECT * FROM MOVIES;"):
            for he in me:
                print(he +" | ", end='')
                print()
    elif(Di == '2'):
        he = input("COLUMN NAME:")
        d = input("ENTER VALUES:")
        print("(NAME, ACTOR, ACTRESS, DIRECTOR, YEAR)")
        for me in h.execute(f'SELECT * FROM MOVIES WHERE {he}={d}";'):
            print(me)