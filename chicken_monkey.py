num = range(1,101)

def chicken_monkey(num):
    for i in num:
        if(i % 5 == 0 and i % 7 == 0):
          print('ChickenMonkey', i)
        elif(i % 5 == 0):
          print('chicken', i)
        elif(i % 7 == 0):
          print('monkey', i)

chicken_monkey(num)