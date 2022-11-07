import random
print ("Question 1")
qu1 = ''
li1 = []
while qu1 != '-1':
  qu1 = input('enter element to add to list: ')
  if qu1 != '-1':
    li1.append(qu1)
    print(li1)
  elif qu1 == '-1':
    print(qu1,'equals -1 did not add to list')
    
li2 = ['apple','bannana','lemons','oranges','strawberry','avocado',]
print ("Question 2")
for i in li2:
  #print('current i is',i)
  #print('checking i[0]',i[0])
  if i[0] == 'a' :
    print(i)
  elif i[0] != 'a' :
    print('the element does not exist')

print ("Question 3")
in3 = input('Enter string for question 3: ')
ds = '$'
newli3 = []
endstr = ''
def q3():
  li3 = in3.split()
  for i in li3:
    newi = ds + i
    newli3.append(newi)
  endstr = ' '.join(newli3)
  print (endstr)
q3()

print ("Question 4")
li4 = ['hey','yeo','yuh','yes',]
def q3(li,el):
  #print('el is',el)
  for i in li:
    #print('current i is',i)
    for x in i:
      #print('current x is',x)
      if x == el:
        print('True')
      elif x != el:
        print('False')
q3(li4,input('enter element to search for in: '))

print ("Question 5")
ui = 'yes'
while ui[0] == 'y':
  a = []
  for i in range(0,100):
    r = random.randint(0,1)
    a.append(r)
  print(a)
  ui= input('Generate New Set Of Numbers y/n? ')


print ("Question 6")
li6 = []
for i in range(0,10):
  r = random.randint(0,10)
  li6.append(r)
def sumall():
  sa = sum(li6)
  print(sa,'is the sum of all elements in',li6)
sumall()