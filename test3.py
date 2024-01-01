import csv
with open('department.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 svensklista = []
 print("ID Department Name")
 print("---------------------------------")
 for row in data:
   svensklista.append(row['department_name'])

for item in svensklista:
  print (item)
  print ("Asim")