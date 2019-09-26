
import csv

hypo = ['%','%','%','%','%','%']

csv_file = open('/home/niktwister/training_examples.csv')

readcsv = csv.reader(csv_file,delimiter=',')

data = []

print('The training examples are :')

for row in readcsv:
    print(row)
    if row[len(row)-1].upper()=='YES':
        data.append(row)
        
print('positive training examples are :')

for x in data:
    print(x)

print('the steps of FIND-S algorithm are :\n',hypo)
    
trainingexamples = len(data)
noofattr = len(data[0])-1

for i in range(trainingexamples):
    for k in range(noofattr):
        if hypo[k]=='%':
            hypo[k] = data[i][k]
        elif hypo[k]!=data[i][k]:
            hypo[k]='?'
    print(hypo)

print('The maximally specific FIND-S hypothesis for the given training examples is ')
print(hypo)
            
            
            
            
            
            
            
            
            
            
            
            
            
            