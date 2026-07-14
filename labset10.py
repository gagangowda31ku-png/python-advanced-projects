# labset 10
'''
 Develop Data Summary Generator:
  Read a CSV file (like COVID data or weather stats), convert to dictionary form, 
 and allow the user to run summary queries: max, min, average by column. 
'''

import csv

def read_csv(filename):
    data = []
    with open(filename,'r') as file:
        reader = csv.DictReader(file)
        print(reader)
        for row in reader:
            data.append(row)
    return data

def get_column(data,column):
    values = []
    for row in data:
        try:
            values.append(float(row[column]))
        except Exception as e:
            print(f"error : {e}")

    return values

def get_max(values):
    return max(values)
def get_min(values):
    return min(values)
def get_mean(values):
    return sum(values)/len(values)



filename = input("Enter the CSV filename name: ")
data = read_csv(filename)
cols = list(data[0].keys())
print("Available columns: ",cols)
column = input("Enter the column anme for analysis: ")
values = get_column(data,column)

if not values:
    print("No numeric data in available in this column")

print("Max :",get_max(values))
print("MIn: ",get_min(values))
print('Mean: ',get_mean(values))
