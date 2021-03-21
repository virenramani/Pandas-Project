import csv
import openpyxl 
import pandas as pd
import numpy as np
from openpyxl import load_workbook

csv_reader = pd.read_excel('C:/Users/viren/Desktop/GUS_Project/Udemy/Udemyxl.xlsx')
csv_reader[['T1','T2','T3','T4','T5','T6']] = csv_reader['Hard_skills'].apply(lambda x: pd.Series(str(x).strip('"]').strip('["').replace('", "', ', ').split(',', 5)))
csv_reader[['SSB1','SSB2','SSB3','SSB4','SSB5']] = csv_reader['Soft_skills'].apply(lambda x: pd.Series(str(x).strip('"]').strip('["').replace('", "', ', ').split(',', 4)))
df = csv_reader.rename(columns={'ID': 'Document ID', 'Course_name': 'Unit Name', 'Course_rating': 'Unit Rating',\
                'Course_duration': 'Unit Duration', 'Course_description':'Unit description', 'Difficulty_level': 'Expertise level','Total_enrollments':'Total enrolled', \
                'URL':'Referral Unit URL','Certifications':'CT1','Course_content':'Course Content','Image_link':'Image Link'})

df_excel = pd.read_excel('C:/Users/viren/Desktop/GUS_Project/Annotation Template VUdemy.xlsx',sheet_name='Annotation')
result = pd.concat([df_excel, df], ignore_index=True)
result.drop(columns=['Subtitles','Soft_skills','Hard_skills','T6','SSB5','Document ID'], inplace=True)
result['Document ID'] = result.index + 1
cols = result.columns.tolist()
cols = cols[-1:] + cols[:-1]
result1 = result[cols]
result1.to_excel('Annotation Template VUd.xlsx',sheet_name='Annotation', index=False)
print('*******File Saved*******')

# writer = pd.ExcelWriter('Annotation Template V6.xlsx', options = {'strings_to_urls': False}, engine='xlsxwriter')
# result1.to_excel(writer,sheet_name='Annotation', index=False)
# writer.save()