import streamlit as st
import mysql.connector
import time
import numpy as np
import pandas as pd
from random_text import *
import tqdm


@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])


conn = init_connection()


def main():
    cursor = conn.cursor()
    st.title("My AI Assignment 3 & 4 🤖")
    st.write(
        "##### This asssignment generates random names and numbers and stores it into Database")

    st.write("### How many entries do you want?")
    entries = st.text_input('No. of entries', ' ')

    try:
        entries = int(entries)
        st.write("No. of entries generated are", entries)
        create_data(entries)
        array = np.array(pd.read_csv(f'data_{entries}.csv'))

        query = """INSERT INTO AI_assignment (Name, Phone_Number) VALUES (%s, %s)"""
        data = []
        for element in array:
            data.append((element[0], element[1]))
        # query = "INSERT INTO AI_assignment (Name, Phone_Number) VALUES " + \
        #     ",".join("(%s, %s)" for _ in data)
        # flattened_values = [item for sublist in data for item in sublist]
        cursor.executemany(query, data)  # flattened_values)
        conn.commit()
        st.write("Data Inserted")
    except ValueError:
        pass
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    cursor.execute("SELECT * from AI_assignment;")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['Name', 'Phone_number'])
    # Print results.
    st.dataframe(df)


if __name__ == "__main__":
    main()
