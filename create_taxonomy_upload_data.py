import pymysql.cursors
#import mysql.connector
import pandas as pd
import time
import json
######## SQL Connection

# mydb = pymysql.connect(
#   host="",
#   user="",
#   password="",
#   db="",
#   cursorclass=pymysql.cursors.DictCursor
# )

# mycursor = mydb.cursor()
########### Create Table
# mycursor.execute("CREATE TABLE IF NOT EXISTS Taxonomy_v6 ( ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Ref_JD_ID INT, Ref_Skills_ID MEDIUMTEXT, Date_Collected VARCHAR(255), Data_Source VARCHAR(255), Region VARCHAR(255), Industry VARCHAR(255), Industry_Sub_Domain VARCHAR(255), Role VARCHAR(255), Generic_Profile VARCHAR(255), Knowledge_Domain VARCHAR(255), UG VARCHAR(255), PG VARCHAR(255), Doctorate VARCHAR(255), Educational_Institute VARCHAR(255), Soft_Skills_and_Behaviours MEDIUMTEXT, Competencies MEDIUMTEXT, Technical_Skills MEDIUMTEXT, Related_Technical_Skills MEDIUMTEXT, Professional_Certification MEDIUMTEXT, Related_Certifications MEDIUMTEXT, Professional_Certification_Body VARCHAR(255), Key_Skills MEDIUMTEXT, Company_Name VARCHAR(255), Experience VARCHAR(255), Salary VARCHAR(255), Location VARCHAR(255), Vacancies VARCHAR(255), Job_Applicants VARCHAR(255), Posted VARCHAR(255) );") 

######### Select All Data

st = time.time()
  
df = pd.read_excel(r"C:/Users/viren/Desktop/GUS_Project/jobs/DB_IndustryWise_Monster_India1.xlsx")

for index,row in df.iterrows():
    #print(row)
    #string = row['ID'],row['Ref. JD ID'],str(row['Ref. Skills ID']),str(row['Date Collected']),str(row['Source of marketplace']),str(row['Region']),str(row['Industry']),str(row['Industry Sub-Domain']),str(row['Role']),str(row['Generic Role']),str(row['Knowledge Area']),str(row['UG']),str(row['PG']),str(row['Doctorate']),str(row['Education institute']),str(row['Soft Skills'] + "," + row['Behaviour Skills']),str(row['Competencies']),str(row['Hard Skills']),str(row['Related Hard Skills']),str(row['Professional Certification']),str(row['Related Certifications']),str(row['Professional Certification institute']),str(row['Key Skills']),str(row['CompanyName']),str(row['Experience']),str(row['Salary']),str(row['Location']),str(row['Vacancies']),str(row['Job Applicants']),str(row['Posted'])
    # sql = "INSERT INTO Taxonomy_v6 (ID,Ref_JD_ID, Ref_Skills_ID, Date_Collected, Data_Source, Region, Industry, Industry_Sub_Domain, Role, Generic_Profile, Knowledge_Domain, UG, PG, Doctorate, Educational_Institute, Soft_Skills_and_Behaviours, Competencies, Technical_Skills, Related_Technical_Skills, Professional_Certification, Related_Certifications, Professional_Certification_Body, Key_Skills, Company_Name, Experience, Salary, Location, Vacancies, Job_Applicants, Posted) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    val = [((row['ID']),
            (row['Ref_JD_ID']),
            (row['Ref_Skills_ID']),
            (row['Date_Collected']),
            (row['Data_Source']),
            (row['Region']),
            (row['Industry']),
            (row['Industry_Sub_Domain']),
            (row['Role']),
            (row['Generic_Profile']),
            (row['Knowledge_Domain']),
            (row['UG']),
            (row['PG']),
            (row['Doctorate']),
            (row['Educational_Institute']),
            (row['Soft_Skills_and_Behaviours']),
            (row['Competencies']),
            (row['Technical_Skills']),
            (row['Related_Technical_Skills']),
            (row['Professional_Certification']),
            (row['Related_Certifications']),
            (row['Professional_Certification_Body']),
            (row['Key_Skills']),
            (row['Company_Name']),
            (row['Experience']),
            (row['Salary']),
            (row['Location']),
            (row['Vacancies']),
            (row['Job_Applicants']),
            (row['Posted']))]
    print(val)
    try:
        mycursor.executemany(sql, val)
        mydb.commit()
    except:
        print("Row already exist , Please Ignore" , index)
    #print(mycursor.rowcount, "was inserted.")
    print("############" , index)
    


