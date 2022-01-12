#To import and read excel files
import xlrd
#To connect to MySQL Workbench
import mysql.connector

#Opens the excel file
book = xlrd.open_workbook("PASTE_YOUR_FILE_PATH_HERE")

# To look at Sheet one only and nothing else
sheet = book.sheet_by_name("Sheet1")

# Establish a MySQL connection
database = mysql.connector.connect (host="LOCALHOST", user = "root", passwd = "", db = "Capstone")

# Get the cursor to read the data line by line
cursor = database.cursor()

query = """INSERT INTO PLANT (FILE_NAME, PLANT, DIST_Km, MAX_Sv, MEAN_Sv, MIN_Sv, MAX_mSv, MEAN_mSv, MIN_mSv, MAX_uSv, MEAN_uSv, MIN_uSv, LENGTH_Km) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Create a for loop 
for r in range(1, sheet.nrows):
		FILE_NAME		    = sheet.cell(r,0).value
		PLANT	  = sheet.cell(r,1).value
		DIST_Km		  = sheet.cell(r,2).value
		MAX_Sv	  = sheet.cell(r,3).value
		MEAN_Sv		  = sheet.cell(r,4).value
		MIN_Sv	  = sheet.cell(r,5).value
		MAX_mSv	  = sheet.cell(r,6).value
		MEAN_mSv	  = sheet.cell(r,7).value
		MIN_mSv	  = sheet.cell(r,8).value
		MAX_uSv	  = sheet.cell(r,9).value
		MEAN_uSv	  = sheet.cell(r,10).value
		MIN_uSv	= sheet.cell(r,11).value
		LENGTH_Km= sheet.cell(r,12).value

		# Assign values from each row
		values = (FILE_NAME, PLANT, DIST_Km, MAX_Sv, MEAN_Sv, MIN_Sv, MAX_mSv, MEAN_mSv, MIN_mSv, MAX_uSv, MEAN_uSv, MIN_uSv, LENGTH_Km)

		#Execute SQL Query
		cursor.execute(query, values)

#Close cursor
cursor.close()

#Commit transaction
database.commit()

#Close database connection
database.close()