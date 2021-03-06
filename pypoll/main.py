import csv
import os
file2load=os.path.join("resources","election_data.csv")
#print(file2load)
file2write =os.path.join("analysis","election_result.txt")
#print(os.path.exists(file2write))
total_number_votes= 0
candidate_list=[]
candidate_dict={}
vote_won = []
votes = []
vote_won_percent = []
with open(file2load) as csv_file:
    csv_reader = csv.reader(csv_file)
    header=next(csv_reader)
    
    for data_row in csv_reader:
        #print(data_row)
        total_number_votes=total_number_votes+1
        candi_name=data_row[2]
        if candi_name not in candidate_list:
            candidate_list.append(candi_name)
            candidate_dict[candi_name]=1
        else:
            candidate_dict[candi_name]=candidate_dict[candi_name]+1

percent_dict = {}
for name in candidate_list:
    #print(name)
    candidate_score = candidate_dict[name]
    percent_score = float(candidate_score)/float(total_number_votes) * 100
    #print(float(candidate_score) / float(total_number_votes))
    percent_dict[name] = percent_score

high_score = 0
winner = ""
for name in candidate_list:
    candidate_score = candidate_dict[name]
    if candidate_score > high_score:
        high_score = candidate_score
        winner = name

print("Election Results")
print("-------------------------")
print("Total Votes: {} ".format(total_number_votes)) 
print("-------------------------")
for name in candidate_list:
    candidate_score = candidate_dict[name]
    candidate_percent = percent_dict[name]
    print("{}: {}% ({})".format(name, round(candidate_percent,3), candidate_score))
print("-------------------------")
print("Winner: {} ".format(winner))
print("-------------------------")

f = open(file2write, "w")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: {} \n".format(total_number_votes)) 
f.write("-------------------------\n")
for name in candidate_list:
    candidate_score = candidate_dict[name]
    candidate_percent = percent_dict[name]
    f.write("{}: {}% ({})\n".format(name, round(candidate_percent,3),candidate_score))
f.write("-------------------------\n")
f.write("Winner: {} \n".format(winner))
f.write("-------------------------\n")
f.close()

