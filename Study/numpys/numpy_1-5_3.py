import pandas as pd
ser = pd.Series(['a','b','c',3])
print(ser)

print(ser.values)

print(ser.values)

ser2 = pd.Series(['a', 'b', 'c', 3], index=['i','j','k','h'])
print(ser2)


data = {'Region' : ['Korea', 'America', 'Chaina', 'Canada', 'Italy'],
        'Sales' : [300, 200, 500, 150, 50],
        'Amount' : [90, 80, 100, 30, 10],
        'Employee' : [20, 10, 30, 5, 3]
        }
s = pd.Series(data)
print(s)

d = pd.DataFrame(data)
d.columns
d.index
print(d)