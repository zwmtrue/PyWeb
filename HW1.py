import re
'''
sum_actual = 0
with open('regex_sum_266067.txt','r') as actual:
    for line in actual:
        numbers=re.findall('[0-9]+',line)
        if len(numbers)!=0:
            sum_actual+=sum([int(items) for items in numbers])

print sum_actual
'''
x = { "id" : "001",
  "x" : "2",
  "name" : "Chuck"
}
print x,type(x)