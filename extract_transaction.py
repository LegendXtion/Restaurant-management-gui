f = open('transaction.txt', 'r')
data = f.readlines()
f.close()

T_DATA = {}
Trans_Id = 101

for i in data:
	date, time, amt, status = i.split(",")
	T_DATA[Trans_Id] = {'date':date, 'time':time, 'amt':amt, 'status':status}
	Trans_Id+=1


