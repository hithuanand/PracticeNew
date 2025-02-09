
data = {1: 'Anand', 2: 'Kiran', 3:'Neha'}
# print(data[1])
print(data)

print(data.get(3))

keys = ['Anand','Kiran','Neha']
values =['Python','java','js']

data1= dict(zip(keys, values))
print(data1)

print(data1['Anand'])

del data1['Kiran']
print(data1)

