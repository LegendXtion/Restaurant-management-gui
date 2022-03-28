f = open('catalog.txt', 'r')
data = f.readlines()
f.close()

Item_code = 1001
C_DATA = {}

for i in data:
	name, price, qty = i.split(",")
	C_DATA[Item_code] = {'name':name, 'price':price, 'qty':qty}
	Item_code+=1

