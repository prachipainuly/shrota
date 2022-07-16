import sqlite3

from read_single_frames import get_handpoints_from_singleframe

def updateSqliteTable(data):
    try:
        sqliteConnection = sqlite3.connect('sign_language_gestures.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """INSERT INTO signs(gesture, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12,
        x13, x14, x15, x16, x17, x18, x19, x20,
        y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12,
        y13, y14, y15, y16, y17, y18, y19, y20,
        z0, z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12,
        z13, z14, z15, z16, z17, z18, z19, z20) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

#updateSqliteTable()

datapath = "C:/Users/jenss/Desktop/ASL_alphabet/"

dataset_names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

dataset_paths = []

for i in range(len(dataset_names)):
    dataset_paths.append(datapath + dataset_names[i] + ".png")
    res = get_handpoints_from_singleframe(dataset_paths[i])
    updateSqliteTable(([dataset_names[i].upper()] + res[0] + res[1] + res[2]))

