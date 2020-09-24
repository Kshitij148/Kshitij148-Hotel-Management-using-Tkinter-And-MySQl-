
from tkinter import*
from tkinter.messagebox import*
from tkinter.scrolledtext import*
from PIL import ImageTk,Image
import mysql.connector

import random
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abc123",
  database="hotel"
)


def employee():
	login.deiconify()
	root.withdraw()
print(mydb)

def security():
	try:
		mycursor=mydb.cursor()
		
		un=p10_e1.get()
		a=un
		p=p10_e2.get()
	
		sql='select* from security'
		mycursor.execute(sql)
		data=mycursor.fetchall()
		d=dict(data)
		k=list(d.keys())
		print(k)
		if un in k:
			if d[un]==p:
				p10_e1.delete(0,END)
				p10_e2.delete(0,END)
				login.withdraw()
				employee.deiconify()
				sql='select* from employee_details where ename="%s"'
				mycursor.execute(sql%(un))
				data=mycursor.fetchall()
				l=[p3_e1,p3_e2,p3_e3,p3_e4,p3_e5,p3_e6,p3_e7]
				for i in range(7):
					l[i].delete(0,END)
				p3_e1.insert(0,str(data[0][0]))
				p3_e1.config(state='readonly')
				p3_e2.insert(0,data[0][1])
				p3_e2.config(state='readonly')
				p3_e3.insert(0,str(data[0][2]))
				p3_e3.config(state='readonly')
				p3_e4.insert(0,data[0][3])
				p3_e4.config(state='readonly')
				p3_e5.insert(0,data[0][5])
				p3_e5.config(state='readonly')
				p3_e6.insert(0,data[0][6])
				p3_e6.config(state='readonly')
				p3_e7.insert(0,data[0][4])
				p3_e7.config(state='readonly')
				print(data)
				showinfo("Greetings","Welcome "+a)
			else:
				raise Exception("Invalid Password")
		else:
			raise Exception("Invalid Username")
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)		 	

def back1():
	p10_e1.delete(0,END)
	p10_e2.delete(0,END)
	login.deiconify()
	employee.withdraw()
def back2():
	employee.deiconify()
	details.withdraw()
def back3():
	p4_e11.delete(0,END)
	p4_e12.delete(0,END)
	p4_e13.delete(0,END)
	p4_e21.delete(0,END)
	p4_e22.delete(0,END)
	p4_e31.delete(0,END)
	p4_e32.delete(0,END)
	p4_e33.delete(0,END)
	p4_e41.delete(0,END)
	p4_e42.delete(0,END)
	var1.set("Single (300)")
	p4_e11.focus()
	employee.deiconify()
	check_in.withdraw()
def back4():
	mycursor=mydb.cursor()
	rn=int(p5_e2.get())
	sql='delete from book_details where room_no="%d"'
	mycursor.execute(sql%(rn))
	mydb.commit()
	sql1='update rooms set Availability="Vacant" where room_no="%d"'
	mycursor.execute(sql1%(rn))
	mydb.commit()
	
	p5_e3.delete(0,END)
	p5_e4.delete(0,END)
	p5_e5.delete(0,END)
	p5_e6.delete(0,END)
	p5_e7.delete(0,END)
	p5_e8.delete(0,END)
	p5_e9.delete(0,END)
	p5_e10.delete(0,END)
	var2.set("NO")
	p5_e12.delete(0,END)
	p5_e13.delete(0,END)
	p5_e3.focus()
	check_in.deiconify()
	check_details.withdraw()

def back5():
	p6_e1.delete(0,END)
	p6_e2.delete(0,END)
	p6_e4.delete(0,END)
	var3.set("Food")
	var4.set(100)


	
	employee.deiconify()
	rs.withdraw()

def back6():
	p7_e1.delete(0,END)
	p7_e2.delete(0,END)
	p7_e3.delete(0,END)
	p7_e4.delete(0,END)
	employee.deiconify()
	game.withdraw()

def back7():
	l1=[p8_e11,p8_e12,p8_e13,p8_e14,p8_e21,p8_e22,p8_e31,p8_e32,p8_e33,p8_e41,p8_e42,p8_e43,p8_e51,p8_e52,p8_e53,p8_e61,p8_e62,p8_e63]
	for i in range(len(l1)):
			a=l1[i].delete(0,END)
	p8_e7.delete(0,END)
	p8_e8.delete(0,END)
	p8_e11.focus()
	employee.deiconify()
	rst.withdraw()
def back8():
	p9_e1.delete(0,END)
	p9_e2.delete(0,END)
	p9_e1.focus()
	employee.deiconify()
	hk.withdraw()

def back9():
	root.deiconify()
	login.withdraw()

def back10():
	adlogin.deiconify()
	ad.withdraw()
def back11():
	p12_e1.delete(0,END)
	ad.deiconify()
	gd.withdraw()

def back12():
	var5.set("phone_no")
	p13_e1.delete(0,END)
	p12_e1.delete(0,END)
	gd.deiconify()
	gdu.withdraw()
	g_details()

def back13():
	employee.deiconify()
	rms.withdraw()

def back14():
	p15_e1.delete(0,END)
	ad.deiconify()
	ed.withdraw()

def back15():
	var6.set("salary")
	p16_e1.delete(0,END)
	p15_e1.delete(0,END)
	ed.deiconify()
	edu.withdraw()
	e_details()

def back16():
	ad.deiconify()
	ade.withdraw()


def back17():
	p18_e1.delete(0,END)
	p18_e2.delete(0,END)
	root.deiconify()
	ad.withdraw()

def back18():
	
	p19_e1.delete(0,END)
	p19_e2.delete(0,END)
	p19_e3.delete(0,END)
	p19_scroll1.delete(1.0,END)
	p19_btn3.place(x=3000,y=3000)
	employee.deiconify()
	chout.withdraw()


def cko():
	chout.deiconify()
	employee.withdraw()


	
def details():
	details.deiconify()
	employee.withdraw()

	
def adlogin1():
	try:
		mycursor=mydb.cursor()
		
		un=p18_e1.get()
		p=p18_e2.get()
	
		sql='select* from adsecurity'
		mycursor.execute(sql)
		data=mycursor.fetchall()
		d=dict(data)
		k=list(d.keys())
		print(k)
		if un in k:
			if d[un]==p:
				p18_e1.delete(0,END)
				p18_e2.delete(0,END)
				ad.deiconify()
				adlogin.withdraw()
			else:
				raise Exception("Invalid Password")
		else:
			raise Exception("Invalid Username")
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)		 	

	

def rs():
	rs.deiconify()
	employee.withdraw()
	
def rst():
	rst.deiconify()
	employee.withdraw()
	
def game():
	game.deiconify()
	employee.withdraw()

def Recruit():
	try:
		mycursor=mydb.cursor()
		eid=p17_e1.get()
		ename=p17_e2.get()
		salary=p17_e3.get()
		post=p17_e5.get()
		ac=p17_e6.get()
		pn=p17_e7.get()
		dt=datetime.datetime.now()
		st=str(dt.year)+"-"+str(dt.month)+"-"+str(dt.day)
		print(type(st))
		if not ename.isalpha() or ename=="" :
			raise Exception("Invalid Name")
		elif int(salary)<=0 :
			raise Exception("Invalid Salary")
		elif not post.isalpha() or post=="":
			raise Exception("Invalid Post")
		elif len(ac)!=12 or not ac.isdigit():
			raise Exception("Invalid AdharCard Number")
		elif len(pn)!=10 or not pn.isdigit():
			raise Exception("Invalid Phone Number")

		sql='insert into employee_details values("%d","%s","%s","%d","%s","%s","%s")'
		mycursor.execute(sql%(int(eid),ename,post,int(salary),st,pn,ac))
		mydb.commit()
		p=eid+ename
		sql1='insert into security values("%s","%s")'
		mycursor.execute(sql1%(ename,p))
		mydb.commit()
		
		p17_e2.delete(0,END)
		p17_e1.config(state='normal')
		p17_e1.delete(0,END)
		
		p17_e3.delete(0,END)
		p17_e4.config(state='normal')
		p17_e4.delete(0,END)

		p17_e5.delete(0,END)
		p17_e6.delete(0,END)
		p17_e7.delete(0,END)
		
		showinfo("Success","Your login"+"\n"+"username: "+ename+"\n"+"Password: "+str(p)) 
	except ValueError:
		mydb.rollback()
		showerror("Issue","Invalid Salary")		
		
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)
		

	
	

def add_employee():
	mycursor=mydb.cursor()
	sql='select eid from employee_details';
	mycursor.execute(sql)
	d=mycursor.fetchall()
	dt=datetime.datetime.now()
	st=str(dt.day)+"-"+str(dt.month)+"-"+str(dt.year)
	t=True
	while t:
		r=random.randint(100,999);
		for i in range(len(d)):
			if r in d[i]:
				break
		else:
			t=False
	
	print(r)
	p17_e1.config(state='normal')
	p17_e1.delete(0,END)
	p17_e1.insert(0,str(r))
	p17_e1.config(state='readonly')

	p5_e4.config(state='normal')
	p5_e4.delete(0,END)
	p17_e4.insert(0,str(st))
	p17_e4.config(state='readonly')
	ade.deiconify()
	ad.withdraw()

def e_update():
	try:
		mycursor=mydb.cursor()
		name=p15_e1.get()
		sql='select* from employee_details where ename="%s"'
		mycursor.execute(sql%(name))
		d=mycursor.fetchall()
		if len(d)==0:
			raise Exception("No Employee Found")
		
		p13_lb1=Label(edu,text=name,font=("sans serif",18,"bold"),width=18,bg="#ffff00")

		p13_lb1.place(x=530,y=20)
		
		
		edu.deiconify()
		ed.withdraw()
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)

def gupdate():
	try:
		mycursor=mydb.cursor()
		name=p12_e1.get()
		l=name.split(" ")
		if len(l)!=2:
			raise Exception("Please Enter Registered Full Name")
		fn=l[0]
		ln=l[1]
		sql='select* from cust_details where fname="%s" and lname="%s";'
		mycursor.execute(sql%(fn,ln))
		d=mycursor.fetchall()
		if len(d)==0:
			raise Exception("No Guest Found")
		p13_lb1=Label(gdu,text=fn+" "+ln,font=("sans serif",18,"bold"),width=18,bg="#ffff00")

		p13_lb1.place(x=530,y=20)
		
		
		gdu.deiconify()
		gd.withdraw()
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)
def gdelete():
	try:
		mycursor=mydb.cursor()
		name=p12_e1.get()
		l=name.split(" ")
		if len(l)!=2:
			raise Exception("Please Enter Registered Full Name")
		fn=l[0]
		ln=l[1]
		sql='select* from cust_details where fname="%s" and lname="%s";'
		mycursor.execute(sql%(fn,ln))
		d=mycursor.fetchall()
		if len(d)==0:
			raise Exception("No Guest Found")
		sql="delete from book_details where room_no='%d'"
		mycursor.execute(sql%(d[0][1]))
		mydb.commit()
		sql="update rooms set Availability='Vacant' where room_no='%d'"
		mycursor.execute(sql%(d[0][1]))
		mydb.commit()
		sql="delete from cust_details where fname='%s' and lname='%s'"
		mycursor.execute(sql%(fn,ln))
		mydb.commit()
		sql="delete from game_zone where rn='%d'"
		mycursor.execute(sql%(d[0][1]))
		mydb.commit()
		sql="delete from house_keeping where rn='%d'"
		mycursor.execute(sql%(d[0][1]))
		mydb.commit()
		sql="delete from restaurant where rn='%d'"
		mycursor.execute(sql%(d[0][1]))
		mydb.commit()
		sql="delete from room_service where rn='%d'"
		mycursor.execute(sql%(d[0][1]))
		mydb.commit()
		p12_e1.delete(0,END)
		showinfo("SUCCESS","DELETED Successfully")
		
		g_details()
		
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)


def e_delete():
	try:
		mycursor=mydb.cursor()
		name=p15_e1.get()
		sql='select* from employee_details where ename="%s"'
		mycursor.execute(sql%(name))
		d=mycursor.fetchall()
		if len(d)==0:
			raise Exception("No Employee Found")
		sql="delete from employee_details where ename='%s'"
		mycursor.execute(sql%(name))
		mydb.commit()
		sql="delete from security where username='%s'"
		mycursor.execute(sql%(name))
		mydb.commit()
		p15_e1.delete(0,END)
		showinfo("SUCCESS","DELETED Successfully")
		
		e_details()
		
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)
			
		
	
def new(gid,d):
	check_details.deiconify()
	check_in.withdraw()
	print(gid,d)
	p5_e1.config(state='normal')
	p5_e1.delete(0,END)
	p5_e1.insert(0,gid)
	
	p5_e1.config(state='readonly')
	p5_e2.config(state='normal')
	p5_e2.delete(0,END)
	p5_e2.insert(0,d)
	
	p5_e2.config(state='readonly')
	showinfo("Success","Please Enter the details")
def hk():
	hk.deiconify()
	employee.withdraw()




def e_details():
	try:
		
		mycursor=mydb.cursor()
		sql="select* from employee_details"
		mycursor.execute(sql)
		d=mycursor.fetchall()
		if len(d)==0:
			ad.deiconify()
			ed.withdraw()
			raise Exception("Employee Records Is empty")
		msg=""
		star="*"
		p15_scroll1.delete(1.0,END)
		for i in range(165):
			star=star+"*"
		print(d)
		for i in range(len(d)):
			msg=msg+"Employee ID:  "+str(d[i][0])+"        "+"Employee Name:  "+d[i][1]+"        "+"POST:  "+d[i][2]+"        "+"SALARY:  "+str(d[i][3])+"\n\n"+"Date Of Joining:  "+str(d[i][4].day)+"-"+str(d[i][4].month)+"-"+str(d[i][4].year)+"        "+"Phone Number:  "+d[i][5]+"        "+"Adharcard Number:  "+d[i][6]+"\n\n\n"+star+"\n\n\n"
		
		p15_scroll1.insert(INSERT,msg)
		p15_e1.focus()
			
		ed.deiconify()
		ad.withdraw()
		p15_e1.focus()

	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)	

	
	
def check():
	l=[31,28,31,30,31,30,31,31,30,31,30,31]
	print("clicked Check")
	try:
		mycursor=mydb.cursor()
		now=datetime.datetime.now()
		
		y=p4_e13.get()
		if(int(y)<now.year or int(y)>now.year+1):
			raise Exception("Invalid Arrival Year")
		if(int(y)%100==0 and int(y)%400==0):
			l=[31,29,31,30,31,30,31,31,30,31,30,31]
		elif(int(y)%4==0):
			l=[31,29,31,30,31,30,31,31,30,31,30,31]
		
		m=p4_e12.get()
		if((int(y)==now.year and int(m)<now.month)or int(m)>12 or (int(y)>now.year and int(m)!=1)):
			raise Exception("Invalid Arrival Month and you can only book for january for the next year")
		
		d=p4_e11.get()
		if((int(m)==now.month and int(d)<now.day) or (int(d)<= 0) or(int(d)>l[int(m)-1])):
			raise Exception("Invalid Arrival Date")
		
		doa=p4_e13.get()+"-"+p4_e12.get()+"-"+p4_e11.get()
		
		h=p4_e21.get()
		if(int(h)<0 or int(h)>23 or (int(h)<now.hour and int(d)==now.day and int(m)==now.month and int(y)==now.year)):
			raise Exception("Invalid Arrival Time")
		
		min=p4_e22.get()
		if(int(min)<0 or int(min)>59 or (int(min)<now.minute and int(h)==now.hour and int(d)==now.day and int(m)==now.month and int(y)==now.year)):
			raise Exception("Invalid Arrival Time")
		toa=p4_e21.get()+" : "+p4_e22.get()
		y1=p4_e33.get()
		if(int(y1)<int(y) or int(y1)>int(y)+1 or int(y1)>now.year+1):
			raise Exception('Invalid Leaving Year') 
		
		m1=p4_e32.get()
		if((int(m1)<int(m) and int(y1)==int(y)) or (int(y1)==now.year+1 and int(m1)!=1)):
			raise Exception('Invalid Leaving Month and next year bookings can be made only till january')
	
		d1=p4_e31.get()
		if((int(d1)<int(d) and int(m1)==int(m)) or int(d1)<=0 or (int(d1)>l[int(m1)-1])):
			raise Exception("Invalid Leaving date ")
		dol=p4_e33.get()+"-"+p4_e32.get()+"-"+p4_e31.get()

		h1=p4_e41.get()
		if int(h1)<0 or int(h1)>23 or (int(h1)<int(h) and int(d)==int(d1) and int(m)==int(m1) and int(y)==int(y1)) :
			raise Exception('Invalid Leaving Time')

		min1=p4_e42.get()
		if(int(min1)<0 or(int(min1)<int(min) and int(h1)==int(h) and int(d)==int(d1) and int(m)==int(m1) and int(y)==int(y1)) or (int(min1)>59)):
			raise Exception("Invalid Leaving Time")
		tol=p4_e41.get()+" : "+p4_e42.get()
		l1=(var1.get()).split(" ")
		rt=l1[0]
		
		l=random.sample(range(1000),3)
		gid=[str(i) for i in l]
		gid=('').join(gid)
		gid=int(gid)
		
		sql='select room_no from rooms where room_type="%s" and Availability="Vacant"'
		mycursor.execute(sql%(rt))
		data=mycursor.fetchall()
		print(data)
		if len(data)==0:
			showerror("Issue","All "+ rt+ " rooms are booked please choose other room type")
		else:
			sql='insert into book_details values("%d","%s","%d","%s","%s","%s","%s")'
			mycursor.execute(sql%(gid,rt,data[0][0],doa,toa,dol,tol))
			mydb.commit()
			p4_e11.delete(0,END)
			p4_e12.delete(0,END)
			p4_e13.delete(0,END)
			p4_e21.delete(0,END)
			p4_e22.delete(0,END)
			p4_e31.delete(0,END)
			p4_e32.delete(0,END)
			p4_e33.delete(0,END)
			p4_e41.delete(0,END)
			p4_e42.delete(0,END)
			var1.set("Single (300)")
			p4_e11.focus()
			new(gid,data[0][0])
			
	except ValueError:
		mydb.rollback()
		showerror("Issue","Date And Time Should Be Integers")		
		
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)
def check_in():
	check_in.deiconify()
	employee.withdraw()

def gdetails():
	try :
		mycursor=mydb.cursor()
		rno=p5_e2.get()
		gid=p5_e1.get()
		fn=p5_e3.get()
		ln=p5_e4.get()
		ad=p5_e5.get()
		oc=p5_e6.get()
		ph=p5_e7.get()
		an=p5_e8.get()
		noa=p5_e9.get()
		noc=p5_e10.get()
		v=var2.get()
		vm=p5_e12.get()
		np=p5_e13.get()
		if not all(i.isalnum() or i.isspace() for i in ad):
			raise Exception("Invalid Address")
		if v=="YES" and (vm=="" or np=="") :
			raise Exception("Vehicle model and number is not mentioned")
		elif v=="NO":
			vm="na"
			np="na"
		if not fn.isalpha() or not ln.isalpha() or not oc.isalpha():
			raise Exception("Invalid Entry for fname,lname or Occuoation or Some details are yet to fill")
		if int(noa)<=0 or int(noc)<0:
			raise Exception("Invalid Count")
		if v=="YES" and (not vm.isalpha() or not np.isalnum()):
			raise Exception("Invalid Vehicle Details")

		
		sql='insert into cust_details values("%d","%d","%s","%s","%s","%s","%d","%d","%d","%s","%s","%s","%s","%s")'
		mycursor.execute(sql%(int(gid),int(rno),ln,fn,ad,ph,int(noa),int(noc),int(noa)+int(noc),oc,an,v,vm,np))
		
		mydb.commit()
		p5_e1.delete(0,END)
		p5_e2.delete(0,END)
		p5_e3.delete(0,END)
		p5_e4.delete(0,END)
		p5_e5.delete(0,END)
		p5_e6.delete(0,END)
		p5_e7.delete(0,END)
		p5_e8.delete(0,END)
		p5_e9.delete(0,END)
		p5_e10.delete(0,END)
		var2.set("NO")
		p5_e12.delete(0,END)
		p5_e13.delete(0,END)
		p5_e3.focus()
		showinfo("Success","Enjoy Your Stay")
		employee.deiconify()
		check_details.withdraw()


	except ValueError:
		mydb.rollback()
		showerror("Issue","Enter All Details Properly")	

	except mysql.connector.Error as e:
		mydb.rollback()
		print(e.errno)
		if e.errno==1062:
			showerror("Issue","The Guest ID Already Exists")
		else:
			showerror("Issue",e)

	
	
	
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)

def rs_sub():
	try :
		mycursor=mydb.cursor()
		rn=p6_e1.get()
		if rn.isalpha():
			raise Exception("Invalid Room Number")
		name=p6_e2.get()
		if not name.isalpha():
			raise Exception("Invalid Name")
		
		w=var3.get()
		o=p6_e4.get()
		if w=="Other" and o=="":
			raise Exception("Reason not metioned in other")
		if w!="Other":
			o="na"
		c=var4.get()
		sql='select fname from cust_details where r_no="%d"'
		mycursor.execute(sql%(int(rn)))
		data=mycursor.fetchall()
		if len(data)==0:
			raise Exception("Invalid Room Number")
		elif data[0][0]!=name:
			raise Exception("Invalid Name for Room Number")

		sql='insert into room_service values("%d","%s","%s","%s","%d")'
		mycursor.execute(sql%(int(rn),name,w,o,c))
		mydb.commit()
		showinfo("DONE","Data Entered")
		p6_e1.delete(0,END)
		p6_e2.delete(0,END)
		var3.set("Food")
		p6_e4.delete(0,END)
		var4.set(100)
		p6_e1.focus()
		
		
	
	except ValueError:
		mydb.rollback()
		showerror("Issue","Invalid Name")	

	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)

			
		
def game_sub():
	try :
		mycursor=mydb.cursor()
		rn=p7_e1.get()
		if rn.isalpha():
			raise Exception("Invalid Room Number")
		name=p7_e2.get()
		if not name.isalpha():
			raise Exception("Invalid Name")
		c=p7_e3.get()
		if c.isalpha():
			raise Exception("Invalid Count")
		t=p7_e4.get()
		if t.isalpha():
			raise Exception("Invalid Time")
		sql='select fname from cust_details where r_no="%d"'
		mycursor.execute(sql%(int(rn)))
		data=mycursor.fetchall()
		if len(data)==0:
			raise Exception("Invalid Room Number")
		elif data[0][0]!=name:
			raise Exception("Invalid Name for Room Number")
		total=int(c)*200+int(t)*100

		sql='insert into game_zone values("%d","%s","%d","%d","%d")'
		mycursor.execute(sql%(int(rn),name,int(c),int(t),total))
		mydb.commit()
		showinfo("Success","Your total amount is "+str(total))
		p7_e1.delete(0,END)
		p7_e2.delete(0,END)
		p7_e3.delete(0,END)
		p7_e4.delete(0,END)
		p7_e1.focus()
		

	except ValueError:
		mydb.rollback()
		showerror("Issue","Invalid Name")	

	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)
 
def order():
	try :
		mycursor=mydb.cursor()
		rn=p8_e7.get()
		if rn.isalpha():
			raise Exception("Invalid Room Number")
		name=p8_e8.get()
		if not name.isalpha():
			raise Exception("Invalid Name")
		sql='select fname from cust_details where r_no="%d"'
		mycursor.execute(sql%(int(rn)))
		data=mycursor.fetchall()
		if len(data)==0:
			raise Exception("Invalid Room Number")
		elif data[0][0]!=name:
			raise Exception("Invalid Name for Room Number")
		l=[70,50,60,40,40,40,50,40,30,200,160,130,110,150,100,100,80,120]
		total=0
		l1=[p8_e11,p8_e12,p8_e13,p8_e14,p8_e21,p8_e22,p8_e31,p8_e32,p8_e33,p8_e41,p8_e42,p8_e43,p8_e51,p8_e52,p8_e53,p8_e61,p8_e62,p8_e63]
		for i in range(len(l1)):
			a=l1[i].get()
			if a=="":
				a=0
			elif a.isalpha() or int(a)<0:
				raise Exception("Invalid Count") 
			else:
				total=total+int(a)*l[i]
		sql='insert into restaurant values("%d","%s","%d")'
		mycursor.execute(sql%(int(rn),name,total))
		mydb.commit()
		showinfo("Success","Your total amount is "+str(total))
		for i in range(len(l1)):
			a=l1[i].delete(0,END)
		p8_e7.delete(0,END)
		p8_e8.delete(0,END)
		p8_e11.focus()
		
		
				
	except ValueError:
		mydb.rollback()
		showerror("Issue","Invalid Name")	
			
		
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)


def hk_sub():
	try :
		mycursor=mydb.cursor()
		rn=p9_e1.get()
		if rn.isalpha():
			raise Exception("Invalid Room Number")
		name=p9_e2.get()
		if not name.isalpha():
			raise Exception("Invalid Name")
		sql='select fname from cust_details where r_no="%d"'
		mycursor.execute(sql%(int(rn)))
		data=mycursor.fetchall()
		if len(data)==0:
			raise Exception("Invalid Room Number")
		elif data[0][0]!=name:
			raise Exception("Invalid Name for Room Number")
		p=100
		a=datetime.datetime.now()
		sql='insert into house_keeping values("%d","%s","%s","%s","%d")'
		mycursor.execute(sql%(int(rn),name,str(a.year)+"-"+str(a.month)+"-"+str(a.day),str(a.hour)+" : "+str(a.minute),p))
		mydb.commit()
		showinfo("Success","Data Added")
		p9_e1.delete(0,END)
		p9_e2.delete(0,END)
		p9_e1.focus()
	except ValueError:
		mydb.rollback()
		showerror("Issue","Invalid Name")	
			
		
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)	


def admin():
	
	adlogin.deiconify()
	root.withdraw()


def g_details():
	try:
		
		mycursor=mydb.cursor()
		sql="select* from cust_details"
		mycursor.execute(sql)
		d=mycursor.fetchall()
		if len(d)==0:
			ad.deiconify()
			gd.withdraw()
			raise Exception("Guest Records Is empty")
		sql1="select* from book_details where guest_id='%d'"
		
		
		msg=""
		star="*"
		p12_scroll1.delete(1.0,END)
		for i in range(165):
			star=star+"*"
		for i in range(len(d)):
			mycursor.execute(sql1%(d[i][0]))
			d1=mycursor.fetchall()
			if len(d1)==0:
				raise Exception("Guest Records Is empt")
			msg=msg+"Room No.: "+str(d[i][1])+"        "+"Name: "+d[i][3]+" "+d[i][2]+"        "+"Phone No.: "+d[i][5]+"        "+"Aadhar No.: "+d[i][10]+"        "+"Occupation: "+d[i][9]+"\n\n\n"+"Adults: "+str(d[i][6])+"          "+"Children: "+str(d[i][7])+"          "+"Total: "+str(d[i][8])+"          "+"Vehicle: "+d[i][11]+"          "+"Vehicle Model: "+d[i][12]+"          "+"Number Plate: "+d[i][13]+"\n\n\n"+"Address: "+d[i][4]+"\n\n\n"+"Check-IN Date: "+str(d1[0][3].day)+"-"+str(d1[0][3].month)+"-"+str(d1[0][3].year)+"        "+"Check-IN Time: "+d1[0][4]+"        "+"Check-OUT Date: "+str(d1[0][5].day)+"-"+str(d1[0][5].month)+"-"+str(d1[0][5].year)+"        "+"Check-OUT Time: "+d1[0][6]+"\n\n\n\n"+star





		p12_scroll1.insert(INSERT,msg)
		p12_e1.focus()
			
		gd.deiconify()
		ad.withdraw()
		p12_e1.focus()

	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)	

def search():
	try:
		mycursor=mydb.cursor()
		name=p12_e1.get()
		l=name.split(" ")
		if len(l)!=2:
			raise Exception("Please Enter Registered Full Name")
		print(l)
		print(len(l))
		fn=l[0]
		ln=l[1]
		sql='select* from cust_details where fname="%s" and lname="%s";'
		mycursor.execute(sql%(fn,ln))
		d=mycursor.fetchall()
		if len(d)==0:
			raise Exception("No Guest Found")
		sql1="select* from book_details where guest_id='%d'"
		mycursor.execute(sql1%(d[0][0]))
		d1=mycursor.fetchall()
		p12_scroll1.delete(1.0,END)
		msg=""
		msg=msg+"Room No.: "+str(d[0][1])+"        "+"Name: "+d[0][3]+" "+d[0][2]+"        "+"Phone No.: "+d[0][5]+"        "+"Aadhar No.: "+d[0][10]+"        "+"Occupation: "+d[0][9]+"\n\n\n"+"Adults: "+str(d[0][6])+"          "+"Children: "+str(d[0][7])+"          "+"Total: "+str(d[0][8])+"          "+"Vehicle: "+d[0][11]+"          "+"Vehicle Model: "+d[0][12]+"          "+"Number Plate: "+d[0][13]+"\n\n\n"+"Address: "+d[0][4]+"\n\n\n"+"Check-IN Date: "+str(d1[0][3].day)+"-"+str(d1[0][3].month)+"-"+str(d1[0][3].year)+"        "+"Check-IN Time: "+d1[0][4]+"        "+"Check-OUT Date: "+str(d1[0][5].day)+"-"+str(d1[0][5].month)+"-"+str(d1[0][5].year)+"        "+"Check-OUT Time: "+d1[0][6]
		p12_scroll1.insert(INSERT,msg)
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)



def e_search():
	try:
		mycursor=mydb.cursor()
		name=p15_e1.get()
		sql='select* from employee_details where ename="%s"'
		mycursor.execute(sql%(name))
		d=mycursor.fetchall()
		if len(d)==0:
			raise Exception("No Employee Found")

		msg=""
		star="*"
		p15_scroll1.delete(1.0,END)
		for i in range(165):
			star=star+"*"
		print(d)
		for i in range(len(d)):
			msg=msg+"Employee ID:  "+str(d[i][0])+"        "+"Employee Name:  "+d[i][1]+"        "+"POST:  "+d[i][2]+"        "+"SALARY:  "+str(d[i][3])+"\n\n"+"Date Of Joining:  "+str(d[i][4].day)+"-"+str(d[i][4].month)+"-"+str(d[i][4].year)+"        "+"Phone Number:  "+d[i][5]+"        "+"Adharcard Number:  "+d[i][6]+"\n\n\n"+star+"\n\n\n"
		p15_scroll1.insert(INSERT,msg)
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)		
def rms():
	mycursor=mydb.cursor()
	sql1="select* from rooms"
	mycursor.execute(sql1)
	d=mycursor.fetchall()
	p14_scroll1.delete(1.0,END)
	msg=""
	star="*"
	for i in range(165):
		star=star+"*"
	for i in range(len(d)):
		msg=msg+"ROOM NUMBER: "+str(d[i][0])+"        "+"ROOM TYPE: "+d[i][2]+"        "+"AVAILABILITY: "+d[i][3]+"        "+"ROOM CHARGE: "+str(d[i][4])+"\n\n"+star+"\n\n"


	p14_scroll1.insert(INSERT,msg)
		
	rms.deiconify()
	employee.withdraw()

def update_sub():
	try:
		mycursor=mydb.cursor()
		field=var5.get()
		print(field)
		value=p13_e1.get()
		name=p12_e1.get()
		name=name.split(' ')
		if field=="address" and not all(i.isalnum() or i.isspace() for i in value):
			raise Exception("Invalid Address")
		if field=="occupation" and not value.isalpha():
			raise Exception("Invalid Entry Occupation")
		if field=="occupation" or field=="address" or field=="Adharcard_no":
			sql="update cust_details set "+field+"='%s' where  fname='%s' and lname='%s'"
			mycursor.execute(sql%(value,name[0],name[1]))
		elif field=="no_adults":
			sql="select* from cust_details where  fname='%s' and lname='%s'"
			mycursor.execute(sql%(name[0],name[1]))
			d=mycursor.fetchall()
			t=int(value)+d[0][7]
			sql="update cust_details set "+field+"='%d',total='%d' where  fname='%s' and lname='%s'"
			mycursor.execute(sql%(int(value),t,name[0],name[1]))
		elif field=="no_children":
			sql="select* from cust_details where  fname='%s' and lname='%s'"
			mycursor.execute(sql%(name[0],name[1]))
			d=mycursor.fetchall()
			t=int(value)+d[0][6]
			sql="update cust_details set "+field+"='%d',total='%d' where  fname='%s' and lname='%s'"
			mycursor.execute(sql%(int(value),t,name[0],name[1]))
			
		else:
			sql="update cust_details set "+field+"='%d' where  fname='%s' and lname='%s'"
			mycursor.execute(sql%(int(value),name[0],name[1]))
		mydb.commit()
		var5.set("phone_no")
		p13_e1.delete(0,END)
		showinfo("SUCCESS","Updated Successfully")
	
	except ValueError:
		mydb.rollback()
		showerror("Issue","Invalid Entry")	
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)

def eupdate_sub():
	try:
		mycursor=mydb.cursor()
		field=var6.get()
		print(field)
		value=p16_e1.get()
		name=p15_e1.get()
		
		if field=="duty" and not value.isalpha():
			raise Exception("Invalid Duty Assigned")
		elif field=="phone" and (not value.isdigit() or len(value)!=10):
			raise Exception("Invalid Phone Number")
		elif field=="salary" and int(value)<=0:
			raise Exception("Invalid Salary")
		if field=="duty" or field=="phone":
			sql="update employee_details set "+field+"='%s' where ename='%s'"
			mycursor.execute(sql%(value,name))			
		else:
			sql="update employee_details set "+field+"='%d' where ename='%s'"
			mycursor.execute(sql%(int(value),name))
		mydb.commit()
		var6.set("salary")
		p16_e1.delete(0,END)
		showinfo("SUCCESS","Updated Successfully")
	
	except ValueError:
		mydb.rollback()
		showerror("Issue","Invalid Entry")	
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)	
		

def ent():
	try:
		mycursor=mydb.cursor()
		name=p19_e1.get()
		name=name.split(' ')
		
		rn=p19_e2.get()
		fb=p19_e3.get()
		if not (i.isalpha() for i in name) or len(name)!=2:
			raise Exception("Inavid Name")
		elif not rn.isdigit() or rn=="" or int(rn)<=0:
			raise Exception("Invalid Room Number")
		elif not all(i.isalnum() or i.isspace() for i in fb) or fb=="":
			raise Exception("Invalid Feedback")
		fn=name[0]
		ln=name[1]
		sql='select fname,lname from cust_details where r_no="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		if len(d)==0:	
			raise Exception("Room Already Vacant")
		print(d)
		if fn!=d[0][0] or ln!=d[0][1]:
			raise Exception("Invalid Name for the room number")

		sql='select date_of_arrival,date_of_leaving from book_details where room_no="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		delta=d[0][1]-d[0][0]
		days=delta.days
		c1,c2,c3,c4,c5=0,0,0,0,0
		sql='select cost from rooms where room_no="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		c1=int(d[0][0])*days
		msg="\t\t"+"   "+"BILL for "+fn+" "+ln+"\n\n"+str(days)+" days                  "+"...............................................................  "+str(c1)+" ₹"
		
		sql='select pay from game_zone where rn="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		print(d)
		for i in range(len(d)):
			c2=c2+d[i][0]
		if len(d)!=0:
			msg=msg+"\n\n"+"Game-Zone         "+"...............................................................  "+str(c2)+" ₹"

		sql='select p from house_keeping where rn="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		for i in range(len(d)):
			c3=c3+d[i][0]
		if len(d)!=0:
			msg=msg+"\n\n"+"House-Keeping  "+"...............................................................  "+str(c3)+" ₹"
		
		sql='select total from restaurant where rn="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		for i in range(len(d)):
			c4=c4+d[i][0]
		if len(d)!=0:
			msg=msg+"\n\n"+"Restaurant          "+"...............................................................  "+str(c4)+" ₹"
		
		sql='select pay from room_service where rn="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		for i in range(len(d)):
			c5=c5+d[i][0]
		if len(d)!=0:
			msg=msg+"\n\n"+"Room-Service     "+"...............................................................  "+str(c5)+" ₹"

		s1=c1+c2+c3+c4+c5
		gst=s1*0.025
		msg=msg+"\n\n"+"GST                       "+"...............................................................  "+str(gst)+" ₹"	
		s2=s1+gst
		msg=msg+"\n\n\n\n"+"\t\t"+"  "+"TOTAL = "+str(s2)+" ₹"+"\n\n\n"+"\t"+"****************************************************"
		p19_scroll1.insert(1.0,msg)
		p19_btn3.place(x=850,y=530)

	except ValueError:
		mydb.rollback()
		showerror("Issue","Invalid Entry")	
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)	


def bye():
	try:
		mycursor=mydb.cursor()
		name=p19_e1.get()
		name1=name
		name=name.split(' ')
		
		rn=p19_e2.get()
		fb=p19_e3.get()
		if not (i.isalpha() for i in name) or len(name)!=2:
			raise Exception("Inavid Name")
		elif not rn.isdigit() or rn=="" or int(rn)<=0:
			raise Exception("Invalid Room Number")
		elif not all(i.isalnum() or i.isspace() for i in fb) or fb=="":
			raise Exception("Invalid Feedback")
		fn=name[0]
		ln=name[1]
		sql='select fname,lname from cust_details where r_no="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		if len(d)==0:	
			raise Exception("Room Already Vacant")
		print(d)
		if fn!=d[0][0] or ln!=d[0][1]:
			raise Exception("Invalid Name for the room number")

		sql='select date_of_arrival,date_of_leaving from book_details where room_no="%d"'
		mycursor.execute(sql%(int(rn)))
		d1=mycursor.fetchall()
		delta=d1[0][1]-d1[0][0]
		days=delta.days
		c1,c2,c3,c4,c5=0,0,0,0,0
		sql='select cost from rooms where room_no="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		c1=int(d[0][0])*days
		
		sql='select pay from game_zone where rn="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		print(d)
		for i in range(len(d)):
			c2=c2+d[i][0]
		
		sql='select p from house_keeping where rn="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		for i in range(len(d)):
			c3=c3+d[i][0]
		
		sql='select total from restaurant where rn="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		for i in range(len(d)):
			c4=c4+d[i][0]
		
		
		sql='select pay from room_service where rn="%d"'
		mycursor.execute(sql%(int(rn)))
		d=mycursor.fetchall()
		for i in range(len(d)):
			c5=c5+d[i][0]
		
		s1=c1+c2+c3+c4+c5
		gst=s1*0.025
		
		s2=s1+gst
		print(d1[0][0])
		sql='insert into backup_data values("%d","%s","%s","%s","%d","%d","%d","%d","%d","%d","%s")'
		mycursor.execute(sql%(int(rn),name1,str(d1[0][0]),str(d1[0][1]),c4,c5,c3,c2,c1,s2,fb))
		mydb.commit()
		p19_e1.delete(0,END)
		p19_e2.delete(0,END)
		p19_e3.delete(0,END)
		p19_scroll1.delete(1.0,END)
		p19_btn3.place(x=3000,y=3000)
		p19_e1.focus()
		showinfo("Success","We hope to see you again")


		sql="delete from book_details where room_no='%d'"
		mycursor.execute(sql%(int(rn)))
		mydb.commit()
		sql="update rooms set Availability='Vacant' where room_no='%d'"
		mycursor.execute(sql%(int(rn)))
		mydb.commit()
		sql="delete from cust_details where fname='%s' and lname='%s'"
		mycursor.execute(sql%(fn,ln))
		mydb.commit()
		sql="delete from game_zone where rn='%d'"
		mycursor.execute(sql%(int(rn)))
		mydb.commit()
		sql="delete from house_keeping where rn='%d'"
		mycursor.execute(sql%(int(rn)))
		mydb.commit()
		sql="delete from restaurant where rn='%d'"
		mycursor.execute(sql%(int(rn)))
		mydb.commit()
		sql="delete from room_service where rn='%d'"
		mycursor.execute(sql%(int(rn)))
		mydb.commit()
	except ValueError:
		mydb.rollback()
		showerror("Issue","Invalid Entry")	
	except Exception as e:
		mydb.rollback()
		showerror("Issue",e)	
		
		
			

root=Tk()
root.title("The Peninsula")

root.configure(background="#b3ffff")
root.iconbitmap("logo.ico")

root.geometry("1200x600+200+100")
canvas1=Canvas(root,width=1200,height=600)

image1=ImageTk.PhotoImage(Image.open("F:\\project\\test.png"))

canvas1.create_image(0,0,anchor=NW,image=image1)

p1_btn1=Button(root,text="ADMIN",font=("sans serif",18,"bold"),width=15,bg="#ffff00",command=admin)
p1_btn1.config(relief="groove")
p1_btn2=Button(root,text="STAFF",font=("sans serif",18,"bold"),width=15,bg="#ffff00",command=employee)
p1_btn2.config(relief="groove")



p1_btn1.place(x=530,y=250)
p1_btn2.place(x=530,y=350)
canvas1.pack()



login=Toplevel(root)
login.title("The Peninsula")

login.configure(background="#b3ffff")
login.iconbitmap("logo.ico")

login.geometry("1200x600+200+100")
canvas2=Canvas(login,width=1200,height=600)

image2=ImageTk.PhotoImage(Image.open("F:\\project\\test.png"))

canvas2.create_image(0,0,anchor=NW,image=image2)

p10_lb1=Label(login,text="Enter Registered Name",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p10_e1=Entry(login,bd=3,font=("sans serif",18,"bold"),width=15)

p10_lb2=Label(login,text="Enter Password",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p10_e2=Entry(login,bd=3,font=("sans serif",18,"bold"),width=15,show="*")

p10_bt1=Button(login,text="BACK",font=("sans serif",18,"bold"),bg="#ffff00",command=back9)
p10_bt2=Button(login,text="LOGIN",font=("sans serif",18,"bold"),bg="#ffff00",command=security)

p10_e1.focus()

p10_bt1.place(x=460,y=500)

p10_bt2.place(x=680,y=500)

p10_lb1.place(x=390,y=200)
p10_e1.place(x=690,y=200)
p10_lb2.place(x=390,y=300)
p10_e2.place(x=690,y=300)
canvas2.pack()

login.withdraw()

employee=Toplevel(login)
employee.title("STAFF")
employee.configure(background="#b3ffff")
employee.iconbitmap("logo.ico")
employee.geometry("1200x600+200+100")


details1=PhotoImage(file="F:\\project\\hr.png")
details11=details1.subsample(2,2)

details2=PhotoImage(file="F:\\project\\hotel.png")
details21=details2.subsample(2,2)

details3=PhotoImage(file="F:\\project\\receptionist.png")
details31=details3.subsample(2,2)

details4=PhotoImage(file="F:\\project\\room-service.png")
details41=details4.subsample(2,2)

details5=PhotoImage(file="F:\\project\\dinner.png")
details51=details5.subsample(2,2)

details6=PhotoImage(file="F:\\project\\house.png")
details61=details6.subsample(2,2)


details7=PhotoImage(file="F:\\project\\game-controller.png")
details71=details7.subsample(2,2)

details8=PhotoImage(file="F:\\project\\graph.png")
details81=details8.subsample(2,2)








p2_bt1=Button(employee,image=details11,borderwidth=0,bg="#ffff66",command=details)
p2_lb1=Label(employee,text="DETAILS",font=("sans serif",18,"bold"),bg="#b3ffff")
p2_bt2=Button(employee,image=details21,borderwidth=0,bg="#ffff66",command=check_in)
p2_lb2=Label(employee,text="CHECK-IN",font=("sans serif",18,"bold"),bg="#b3ffff")
p2_bt3=Button(employee,image=details31,borderwidth=0,bg="#ffff66",command=cko)
p2_lb3=Label(employee,text="CHECK-OUT",font=("sans serif",18,"bold"),bg="#b3ffff")
p2_bt4=Button(employee,image=details41,borderwidth=0,bg="#ffff66",command=rs)
p2_lb4=Label(employee,text="ROOM-SERVICE",font=("sans serif",18,"bold"),bg="#b3ffff")
p2_bt5=Button(employee,image=details51,borderwidth=0,bg="#ffff66",command=rst)
p2_lb5=Label(employee,text="RESTAURENT",font=("sans serif",18,"bold"),bg="#b3ffff")
p2_bt6=Button(employee,image=details61,borderwidth=0,bg="#ffff66",command=hk)
p2_lb6=Label(employee,text="HOUSE-KEEPING",font=("sans serif",18,"bold"),bg="#b3ffff")
p2_bt7=Button(employee,image=details71,borderwidth=0,bg="#ffff66",command=game)
p2_lb7=Label(employee,text="GAME-ZONE",font=("sans serif",18,"bold"),bg="#b3ffff")
p2_bt8=Button(employee,image=details81,borderwidth=0,bg="#ffff66",command=rms)
p2_lb8=Label(employee,text="Room Status",font=("sans serif",18,"bold"),bg="#b3ffff")
p2_bt9=Button(employee,text="BACK",font=("sans serif",18,"bold"),bg="#ffff00",command=back1)


p2_bt1.place(x=100,y=70)
p2_lb1.place(x=110,y=210)
p2_bt2.place(x=400,y=70)
p2_lb2.place(x=400,y=210)
p2_bt3.place(x=700,y=70)
p2_lb3.place(x=700,y=210)
p2_bt4.place(x=100,y=300)
p2_lb4.place(x=80,y=440)
p2_bt5.place(x=400,y=300)
p2_lb5.place(x=380,y=440)
p2_bt6.place(x=700,y=300)
p2_lb6.place(x=680,y=440)

p2_bt7.place(x=1000,y=70)
p2_lb7.place(x=990,y=210)
p2_bt8.place(x=1000,y=300)
p2_lb8.place(x=1010,y=440)
p2_bt9.place(x=570,y=530)
employee.withdraw()


details=Toplevel(employee)
details.title("DETAILS")
details.configure(background="#b3ffff")
details.iconbitmap("logo.ico")
details.geometry("1200x600+200+100")


p3_lb1=Label(details,text="Employee ID",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p3_e1=Entry(details,bd=3,font=("sans serif",18,"bold"),width=14)


p3_lb2=Label(details,text="Employee Name",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p3_e2=Entry(details,bd=3,font=("sans serif",18,"bold"),width=14)


p3_lb3=Label(details,text="Duty",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p3_e3=Entry(details,bd=3,font=("sans serif",18,"bold"),width=14)

p3_lb4=Label(details,text="Salary",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p3_e4=Entry(details,bd=3,font=("sans serif",18,"bold"),width=14)

p3_lb5=Label(details,text="Phone Number",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p3_e5=Entry(details,bd=3,font=("sans serif",18,"bold"),width=14)

p3_lb6=Label(details,text="Aadhar Number",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p3_e6=Entry(details,bd=3,font=("sans serif",18,"bold"),width=14)

p3_lb7=Label(details,text="Date OF Joining",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p3_e7=Entry(details,bd=3,font=("sans serif",18,"bold"),width=14)





p3_btn3=Button(details,text="BACK",font=("sans serif",18,"bold"),bg="#ffff00",command=back2)


p3_lb1.place(x=30,y=10)
p3_e1.place(x=370,y=10)

p3_lb2.place(x=30,y=100)
p3_e2.place(x=370,y=100)

p3_lb3.place(x=30,y=200)
p3_e3.place(x=370,y=200)

p3_lb4.place(x=30,y=300)
p3_e4.place(x=370,y=300)

p3_lb5.place(x=30,y=400)
p3_e5.place(x=370,y=400)


p3_lb6.place(x=600,y=10)
p3_e6.place(x=900,y=10)

p3_lb7.place(x=600,y=100)
p3_e7.place(x=900,y=100)


p3_btn3.place(x=550,y=530)

details.withdraw()


check_in=Toplevel(employee)
check_in.title("CHECK IN")
check_in.configure(background="#b3ffff")
check_in.iconbitmap("logo.ico")
check_in.geometry("1200x600+200+100")
img=PhotoImage(file='arrow.gif')
var1=StringVar()
var1.set("Single (300)")

canvas8=Canvas(check_in,width=800,height=900)

image8=ImageTk.PhotoImage(Image.open("F:\\project\\t5.jpg"))

canvas8.create_image(0,0,anchor=NW,image=image8)

p4_lb1=Label(check_in,text="Date of Arrival (dd/mm/yy)",font=("sans serif",18,"bold"),width=20,bg="#ffff00")
p4_e11=Entry(check_in,bd=3,font=("sans serif",18,"bold"),width=4)
p4_e12=Entry(check_in,bd=3,font=("sans serif",18,"bold"),width=4)
p4_e13=Entry(check_in,bd=3,font=("sans serif",18,"bold"),width=4)
p4_lb2=Label(check_in,text="Time of Arrival (hh:min)",font=("sans serif",18,"bold"),width=20,bg="#ffff00")
p4_e21=Entry(check_in,bd=3,font=("sans serif",18,"bold"),width=4)
p4_e22=Entry(check_in,bd=3,font=("sans serif",18,"bold"),width=4)

p4_lb3=Label(check_in,text="Date of Leaving (dd/mm/yy)",font=("sans serif",18,"bold"),width=22,bg="#ffff00")
p4_e31=Entry(check_in,bd=3,font=("sans serif",18,"bold"),width=4)
p4_e32=Entry(check_in,bd=3,font=("sans serif",18,"bold"),width=4)
p4_e33=Entry(check_in,bd=3,font=("sans serif",18,"bold"),width=4)

p4_lb4=Label(check_in,text="Time of Leaving (hh:mm)",font=("sans serif",18,"bold"),width=20,bg="#ffff00")
p4_e41=Entry(check_in,bd=3,font=("sans serif",18,"bold"),width=4)
p4_e42=Entry(check_in,bd=3,font=("sans serif",18,"bold"),width=4)
p4_lb5=Label(check_in,text="Room Type",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p4_option1=OptionMenu(check_in,var1,"Single (300)","Double (400)","Triple (500)","Quad (600)","Queen (800)","King (900)")

p4_option1.config(indicatoron=0,width=170,height=30,font=("sans serif",16,"bold"),image=img,bg="#ffff80",compound='right')  #compound for plcing arrow to right and indicatoron=0 to hide the default indicator


p4_btn1=Button(check_in,text="CHECK",font=("sans serif",18,"bold"),width=10,bg="#ffff00",command=check)
p4_btn2=Button(check_in,text="BACK",font=("sans serif",18,"bold"),width=10,bg="#ffff00",command=back3)
p4_e11.focus()
canvas8.place(x=650,y=0)
p4_lb1.place(x=30,y=30)
p4_e11.place(x=380,y=30)
p4_e12.place(x=480,y=30)
p4_e13.place(x=580,y=30)


p4_lb2.place(x=30,y=120)
p4_e21.place(x=380,y=120)
p4_e22.place(x=480,y=120)


p4_lb3.place(x=30,y=220)
p4_e31.place(x=380,y=220)
p4_e32.place(x=480,y=220)
p4_e33.place(x=580,y=220)


p4_lb4.place(x=30,y=320)
p4_e41.place(x=380,y=320)
p4_e42.place(x=480,y=320)

p4_btn1.place(x=320,y=520)
p4_btn2.place(x=50,y=520)

p4_lb5.place(x=30,y=420)
p4_option1.place(x=380,y=420)
check_in.withdraw()


check_details=Toplevel(check_in)
check_details.title("GUEST DETAILS")
check_details.configure(background="#b3ffff")
check_details.iconbitmap("logo.ico")
check_details.geometry("1200x600+200+100")

var2=StringVar()
var2.set("NO")

p5_lb1=Label(check_details,text="Guest id",font=("sans serif",18,"bold"),width=10,bg="#ffff00")
p5_lb2=Label(check_details,text="Room No.",font=("sans serif",18,"bold"),width=10,bg="#ffff00")
p5_e1=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=9)
p5_e2=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=9)

p5_lb3=Label(check_details,text="First Name",font=("sans serif",18,"bold"),width=10,bg="#ffff00")
p5_e3=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=9)
p5_lb4=Label(check_details,text="Last Name",font=("sans serif",18,"bold"),width=10,bg="#ffff00")
p5_e4=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=9)

p5_lb5=Label(check_details,text="Address",font=("sans serif",18,"bold"),width=10,bg="#ffff00")
p5_e5=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=70)

p5_lb6=Label(check_details,text="Occupation",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p5_e6=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=10)

p5_lb7=Label(check_details,text="Phone Number",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p5_e7=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=10)

p5_lb8=Label(check_details,text="AdharCard No.",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p5_e8=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=10)

p5_lb9=Label(check_details,text="No. of Adults",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p5_e9=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=10)



p5_lb10=Label(check_details,text="No. of Children",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p5_e10=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=10)


p5_lb11=Label(check_details,text="Vehicle",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p5_option1=OptionMenu(check_details,var2,"YES","NO")
p5_option1.config(indicatoron=0,width=120,height=25,font=("sans serif",16,"bold"),image=img,bg="#ffff80",compound='right')


p5_lb12=Label(check_details,text="Vehicle Company",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p5_e12=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=10)

p5_lb13=Label(check_details,text="Number Plate",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p5_e13=Entry(check_details,bd=3,font=("sans serif",18,"bold"),width=10)



p5_btn1=Button(check_details,text="BACK",font=("sans serif",18,"bold"),width=10,bg="#ffff00",command=back4)
p5_btn2=Button(check_details,text="SUBMIT",font=("sans serif",18,"bold"),width=10,bg="#ffff00",command=gdetails)

p5_lb1.place(x=20,y=30)
p5_lb2.place(x=20,y=130)
p5_e1.place(x=200,y=30)
p5_e2.place(x=200,y=130)
p5_btn1.place(x=400,y=500)
p5_btn2.place(x=600,y=500)

p5_lb3.place(x=20,y=230)
p5_e3.place(x=200,y=230)

p5_lb4.place(x=20,y=330)
p5_e4.place(x=200,y=330)

p5_lb5.place(x=20,y=430)
p5_e5.place(x=200,y=430)

p5_lb6.place(x=380,y=30)
p5_e6.place(x=640,y=30)
p5_lb8.place(x=380,y=130)
p5_e8.place(x=640,y=130)
p5_lb7.place(x=380,y=230)
p5_e7.place(x=640,y=230)
p5_lb9.place(x=380,y=330)
p5_e9.place(x=640,y=330)


p5_lb10.place(x=800,y=30)
p5_e10.place(x=1050,y=30)

p5_lb11.place(x=800,y=130)
p5_option1.place(x=1050,y=126)

p5_lb12.place(x=800,y=230)
p5_e12.place(x=1050,y=230)

p5_lb13.place(x=800,y=330)
p5_e13.place(x=1050,y=330)



check_details.withdraw()


rs=Toplevel(employee)
rs.title("Room Service")
rs.configure(background="#b3ffff")
rs.iconbitmap("logo.ico")
rs.geometry("1200x600+200+100")

var3=StringVar()
var3.set("Food")

var4=IntVar()
var4.set(100)
canvas5=Canvas(rs,width=800,height=600)

image5=ImageTk.PhotoImage(Image.open("F:\\project\\t1.jpg"))

canvas5.create_image(0,0,anchor=NW,image=image5)


p6_lb1=Label(rs,text="Room Number",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p6_e1=Entry(rs,bd=3,font=("sans serif",18,"bold"),width=14)


p6_lb2=Label(rs,text="Registered Name",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p6_e2=Entry(rs,bd=3,font=("sans serif",18,"bold"),width=14)

p6_lb3=Label(rs,text="Work",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p6_option1=OptionMenu(rs,var3,"Food","Towel","Bedsheet","Other")
p6_option1.config(indicatoron=0,width=150,height=25,font=("sans serif",16,"bold"),image=img,bg="#ffff80",compound='right')



p6_lb4=Label(rs,text="Other",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p6_e4=Entry(rs,bd=3,font=("sans serif",18,"bold"),width=14)

p6_lb5=Label(rs,text="Charge",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p6_option2=OptionMenu(rs,var4,100,200)
p6_option2.config(indicatoron=0,width=150,height=25,font=("sans serif",16,"bold"),image=img,bg="#ffff80",compound='right')

p6_btn1=Button(rs,text="BACK",font=("sans serif",18,"bold"),width=10,bg="#ffff00",command=back5)
p6_btn2=Button(rs,text="SUBMIT",font=("sans serif",18,"bold"),width=10,bg="#ffff00",command=rs_sub)


canvas5.place(x=520,y=0)

p6_e1.focus()

p6_lb1.place(x=20,y=30)
p6_e1.place(x=300,y=30)

p6_lb2.place(x=20,y=130)
p6_e2.place(x=300,y=130)

p6_lb3.place(x=20,y=230)
p6_option1.place(x=300,y=230)

p6_lb4.place(x=20,y=330)
p6_e4.place(x=300,y=330)

p6_lb5.place(x=20,y=430)
p6_option2.place(x=300,y=430)

p6_btn2.place(x=320,y=520)
p6_btn1.place(x=50,y=520)

rs.withdraw()


game=Toplevel(employee)
game.title("GAME ZONE")
game.configure(background="#b3ffff")
game.iconbitmap("logo.ico")
game.geometry("1200x600+200+100")

canvas6=Canvas(game,width=800,height=900)

image6=ImageTk.PhotoImage(Image.open("F:\\project\\t4.jpg"))

canvas6.create_image(0,0,anchor=NW,image=image6)


p7_lb1=Label(game,text="Room Number",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p7_e1=Entry(game,bd=3,font=("sans serif",18,"bold"),width=14)


p7_lb2=Label(game,text="Registered Name",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p7_e2=Entry(game,bd=3,font=("sans serif",18,"bold"),width=14)


p7_lb3=Label(game,text="Count(200 per person)",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p7_e3=Entry(game,bd=3,font=("sans serif",18,"bold"),width=14)

p7_lb4=Label(game,text="Time(100 per hour)",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p7_e4=Entry(game,bd=3,font=("sans serif",18,"bold"),width=14)

p7_btn1=Button(game,text="BACK",font=("sans serif",18,"bold"),width=10,bg="#ffff00",command=back6)
p7_btn2=Button(game,text="SUBMIT",font=("sans serif",18,"bold"),width=10,bg="#ffff00",command=game_sub)

p7_e1.focus()
canvas6.place(x=580,y=0)
p7_lb1.place(x=10,y=30)
p7_e1.place(x=340,y=30)

p7_lb2.place(x=10,y=130)
p7_e2.place(x=340,y=130)

p7_lb3.place(x=10,y=230)
p7_e3.place(x=340,y=230)

p7_lb4.place(x=10,y=330)
p7_e4.place(x=340,y=330)



p7_btn2.place(x=320,y=520)
p7_btn1.place(x=50,y=520)

game.withdraw()


rst=Toplevel(employee)
rst.title("RESTAURANT")
rst.configure(background="#b3ffff")
rst.iconbitmap("logo.ico")
rst.geometry("1200x600+200+100")


p8_lb1=Label(rst,text="BreakFast",font=("sans serif",18,"bold"),width=15,bg="#ffff00")


p8_lb11=Label(rst,text="Masala Dosa.... ₹70",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e11=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb12=Label(rst,text="Idli.... ₹50",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e12=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb13=Label(rst,text="Upma.... ₹60",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e13=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb14=Label(rst,text="Poha.... ₹40",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e14=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb2=Label(rst,text="Bevarages",font=("sans serif",18,"bold"),width=15,bg="#ffff00")
p8_lb21=Label(rst,text="Tea.... ₹40",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e21=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb22=Label(rst,text="Coffee.... ₹40",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e22=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb3=Label(rst,text="Indian Breads",font=("sans serif",18,"bold"),width=15,bg="#ffff00")

p8_lb31=Label(rst,text="Butter Naan.... ₹50",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e31=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb32=Label(rst,text="Paratha.... ₹40",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e32=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)


p8_lb33=Label(rst,text="Butter Roti.... ₹30",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e33=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb4=Label(rst,text="Rice",font=("sans serif",18,"bold"),width=15,bg="#ffff00")

p8_lb41=Label(rst,text="Biryani.... ₹200",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e41=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb42=Label(rst,text="Pulao.... ₹160",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e42=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)


p8_lb43=Label(rst,text="Jeera Rice .... ₹130",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e43=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)


p8_lb5=Label(rst,text="Sabji",font=("sans serif",18,"bold"),width=15,bg="#ffff00")

p8_lb51=Label(rst,text="Veg Handi.... ₹110",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e51=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb52=Label(rst,text="Paneer Tikka.... ₹150",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e52=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)


p8_lb53=Label(rst,text="Chana Masala.... ₹100",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e53=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)


p8_lb6=Label(rst,text="Desert",font=("sans serif",18,"bold"),width=15,bg="#ffff00")

p8_lb61=Label(rst,text="Gulab Jamun.... ₹100",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e61=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb62=Label(rst,text="Ice Cream.... ₹80",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e62=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)


p8_lb63=Label(rst,text="Brownie.... ₹120",font=("sans serif",18,"bold"),width=18,bg="#b3ffff",anchor="e",justify=RIGHT)
p8_e63=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=4)

p8_lb7=Label(rst,text="Room NO.",font=("sans serif",18,"bold"),width=18,bg="#b3ffff")
p8_e7=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=8)

p8_lb8=Label(rst,text="Registered Name",font=("sans serif",18,"bold"),width=18,bg="#b3ffff")
p8_e8=Entry(rst,bd=3,font=("sans serif",18,"bold"),width=12)





p8_btn1=Button(rst,text="BACK",font=("sans serif",14,"bold"),width=6,bg="#ffff00",command=back7)
p8_btn2=Button(rst,text="ORDER",font=("sans serif",14,"bold"),width=6,bg="#ffff00",command=order)

p8_e11.focus()




p8_lb1.place(x=40,y=20)
p8_lb11.place(x=10,y=80)
p8_e11.place(x=310,y=80)

p8_lb12.place(x=10,y=140)
p8_e12.place(x=310,y=140)

p8_lb13.place(x=10,y=200)
p8_e13.place(x=310,y=200)

p8_lb14.place(x=10,y=260)
p8_e14.place(x=310,y=260)

p8_lb2.place(x=40,y=340)

p8_lb21.place(x=10,y=400)
p8_e21.place(x=310,y=400)

p8_lb22.place(x=10,y=460)
p8_e22.place(x=310,y=460)

p8_lb3.place(x=440,y=20)
p8_lb31.place(x=400,y=80)
p8_e31.place(x=700,y=80)

p8_lb32.place(x=400,y=140)
p8_e32.place(x=700,y=140)

p8_lb33.place(x=400,y=200)
p8_e33.place(x=700,y=200)

p8_lb4.place(x=440,y=280)

p8_lb41.place(x=400,y=340)
p8_e41.place(x=700,y=340)

p8_lb42.place(x=400,y=400)
p8_e42.place(x=700,y=400)

p8_lb43.place(x=400,y=460)
p8_e43.place(x=700,y=460)

p8_lb5.place(x=830,y=20)
p8_lb51.place(x=790,y=80)
p8_e51.place(x=1090,y=80)

p8_lb52.place(x=790,y=140)
p8_e52.place(x=1090,y=140)

p8_lb53.place(x=790,y=200)
p8_e53.place(x=1090,y=200)

p8_lb6.place(x=830,y=280)

p8_lb61.place(x=790,y=340)
p8_e61.place(x=1090,y=340)

p8_lb62.place(x=790,y=400)
p8_e62.place(x=1090,y=400)

p8_lb63.place(x=790,y=460)
p8_e63.place(x=1090,y=460)

p8_lb7.place(x=220,y=540)
p8_e7.place(x=440,y=540)

p8_lb8.place(x=560,y=540)
p8_e8.place(x=810,y=540)

p8_btn2.place(x=1100,y=540)
p8_btn1.place(x=50,y=540)

rst.withdraw()

hk=Toplevel(employee)
hk.title("HOUSE KEEPING")
hk.configure(background="#b3ffff")
hk.iconbitmap("logo.ico")
hk.geometry("1200x600+200+100")

canvas7=Canvas(hk,width=1200,height=600)

image7=ImageTk.PhotoImage(Image.open("F:\\project\\t3.jpg"))

canvas7.create_image(0,0,anchor=NW,image=image7)


p9_lb1=Label(hk,text="Room Number",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p9_e1=Entry(hk,bd=3,font=("sans serif",18,"bold"),width=14)


p9_lb2=Label(hk,text="Registered Name",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p9_e2=Entry(hk,bd=3,font=("sans serif",18,"bold"),width=14)



p9_e1.focus()

p9_btn1=Button(hk,text="BACK",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=back8)
p9_btn2=Button(hk,text="SUBMIT",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=hk_sub)

p9_lb1.place(x=10,y=180)
p9_e1.place(x=340,y=180)
canvas7.place(x=580,y=0)
p9_lb2.place(x=10,y=300)
p9_e2.place(x=340,y=300)

p9_btn2.place(x=320,y=520)
p9_btn1.place(x=50,y=520)
hk.withdraw()


ad=Toplevel(root)
ad.title("ADMIN")
ad.configure(background="#b3ffff")
ad.iconbitmap("logo.ico")
ad.geometry("1200x600+200+100")

canvas3=Canvas(ad,width=1200,height=600)

image3=ImageTk.PhotoImage(Image.open("F:\\project\\test.png"))

canvas3.create_image(0,0,anchor=NW,image=image3)

p11_btn2=Button(ad,text="Guest Details",font=("sans serif",14,"bold"),width=18,bg="#ffff00",command=g_details)
p11_btn2.config(relief="groove")
p11_btn3=Button(ad,text="Employee Details",font=("sans serif",14,"bold"),width=18,bg="#ffff00",command=e_details)
p11_btn3.config(relief="groove")
p11_btn4=Button(ad,text="Recruit Employee",font=("sans serif",14,"bold"),width=18,bg="#ffff00",command=add_employee)
p11_btn4.config(relief="groove")


p11_btn1=Button(ad,text="BACK",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=back10)


p11_btn2.place(x=530,y=180)
p11_btn3.place(x=530,y=260)
p11_btn4.place(x=530,y=340)
p11_btn1.place(x=575,y=520)
canvas3.pack()

ad.withdraw()


def key(event):
	if(len(p12_e1.get())==1):
		g_details()


gd=Toplevel(ad)
gd.title("GUEST DETAILS")
gd.configure(background="#b3ffff")
gd.iconbitmap("logo.ico")
gd.geometry("1200x600+200+100")
p12_scroll1=ScrolledText(gd,width=106,height=20,font=("arial",14,"bold"))

p12_lb1=Label(gd,text="Enter Full Name",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p12_e1=Entry(gd,bd=3,font=("sans serif",18,"bold"),width=14)
p12_btn2=Button(gd,text="SEARCH",font=("sans serif",14,"bold"),width=12,bg="#ffff00",command=search)
p12_btn2.config(relief="groove")
p12_btn3=Button(gd,text="UPDATE",font=("sans serif",14,"bold"),width=12,bg="#ffff00",command=gupdate)
p12_btn3.config(relief="groove")
p12_btn4=Button(gd,text="DELETE",font=("sans serif",14,"bold"),width=12,bg="#ffff00",command=gdelete)
p12_btn4.config(relief="groove")
p12_e1.focus()

p12_btn1=Button(gd,text="BACK",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=back11)
p12_lb1.place(x=30,y=20)
p12_e1.place(x=360,y=20)
p12_scroll1.place(x=8,y=90)
p12_btn1.place(x=575,y=550)
p12_btn2.place(x=600,y=20)
p12_btn3.place(x=800,y=20)
p12_btn4.place(x=1000,y=20)
p12_e1.bind('<BackSpace>',key)
gd.withdraw()

gdu=Toplevel(gd)
gdu.title("GUEST DETAILS UPDATE")
gdu.configure(background="#b3ffff")
gdu.iconbitmap("logo.ico")
gdu.geometry("1200x600+200+100")

var5=StringVar()
var5.set("phone_no")
p13_option1=OptionMenu(gdu,var5,"address","phone_no","no_adults","no_children","occupation","Adharcard_no")
p13_option1.config(indicatoron=0,width=200,height=25,font=("sans serif",16,"bold"),image=img,bg="#ffff80",compound='right')

p13_e1=Entry(gdu,bd=3,font=("sans serif",18,"bold"),width=70)
p13_btn1=Button(gdu,text="BACK",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=back12)
p13_btn2=Button(gdu,text="UPDATE",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=update_sub)


p13_e1.focus()

p13_option1.place(x=20,y=100)
p13_e1.place(x=270,y=100)
p13_btn1.place(x=420,y=530)
p13_btn2.place(x=630,y=530)

gdu.withdraw()

rms=Toplevel(employee)
rms.title("ROOM STATUS")
rms.configure(background="#b3ffff")
rms.iconbitmap("logo.ico")
rms.geometry("1200x600+200+100")
p14_scroll1=ScrolledText(rms,width=106,height=20,font=("arial",14,"bold"))
p14_btn1=Button(rms,text="BACK",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=back13)
p14_lb1=Label(rms,text="ROOM STATUS",font=("sans serif",18,"bold"),width=18,bg="#ffff00")

p14_btn1.place(x=560,y=550)
p14_scroll1.place(x=8,y=90)
p14_lb1.place(x=510,y=20)
rms.withdraw()

ed=Toplevel(ad)
ed.title("Employee DETAILS")
ed.configure(background="#b3ffff")
ed.iconbitmap("logo.ico")
ed.geometry("1200x600+200+100")
p15_scroll1=ScrolledText(ed,width=106,height=20,font=("arial",14,"bold"))

p15_lb1=Label(ed,text="Enter Full Name",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p15_e1=Entry(ed,bd=3,font=("sans serif",18,"bold"),width=14)
p15_btn2=Button(ed,text="SEARCH",font=("sans serif",14,"bold"),width=12,bg="#ffff00",command=e_search)
p15_btn2.config(relief="groove")
p15_btn3=Button(ed,text="UPDATE",font=("sans serif",14,"bold"),width=12,bg="#ffff00",command=e_update)
p15_btn3.config(relief="groove")
p15_btn4=Button(ed,text="DELETE",font=("sans serif",14,"bold"),width=12,bg="#ffff00",command=e_delete)
p15_btn4.config(relief="groove")
p15_e1.focus()

def key(event):
	if(len(p15_e1.get())==1):
		e_details()
p15_btn1=Button(ed,text="BACK",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=back14)
p15_lb1.place(x=30,y=20)
p15_e1.place(x=360,y=20)
p15_scroll1.place(x=8,y=90)
p15_btn1.place(x=575,y=550)
p15_btn2.place(x=600,y=20)
p15_btn3.place(x=800,y=20)
p15_btn4.place(x=1000,y=20)
p15_e1.bind('<BackSpace>',key)
ed.withdraw()


edu=Toplevel(ed)
edu.title("EMPLOYEE DETAILS UPDATE")
edu.configure(background="#b3ffff")
edu.iconbitmap("logo.ico")
edu.geometry("1200x600+200+100")

var6=StringVar()
var6.set("salary")
p16_option1=OptionMenu(edu,var6,"phone","salary","duty")
p16_option1.config(indicatoron=0,width=200,height=25,font=("sans serif",16,"bold"),image=img,bg="#ffff80",compound='right')

p16_e1=Entry(edu,bd=3,font=("sans serif",18,"bold"),width=70)
p16_btn1=Button(edu,text="BACK",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=back15)
p16_btn2=Button(edu,text="UPDATE",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=eupdate_sub)


p16_e1.focus()

p16_option1.place(x=20,y=100)
p16_e1.place(x=270,y=100)
p16_btn1.place(x=420,y=530)
p16_btn2.place(x=630,y=530)

edu.withdraw()

ade=Toplevel(ad)
ade.title("RECRUIT EMPLOYEE")
ade.configure(background="#b3ffff")
ade.iconbitmap("logo.ico")
ade.geometry("1200x600+200+100")

p17_lb1=Label(ade,text="Employee ID",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p17_e1=Entry(ade,bd=3,font=("sans serif",18,"bold"),width=14)
p17_lb2=Label(ade,text="Employee Name",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p17_e2=Entry(ade,bd=3,font=("sans serif",18,"bold"),width=14)
p17_lb3=Label(ade,text="Salary",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p17_e3=Entry(ade,bd=3,font=("sans serif",18,"bold"),width=14)
p17_lb4=Label(ade,text="Date OF Joining",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p17_e4=Entry(ade,bd=3,font=("sans serif",18,"bold"),width=14)
p17_lb5=Label(ade,text="Post",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p17_e5=Entry(ade,bd=3,font=("sans serif",18,"bold"),width=14)
p17_lb6=Label(ade,text="Adharcard NO.",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p17_e6=Entry(ade,bd=3,font=("sans serif",18,"bold"),width=14)
p17_lb7=Label(ade,text="Phone No.",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p17_e7=Entry(ade,bd=3,font=("sans serif",18,"bold"),width=14)


p17_btn2=Button(ade,text="RECRUIT",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=Recruit)
p17_btn1=Button(ade,text="BACK",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=back16)
p17_btn1.place(x=420,y=530)
p17_btn2.place(x=630,y=530)


p17_lb1.place(x=10,y=20)

p17_e1.place(x=320,y=20)

p17_lb2.place(x=10,y=120)
p17_e2.place(x=320,y=120)

p17_lb3.place(x=10,y=220)
p17_e3.place(x=320,y=220)

p17_lb4.place(x=10,y=320)
p17_e4.place(x=320,y=320)

p17_lb5.place(x=10,y=420)
p17_e5.place(x=320,y=420)


p17_lb6.place(x=610,y=20)
p17_e6.place(x=920,y=20)


p17_lb7.place(x=610,y=120)
p17_e7.place(x=920,y=120)

p17_e2.focus()



ade.withdraw()

adlogin=Toplevel(root)
adlogin.title("The Peninsula")

adlogin.configure(background="#b3ffff")
adlogin.iconbitmap("logo.ico")

adlogin.geometry("1200x600+200+100")
canvas4=Canvas(adlogin,width=1200,height=600)

image4=ImageTk.PhotoImage(Image.open("F:\\project\\test.png"))

canvas4.create_image(0,0,anchor=NW,image=image4)

p18_lb1=Label(adlogin,text="Enter Registered Name",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p18_e1=Entry(adlogin,bd=3,font=("sans serif",18,"bold"),width=15)

p18_lb2=Label(adlogin,text="Enter Password",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p18_e2=Entry(adlogin,bd=3,font=("sans serif",18,"bold"),width=15,show="*")

p18_bt1=Button(adlogin,text="BACK",font=("sans serif",18,"bold"),bg="#ffff00",command=back17)
p18_bt2=Button(adlogin,text="LOGIN",font=("sans serif",18,"bold"),bg="#ffff00",command=adlogin1)

p18_e1.focus()

p18_bt1.place(x=460,y=500)

p18_bt2.place(x=680,y=500)

p18_lb1.place(x=390,y=200)
p18_e1.place(x=690,y=200)
p18_lb2.place(x=390,y=300)
p18_e2.place(x=690,y=300)
canvas4.pack()

adlogin.withdraw()

chout=Toplevel(employee)
chout.title("CHECK OUT")


chout.configure(background="#b3ffff")
chout.iconbitmap("logo.ico")

chout.geometry("1200x600+200+100")
p19_scroll1=ScrolledText(chout,width=50,height=26,font=("arial",14,"bold"))
p19_btn2=Button(chout,text="ENTER",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=ent)
p19_btn1=Button(chout,text="BACK",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=back18)
p19_btn3=Button(chout,text="CHECKOUT",font=("sans serif",14,"bold"),width=10,bg="#ffff00",command=bye)
p19_lb1=Label(chout,text="Enter Registered Name",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p19_e1=Entry(chout,bd=3,font=("sans serif",18,"bold"),width=13)

p19_lb2=Label(chout,text="Enter Room Number",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p19_e2=Entry(chout,bd=3,font=("sans serif",18,"bold"),width=13)


p19_lb3=Label(chout,text="Feedback",font=("sans serif",18,"bold"),width=18,bg="#ffff00")
p19_e3=Entry(chout,bd=3,font=("sans serif",18,"bold"))
p19_e1.focus()
p19_lb1.place(x=20,y=50)
p19_e1.place(x=330,y=50)
p19_lb2.place(x=20,y=150)
p19_e2.place(x=330,y=150)
p19_lb3.place(x=140,y=250)
p19_e3.place(x=80,y=320)
p19_e3.place(width=400,height=80)
p19_btn1.place(x=100,y=530)
p19_btn2.place(x=300,y=530)
chout.withdraw()
p19_scroll1.place(x=620,y=10)
root.mainloop()