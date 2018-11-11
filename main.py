# Modules
import os
import csv

electiondataCSV = os.path.join('resources','election_data.csv')

rows = 0
voter_id = []
county = []
candidate = []
total_voters = []
unique_candidates = []
Khan = []
Correy = []
Li =[]
O_Tooley = []

with open(electiondataCSV, 'r') as electiondata:
    csv_reader = csv.reader(electiondata)

    header = next(csv_reader)

    for row in csv_reader:
        total_voters.append(row[0])
        candidate.append(str(row[2]))

    for i in candidate:
        if not i in unique_candidates:
            unique_candidates.append(i)  

    for name in candidate:
        if name == "Khan":
            Khan.append(name)
        elif name == "Correy":
            Correy.append(name)
        elif name == "Li":
            Li.append(name)
        elif name == "O'Tooley":
            O_Tooley.append(name)


    khan_percentage = round(((len(Khan)/len(total_voters))*100),2)  
    correy_percentage = round(((len(Correy)/len(total_voters))*100),2)  
    li_percentage = round(((len(Li)/len(total_voters))*100),2)  
    o_tooley_percentage = round(((len(O_Tooley)/len(total_voters))*100),2)  



print("Election Results")   
print("------------------------")       
print("Total Voters:",len(total_voters))  
print("------------------------")
print(f"Khan: {khan_percentage}% ({len(Khan)})")
print(f"Correy: {correy_percentage}% ({len(Correy)})")
print(f"Li: {li_percentage}% ({len(Li)})")
print(f"O'Tooley: {o_tooley_percentage}% ({len(O_Tooley)})")
print("------------------------")
          
if khan_percentage > correy_percentage and khan_percentage > li_percentage and khan_percentage > o_tooley_percentage:
        print("Winner: Khan")
if correy_percentage > khan_percentage and correy_percentage > li_percentage and correy_percentage > o_tooley_percentage:
        print("Winner: Correy")
if li_percentage > khan_percentage and li_percentage > correy_percentage and li_percentage > o_tooley_percentage:
        print("Winner: Li")
if o_tooley_percentage > khan_percentage and o_tooley_percentage > correy_percentage and o_tooley_percentage > li_percentage:
        print("Winner: O'Tooley")

print("------------------------")
