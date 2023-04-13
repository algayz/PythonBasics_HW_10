import random, pprint

lst = ['robot'] * 5
lst += ['human'] * 5
lst += ['animal'] * 5
random.shuffle(lst)

data = {'whoAmI' : lst}
pprint.pprint(data['whoAmI'])
print() 

cat = set(data['whoAmI'])
pprint.pprint(cat)
print()

onehot_encode = [{z: 0 for z in cat} for x in range(len(data['whoAmI']))]

for item in enumerate(data['whoAmI']):
	onehot_encode[item[0]][item[1]] = 1

pprint.pprint (onehot_encode)