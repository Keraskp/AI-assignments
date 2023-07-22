import random
import string
import numpy as np
import pandas as pd
import mysql.connector

from generate_text import *

def get_random_string(n=15):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

def get_random_number(n=8):
    start = 10**(n-1)
    end = (10**n)-1
    return random.randint(start, end)

def main(num_entries):

    cnx = mysql.connector.connect(user='root', password='@Ditya1601',
                                  host='127.0.0.1', database='college', port=3306)
    cursor = cnx.cursor()

    
    entries = num_entries

    try:
        entries = int(entries)
        print("No. of entries generated are", entries)
        create_data(entries)
        array = np.array(pd.read_csv(f'data_{entries}.csv'))

        query = """INSERT INTO AI_assignment (Name, Phone_Number) VALUES (%s, %s)"""
        data = []
        for element in array:
            data.append((element[0], element[1]))

        cursor.executemany(query, data)  
        cnx.commit()

        print("Data Inserted")

    except ValueError:
        pass
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    cursor.execute("SELECT * from AI_assignment;")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['Name', 'Phone_number'])
    print(df)



if __name__ == "__main__":
    main(100000000)