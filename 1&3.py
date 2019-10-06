/////////////////////////1st Pgm///////////////////////////////////////////////////

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


/////////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////3rd pgm/////////////////////////////////////////////////



import pandas as pd
#from pandas import DataFrame
df_tennis = pd.read_csv('/home/niktwister/tennis.csv')
print("\n Given Play Tennis Data Set:\n\n",df_tennis)
def entropy(probs):
    import math
    return sum( [-prob*math.log(prob, 2) for prob in probs] )

#Function to calulate the entropy of the given Data Sets/List with respect to target attributes
def entropy_of_list(a_list):
    from collections import Counter
    cnt = Counter(a_list)   # Counter calculates the propotion of class
    num_instances = len(a_list)   # = 14
    probs = [x / num_instances for x in cnt.values()]  # x means no of YES/NO
    return entropy(probs) # Call Entropy :
total_entropy = entropy_of_list(df_tennis['PlayTennis'])
print("\n Total Entropy of PlayTennis Data Set:",total_entropy)
def information_gain(df, split_attribute_name, target_attribute_name, trace=0):
    df_split = df.groupby(split_attribute_name)
    for name,group in df_split:
        nobs = len(df.index)
    df_agg_ent = df_split.agg({target_attribute_name : [entropy_of_list, lambda x: len(x)/nobs] })[target_attribute_name]
    df_agg_ent.columns = ['Entropy', 'PropObservations']#x = lambda a, b: a * b
    if trace: # helps understand what fxn is doing:     #print(x(5, 6))
        print(df_agg_ent)
    # Calculate Information Gain:
    new_entropy = sum( df_agg_ent['Entropy'] * df_agg_ent['PropObservations'] )
    old_entropy = entropy_of_list(df[target_attribute_name])
    return old_entropy - new_entropy
print('Info-gain for Outlook is :'+str( information_gain(df_tennis, 'Outlook', 'PlayTennis')),"\n")
print('\n Info-gain for Humidity is: ' + str( information_gain(df_tennis, 'Humidity', 'PlayTennis')),"\n")
print('\n Info-gain for Wind is:' + str( information_gain(df_tennis, 'Wind', 'PlayTennis')),"\n")
print('\n Info-gain for Temperature is:' + str( information_gain(df_tennis, 'Temperature','PlayTennis')),"\n")
def id3(df, target_attribute_name, attribute_names, default_class=None):

    ## Tally target attribute:
    from collections import Counter
    cnt = Counter(df[target_attribute_name])# class of YES /NO

    ## First check: Is this split of the dataset homogeneous?
    if len(cnt) == 1:
        return next(iter(cnt))  # next input data set, or raises StopIteration when EOF is hit.
    elif df.empty or (not attribute_names):
        return default_class  # Return None for Empty Data Set
    else:
        default_class = max(cnt.keys()) #No of YES and NO Class
        gainz = [information_gain(df, attr, target_attribute_name) for attr in attribute_names] #
        index_of_max = gainz.index(max(gainz)) # Index of Best Attribute
        best_attr = attribute_names[index_of_max]
        tree = {best_attr:{}} # Iniiate the tree with best attribute as a node
        remaining_attribute_names = [i for i in attribute_names if i != best_attr]
        for attr_val, data_subset in df.groupby(best_attr):
            subtree = id3(data_subset,
                        target_attribute_name,
                        remaining_attribute_names,
                        default_class)
            tree[best_attr][attr_val] = subtree
        return tree
attribute_names = list(df_tennis.columns)
attribute_names.remove('PlayTennis') #Remove the class attribute
from pprint import pprint #pprint means preety print.
tree = id3(df_tennis,'PlayTennis',attribute_names)
print("\n\nThe Resultant Decision Tree is :\n")
#print(tree)
pprint(tree)

/////end of prog 4 /////////
