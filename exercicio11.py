s = float(input("Digite seu salário"))
if (s <= 280):
    p = 0.2
elif (s <=700):
    p = 0.15
elif (s <= 1500):
    p = 0.1
elif (s >= 1500):
    p = 0.05
a = s * p
print (s)
print (p)
print(s-a)
