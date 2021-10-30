# accessing the sqlite3 module
import sqlite3

# Creating a Connection to the Database
connection = sqlite3.connect('Moviesdatabase.db')

# obtaining a cursor object to facilitate operations on our database
cursor = connection.cursor()
cursor.execute("CREATE TABLE Movies (name TEXT, actor TEXT, actress TEXT, director TEXT, year_of_release INTEGER)")

# inserting rows of data
cursor.execute("INSERT INTO Movies VALUES ('Zindagi Na Milegi Dobara', 'Hrithik Roshan', 'Katrina Kaif', 'Zoya Akhtar', 2011)")
cursor.execute("INSERT INTO Movies VALUES ('Bajirao Mastani', 'Ranveer Singh', 'Deepika Padukone', 'Sanjay Leela Bhansali', 2015)")
cursor.execute("INSERT INTO Movies VALUES ('Shershaah', 'Sidharth Malhotra', 'Kiara Advani', 'Vishnuvardhan', 2021)")

# retrieving all the values from the database
rows = cursor.execute("SELECT name, actor, actress, director, year_of_release FROM Movies").fetchall()
print(rows)

# retrieving all the values from the database with a condition
target_actor = "Sidharth Malhotra"
rows2 = cursor.execute("SELECT name, actor, actress, director, year_of_release FROM Movies WHERE actor = ?", (target_actor, ), ).fetchall()
print(rows2)
