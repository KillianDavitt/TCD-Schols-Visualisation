import csv

with open('schols.csv', 'r') as f:
    scholar_id = 0
    for line in csv.reader(f, dialect="excel-tab"):
        print("INSERT INTO scholar VALUES('" + str(scholar_id) + "', '" + line[0].strip().replace("'","") + " " + line[1].strip().replace("'","")+ "', '" + line[2].strip().replace("'", "") + "', " + line[3] + ");")
        scholar_id += 1
