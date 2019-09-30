from swat import CAS 
s = CAS('localhost',8099 ,'sasdemo','sasdemo',protocol='http') 


import sasoptpy as so

m = so.Model(name='candy', session=s) # proc optmodel;
choco = m.add_variable(lb=0, name='choco') # var choco >= 0;
toffee = m.add_variable(lb=0, name='toffee') # var toffee >= 0;
m.set_objective(0.25*choco + 0.75*toffee, # maximize profit =
sense=so.MAX, # 0.25*choco + 0.75*toffee;
name='profit') #
m.add_constraint(15*choco + 40*toffee <= 27000, # con process1:
name='process1') # 15*choco + 40*toffee <= 27000;
m.add_constraint(56.25*toffee <= 27000, # con process2:
name='process2') # 56.25*toffee <= 27000;
m.add_constraint(18.75*choco <= 27000, # con process3:
name='process3') # 18.75*choco <= 27000;
m.add_constraint(12*choco + 50*toffee <= 27000, # con process4:
name='process4') # 12*choco + 50*toffee <= 27000;
result = m.solve() # solve;
print(so.get_solution_table(choco, toffee))



# from swat import CAS 
conn = CAS('localhost', 8099,'sasdemo','sasdemo') 
#tbl = conn.read_excel('C:\\ajps\\_viya\\sasdemohome\\Book1.xlsx')

#C:\Windows\system32>mklink /D c:\home\sasdemo C:\ajps\_viya\sasdemohome
#symbolic link created for c:\home\sasdemo <<===>> C:\ajps\_viya\sasdemohome

#tbl = conn.read_excel('/home/sasdemo/Book1.xlsx')
print(tbl.head())