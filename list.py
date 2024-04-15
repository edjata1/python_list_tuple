print('============= list =============')
users = ['Peter', 'Empress', 'En', 'Na']

data = ['Empress', 42, True]

emptylist = []

print("============= what\n's in the list =============")

print("Empress" in users)
print("Empress" in emptylist)
print("Empress" in data)

print(users[0])
print(users[-1])
print(users.index('En'))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))
print(len(users))

print('============= Adding to list =============')
# adding to list
print()
print('*********** append list *************')
users.append('Is')
print(users)

print()
print('*********** += list *************')
users += ['Jason', 'Jack', 'Sara', 'Jill']
print(users)

print()
print('*********** extend list *************')
users.extend(['Rob', 'Bill', 'Steve', 'Tom'])
print(users)

# adding a list to a list
# users.extend(data)
# print(users)
print()
print('*********** insert list *************')
users.insert(0, 'Bobby')
print(users)

print()
print('*********** [2:2] slice *************')
users[2:2] = ['Albert', 'Eddie']
print(users)

print()
print('*********** [1:3] replaced *************')
users[1:3] = ['Mimee', 'Kiki']
print(users)

print()
print('*********** Removing list *************')
users.remove('Bobby')
print(users)

print()
print(users.pop())
print()
print(users)
print()

del users[0]
print(users)

# del data
data.clear()
print(data)

print()
print('*********** reverse list *************')
nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)
# print()

print()
print('*********** sort list *************')
print(users.sort())
print(users)

users[1:2] = ['dave']
users.sort()
print(users)

print()
users.sort(key=str.lower)
print(users)

print()
print('*********** sorted list *************')
print(sorted(nums, reverse=True))
print(nums)

print()
print('*********** copy list *************')
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
numscopy.sort()
print(numscopy)

print(mynums)
mynums.sort()
print(mynums)

print(mycopy)
mycopy.sort()
print(mycopy)

print(nums)
nums.sort()
print(nums)

print(type(nums))
print(type(numscopy))
print(type(mynums))
print(type(mycopy))



print()
print('*********** create list *************')
mylist = list([1, "Neil", True]) # explicit list
print(mylist)

print()
print('*********** tuples *************')
# like list, BUT data will not change and the order will not change
mytuple = tuple(('Dave', 42, True)) # with constructor
anothertuple = (1, 4, 2, 8, 2, 2, 2, 2) # without constructor

print(mytuple)
print(type(mytuple))
print(anothertuple)
print(type(anothertuple))

print()
print('*********** copy tuples *************')
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)
print()

print(" ------ Not adding 'Empress' ")
copytuple = mytuple
print(copytuple)
copytuple.__add__(tuple(['Empress']))
print(copytuple)

print()
print('*********** unpack tuples *************')
(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)
print()

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print()
print('*********** check methods on tuple *************')
print(data.count(2))
print(data.count(0))

# print(anothertuple.count())
print(anothertuple)
print(anothertuple.count(1))
print(anothertuple.count(2))


