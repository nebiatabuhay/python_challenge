import csv
import os
import numpy as np
project_file = os.path.join("resources","budget_data.csv")
#print=(project_file)
project_file2write = os.path.join("analysis", "budget_result.txt")
print(os.path.exists(project_file2write))
month_count = 0
profit_changes_list = []
total_netamount_list = []
#total_netamount = ("profit")
#total_netamount = ("losses")
#entire_changes = ("profit", "losses")
#average_change = 0
#date_amount = (max_profit_loss)
#date_amount = (min_profit_loss)
greatest_increase_profits = 0
greatest_increase_date = ""
greatest_decrease_losses = 99999999
greatest_decrease_date = ""

with open (project_file) as csv_file:
  csv_reader = csv.reader(csv_file)
  header = next(csv_reader)
  first_time = True     
  for data_row in csv_reader:
    #Jan-2010,867884
    #print(data_list)
    month_count = month_count + 1
    profit_loss = int(data_row[1])
    total_netamount_list.append(profit_loss)
    if first_time:
      profit_diff = 0
    else:
      profit_diff = profit_loss - profit_loss_previous
      profit_changes_list.append(profit_diff)
      if profit_diff > greatest_increase_profits:
        greatest_increase_profits = profit_diff
        greatest_increase_date = data_row[0]
      if profit_loss < greatest_decrease_losses:
         greatest_decrease_losses = profit_loss
         greatest_decrease_date = data_row[0]


    first_time = False
    profit_loss_previous = profit_loss
  
    #if i > 1:
    #average_change = average_change + (int(data[i][2]) 
    #total_netamount_profit = < int(data[i][2]):
    #total_netamount_loss < int(data[i][2]):
    #average_change = (month_sum / entire_changes
    #date_amount (max_profit_loss) =
#average_change = sum(profit_changes_list) / len(profit_changes_list)
#average_change_2 = np.mean(profit_changes_list)
#greatest_increase_profits = total_netamount_profit - date_amount (max_profit_loss)
#greatest_decrease_losses = total_netamount_loss - date_amount (max_profit_loss)

#print(sum(total_netamount_list))
#print(sum(profit_changes_list))
#print(len(profit_changes_list))
#print(average_change)
#print(average_change_2)
#print(greatest_increase_profits)
#print(greatest_decrease_losses)
#print(greatest_increase_profits)
#print(greatest_increase_date)
#print(greatest_decrease_losses)
#print(greatest_decrease_date)