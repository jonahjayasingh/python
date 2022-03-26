import mysql.connector


link = mysql.connector.connect(
            host = "bciztpfbvw9cwkdabtdq-mysql.services.clever-cloud.com",
            user = "uk2cf58exem1zvij",
            password = "ECpx1kso1QvzQnFko6IK",
            database = "bciztpfbvw9cwkdabtdq"
        )
mycursor = link.cursor()

def into_database(first_name,second_name,password,DOB,user_name):
    print("hi")
    sql = "INSERT INTO sign  (first_name,second_name,username,DOB,Password)\
    VALUES(%s,%s,%s,%s,%s)"
    firstName = first_name.get()
    secondName = second_name.get()
    username = user_name.get()
    dob = DOB.get_date()
    Pass_word = password.get()
    val = (firstName,secondName,username,dob,Pass_word)
    mycursor.execute(sql,val)
    link.commit()
    
def from_database():
    mycursor.execute("SELECT username,Password FROM sign")
    myresult = mycursor.fetchall()
    link.commit()
    return myresult