import math
import sqlite3

#from Machine_learning.read_single_frames import get_handpoints_from_singleframe

def getVectoryFromDatabase(letter):
    try:
        sqliteConnection = sqlite3.connect('sign_language_gestures.db')
        cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")

        sql_update_query = """SELECT * from signs WHERE gesture = (?) """
        cursor.execute(sql_update_query, letter)
        rows = cursor.fetchall()
        res = []
        for row in rows:
            # print(row)
            # print(list(row[1:22]))
            # print(list(row[22:43]))
            # print(list(row[43:64]))
            res.append( list(row[1:22]))
            res.append( list(row[22:43] ))
            res.append ( list(row[43:64]))
        # print("Record Updated successfully ")
        cursor.close()
        return res

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def calculate_distance_from_two_frames(vector1, vocabluary):
    ## At first we normalize the vector to landmark of writs (x/y/z_zero)
    x_zero = vector1[0][0]
    y_zero = vector1[1][0]
    z_zero = vector1[2][0]

    ## We also get the handsize to normalize points to hand_size
    handsize_reference = math.sqrt(
        (x_zero - vector1[0][5]) ** 2 + (y_zero - vector1[1][5]) ** 2 + (z_zero - vector1[2][5]) ** 2)

    ## Now based on the handsize_reference we can normalize landmarks to hand size

    for j in range(20):
        vector1[0][j + 1] = (vector1[0][j + 1] - x_zero) / handsize_reference
        vector1[1][j + 1] = (vector1[1][j + 1] - y_zero) / handsize_reference
        vector1[2][j + 1] = (vector1[2][j + 1] - z_zero) / handsize_reference


    ## Now we get the handmark vectors from our database:
    res = getVectoryFromDatabase(vocabluary)
    vector_from_database_x = res[0]
    vector_from_database_y = res[1]
    vector_from_database_z = res[2]

    print(len(vector_from_database_x))
    print(len(vector_from_database_y))
    print(len(vector_from_database_z))

    x_zero = vector_from_database_x[0]
    y_zero = vector_from_database_y[0]
    z_zero = vector_from_database_z[0]
    # # We do the same as above with  vectors from database:
    handsize_reference_database = math.sqrt(
        (vector_from_database_x[0] - vector_from_database_x[5]) ** 2 + (vector_from_database_y[0] - vector_from_database_y[5]) ** 2 +
        (vector_from_database_z[0] - vector_from_database_z[5]) ** 2)

    ## Now based on the handsize_reference we can normalize landmarks to hand size

    for j in range(20):
        vector_from_database_x[j + 1] = (vector_from_database_x[j + 1] - x_zero) / handsize_reference_database
        vector_from_database_y[j + 1] = (vector_from_database_y[j + 1] - y_zero) / handsize_reference_database
        vector_from_database_z[j + 1] = (vector_from_database_z[j + 1] - z_zero) / handsize_reference_database


    ## Now we calculate for each handpoint the difference
    diff1 = 0
    for i in range(20):
        ## for each landmark_point we compare difference:
        diff1 = diff1 +  math.sqrt((vector1[0][i + 1] - vector_from_database_x[i + 1]) ** 2 +
                           (vector1[1][i + 1] - vector_from_database_y[i + 1]) ** 2 +
                           (vector1[2][i + 1] - vector_from_database_z[i + 1]) ** 2)
        print(diff1)


    ## Now we can finally return the difference!
    return diff1


#getVectoryFromDatabase('A')

# vector_for_letter_a_x = [0.415635347366333, 0.44734546542167664, 0.4632556438446045, 0.46720176935195923,0.4716016948223114, 0.4472196400165558, 0.45328840613365173, 0.45029348134994507,0.4463890492916107, 0.42642131447792053, 0.43301692605018616, 0.4308911859989166,0.4288635551929474, 0.4051017165184021, 0.41283077001571655, 0.4122315049171448,0.4104270339012146, 0.3816864490509033, 0.3907229006290436, 0.3943542540073395,0.3943181037902832]
# vector_for_letter_a_y = [0.47500044107437134, 0.4434950053691864, 0.4005970060825348, 0.36401888728141785,0.3349454998970032, 0.3719223439693451, 0.3538094758987427, 0.3845536708831787,0.4067535698413849, 0.3730696737766266, 0.3565751612186432, 0.3922598958015442,0.40819263458251953, 0.3782212734222412, 0.3639320433139801, 0.3964857757091522,0.40970996022224426, 0.38706347346305847, 0.3736375570297241, 0.39594152569770813,0.4064430892467499]
# vector_for_letter_a_z = [-2.1831179708442505e-07, -0.007337012328207493, -0.009634657762944698,-0.01323014684021473, -0.01489123422652483, 0.0029733432456851006, -0.014627293683588505,-0.02394128404557705, -0.026487048715353012, 0.0012474232353270054, -0.015369277447462082,-0.0180810634046793, -0.015767602249979973, -0.003712201025336981, -0.020756220445036888,-0.015632545575499535, -0.007425137795507908, -0.009314264170825481, -0.017032409086823463,-0.010223452933132648, -0.00243140640668571]
#
# print(len(vector_for_letter_a_x))
# print(len(vector_for_letter_a_y))
# print(len(vector_for_letter_a_z))
#
# res = calculate_distance_from_two_frames([vector_for_letter_a_x, vector_for_letter_a_y, vector_for_letter_a_z], 'A')
#
# print(res)
