from tkinter import *
from extract_transaction import T_DATA
from tkinter.messagebox import showinfo
from extract_catalog import C_DATA
import datetime

def showCatalog():
	cat_win = Toplevel()
	cat_win.wm_title('Catalog')
	Label(master=cat_win, text='Item', width=15, fg='green', bg='yellow').grid(row=0, column=0)
	Label(master=cat_win, text='Quantity', width=15, fg='green', bg='yellow').grid(row=0, column=1)
	Label(master=cat_win, text='Rate', width=15, fg='green', bg='yellow').grid(row=0, column=2)

	for c,i in enumerate(C_DATA.keys()):
		Label(master=cat_win, text=C_DATA[i]['name'], width=15, fg='blue').grid(row=c+1, column=0)

	for c,i in enumerate(C_DATA.keys()):
		Label(master=cat_win, text=C_DATA[i]['qty'], width=15, fg='purple').grid(row=c+1, column=1)
	
	for c,i in enumerate(C_DATA.keys()):
		Label(master=cat_win, text='₹ '+C_DATA[i]['price'], width=15, fg='red').grid(row=c+1, column=2)
	
	
def placeOrder():
	date_time= datetime.datetime.now()
	date = str(date_time.date())
	time = str(date_time.time())
	status = 'Success'
	amt = sum(su)
	with open('transaction.txt', 'a') as trans:
		trans.write(f'{date},{time},{amt},{status}\n')
	
	showinfo('Confirmation', 'Order Placed Successfully')
	
	[i.e.delete(0,3) for i in Items_Class]
	[i.e.insert(0, 0) for i in Items_Class]

	place_order_button.config(state='disabled')

def transactionHistory():
	tra_win = Toplevel()
	tra_win.wm_title('History')
	Label(master=tra_win, text='Date', width=15, fg='green', bg='yellow').grid(row=0, column=0)
	Label(master=tra_win, text='Time', width=15, fg='green', bg='yellow').grid(row=0, column=1)
	Label(master=tra_win, text='Amount', width=15, fg='green', bg='yellow').grid(row=0, column=2)
	Label(master=tra_win, text='Status', width=15, fg='green', bg='yellow').grid(row=0, column=3)

	for c,i in enumerate(T_DATA.keys()):
		Label(master=tra_win, text=T_DATA[i]['date'], width=15, fg='blue').grid(row=c+1, column=0)

	for c,i in enumerate(T_DATA.keys()):
		Label(master=tra_win, text=T_DATA[i]['time'], width=15, fg='purple').grid(row=c+1, column=1)
	
	for c,i in enumerate(T_DATA.keys()):
		Label(master=tra_win, text='₹ '+T_DATA[i]['amt'], width=15, fg='red').grid(row=c+1, column=2)

	for c,i in enumerate(T_DATA.keys()):
		Label(master=tra_win, text=T_DATA[i]['status'], width=15, fg='red').grid(row=c+1, column=3)


def calculate():
	global su
	su = [it.value.get()*int(C_DATA[it.item_code]['price']) for it in Items_Class]
	amt_label.config(text='Amount Payable: '+str(sum(su)))
	if sum(su)>0:
		place_order_button.config(state='active')

window = Tk()
window.title('Restaurants Management')

class Item:
	def __init__(self, r, item):
		Label(master=window, text=C_DATA[item]['name']+' - '+C_DATA[item]['qty'], fg='blue', anchor='w', width=20).grid(row=r, column=0)

		self.item_code = item
		self.value = IntVar()
		self.e = Entry(master=window, width=2, textvariable=self.value, fg='red', state='normal')
		self.e.grid(row=r, column=1)
		
		b = Button(master=window, text='+', command=self.addQty, bg='cyan')
		b.grid(row=r, column=2)

	def addQty(self):
		v = self.value.get()+1
		self.e.delete(0, 3)
		self.e.insert(0, v)

Items_Class = []
rc = 0
for item in C_DATA.keys():
	Items_Class.append(Item(r=rc, item=item))
	rc+=1


calculate_button = Button(master=window, text='Calculate Amount', command=calculate, bg='yellow', fg='red')
calculate_button.grid(row=rc, column=0, columnspan=2)

Label(master=window, text=' ').grid(row=0, column=4, rowspan=rc)

show_catalog_button = Button(master=window, text='Catalog', command=showCatalog, bg='yellow', fg='green', width=20)
show_catalog_button.grid(row=0, column=5)

transaction_history = Button(master=window, text='View Transaction History', command=transactionHistory, bg='yellow', fg='green', width=20)
transaction_history.grid(row=1, column=5)

amt_label = Label(master=window, text='Amount Payable: ', fg='dark green')
amt_label.grid(row=4, column=5)

place_order_button = Button(master=window, text='Place Order', command=placeOrder, bg='orange', fg='red', state='disabled')
place_order_button.grid(row=5, column=5)

window.mainloop()
