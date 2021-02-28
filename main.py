import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")


Total_Months = 0
Profit_Losses = 0
Monthly_Change = []
Dataset_Month = []
Greatest_Increase = 0
Inc_Month = 0
Greatest_Decrease = 0
Dec_Month = 0


csvfile= open(csvpath)
csvreader = csv.reader(csvfile, delimiter=",")


header= next(csvreader)
row = next(csvreader)

Previous_Amount = int(row[1])
Total_Months += 1
Profit_Losses += int(row[1])
Greatest_Increase = int(row[1])
Inc_Month = row[0]
    

for row in csvreader:
        Total_Months += 1
        Profit_Losses += int(row[1])
        Change_Amount = int(row[1]) - Previous_Amount
        Monthly_Change.append(Change_Amount)
        Previous_Amount = int(row[1])
        Dataset_Month.append(row[0])
        

        if int(row[1]) > Greatest_Increase:
            Greatest_Increase = int(row[1])
            Inc_Month=row[0]
            

        if int(row[1]) < Greatest_Decrease:
            Greatest_Decreasev = int(row[1])
            Dec_Month = row[0]  
        
  
        Average_Change = sum(Monthly_Change)/ len(Monthly_Change)
    
        Highest = max(Monthly_Change)
        Lowest = min(Monthly_Change)


print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Profit_Losses}")
print(f"Average Change: ${Average_Change:.2f}")
print(f"Greatest Increase in Profits:, {Inc_Month}, (${Highest})")
print(f"Greatest Decrease in Profits:, {Dec_Month}, (${Lowest})")


output_file = os.path.join('Resources', 'budget_data_Analysis.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {Total_Months}\n")
    txtfile.write(f"Total: ${Profit_Losses}\n")
    txtfile.write(f"Average Change: ${Average_Change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {Inc_Month}, (${Highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {Dec_Month}, (${Lowest})\n")
