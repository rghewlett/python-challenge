# Modules
import os
import csv  

# Path to collect data from the python-challenges/pybank folder
budgetdataCSV = os.path.join('budget_data.csv')

uniq_dates = [] 
rows = 0
p_and_l = []
differences =[]

with open(budgetdataCSV, 'r') as budgetdata:
    csv_reader = csv.reader(budgetdata)

    header = next(csv_reader)

    for row in csv_reader: 
        rows = rows + 1
        if row[0] not in uniq_dates:
            uniq_dates.append(row[0])

            p_and_l.append(int(row[1]))  
            
    for i in range(1,len(p_and_l)):
        differences.append(p_and_l[i] - p_and_l[i-1])

        avg_rev_change = sum(differences)/len(differences)

        max_rev_change = max(differences)

        min_rev_change = min(differences)
       
        max_rev_change_date = str(uniq_dates[differences.index(max(differences))+1])

        min_rev_change_date = str(uniq_dates[differences.index(min(differences))+1])

        

print("Financial Analysis")
print("---------------------------------------------")
print("Total Months:" + str(rows))
print("Net Total: $", + sum(p_and_l))
print("Average Revenue Change: $", + round(avg_rev_change))
print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")




