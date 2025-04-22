#Dictionary set
DSET = {
    'key1': 'value1',
     'key2': 'value2',
     'key3': 'value3',
     "age":23,
     "name":{"first":"usama","last":"jamshed"}
}
DSET['key3'] = 'value4'
print(DSET)
#nested dictionary
dic={
    "name":{"first":"usama","last":"jamshed"},
    "age":23
}
print(dic["name"]["first"])
print(dic["name"]["last"])
print(dic.keys())
print(dic.values())
print(dic.items())
dic["age"] = 24
print(dic)  
dic["city"] = "Karachi"  # adding a new key-value pair
print(dic)
#set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))
set1.add(9)  # adding an element to set1
print(set1) 
set1.remove(9)  # removing an element from set1
print(set1)
# Dictionary comprehension example
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict)

