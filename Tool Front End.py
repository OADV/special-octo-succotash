from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def update(rows):
  trv.delete(*trv.get_children())
  for i in rows:
    trv.insert('','end', values = i)

def search():
  q2 = q.get()
  query = "SELECT FILE_NAME, PLANT, DIST_KM, MAX_uSv, MEAN_uSv, MIN_uSv, LENGTH_Km, PLANT_ID from Nuclear_Facility_Locations WHERE PLANT LIKE '%"+q2+"%' OR MEAN_uSv LIKE '%"+q2+"%'"
  cursor.execute(query)
  rows=cursor.fetchall()
  update(rows)

def clear():
  query = "SELECT FILE_NAME, PLANT, DIST_KM, MAX_uSv, MEAN_uSv, MIN_uSv, LENGTH_Km, PLANT_ID from Nuclear_Facility_Locations"
  cursor.execute(query)
  ent.delete(0, END)
  rows=cursor.fetchall()
  update(rows)

def getrow(event):
  item = trv.item(trv.focus())
  t1.set(item['values'][0])
  t2.set(item['values'][1])
  t3.set(item['values'][2])
  t4.set(item['values'][3])
  t5.set(item['values'][4])
  t6.set(item['values'][5])
  t7.set(item['values'][6])
  t8.set(item['values'][7])

def update_plant():
  file_name = t1.get()
  plant = t2.get()
  dist_km = t3.get()
  max_usv = t4.get()
  mean_usv = t5.get()
  min_usv = t6.get()
  length_km = t7.get()
  plt_id = t8.get()

  if messagebox.askyesno("Confirm Please", "Are you sure you want to add this?"):
    query = "UPDATE Nuclear_Facility_Locations SET FILE_NAME = %s, PLANT = %s, DIST_KM = %s, MAX_uSv = %s, MEAN_uSv = %s, MIN_uSv = %s, LENGTH_Km = %s WHERE PLANT_ID = %s"
    cursor.execute(query, (file_name, plant, dist_km, max_usv, mean_usv, min_usv, length_km, plt_id))
    clear()
  else:
    return True
  ent1.delete(0, END)
  ent2.delete(0, END)
  ent3.delete(0, END)
  ent4.delete(0, END)
  ent5.delete(0, END)
  ent6.delete(0, END)
  ent7.delete(0, END)
  ent8.delete(0, END)
  mydb.commit()

 

def add_new():
  file_name = t1.get()
  plant = t2.get()
  dist_km = t3.get()
  max_usv = t4.get()
  mean_usv = t5.get()
  min_usv = t6.get()
  length_km = t7.get()
  query = "INSERT INTO Nuclear_Facility_Locations(FILE_NAME, PLANT, DIST_KM, MAX_uSv, MEAN_uSv, MIN_uSv, LENGTH_Km, PLANT_ID) VALUES(%s, %s, %s, %s, %s, %s, %s, NULL)"
  cursor.execute(query, (file_name, plant, dist_km, max_usv, mean_usv, min_usv, length_km))
  ent1.delete(0, END)
  ent2.delete(0, END)
  ent3.delete(0, END)
  ent4.delete(0, END)
  ent5.delete(0, END)
  ent6.delete(0, END)
  ent7.delete(0, END)
  ent8.delete(0, END)
  clear()
  mydb.commit()
  



def delete_plant():
  plant_id = t8.get()
  if messagebox.askyesno("Confirm Delete?", "Are you sure you want to delete this?"):
     query = "DELETE FROM Nuclear_Facility_Locations WHERE PLANT_ID = "+plant_id
     cursor.execute(query)
     mydb.commit()
     clear()
  else:
    return True
  ent1.delete(0, END)
  ent2.delete(0, END)
  ent3.delete(0, END)
  ent4.delete(0, END)
  ent5.delete(0, END)
  ent6.delete(0, END)
  ent7.delete(0, END)
  ent8.delete(0, END)


def Exit():
  if messagebox.askyesno("MYSQL Connection", "Are you sure you would like to exit?"):
    root.destroy()
  else:
    return
  

mydb = mysql.connector.connect(host='LOCALHOST',database='Capstone1', user='root', password='')
cursor= mydb.cursor()

root = Tk()
q = StringVar()
q3 = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()

wrapper1 = LabelFrame(root, text= "Nuclear Facility")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(expand="yes", padx=20, pady=10)
wrapper3.pack(expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8), show="headings", height="10")
trv.columnconfigure(0, weight=10)
trv.pack()

trv.heading(1, text='FILE_NAME')
trv.heading(2, text='PLANT')
trv.heading(3, text='DIST_KM')
trv.heading(4, text='MAX_uSv')
trv.heading(5, text='MEAN_uSv')
trv.heading(6, text='MIN_uSv')
trv.heading(7, text='LENGTH_Km')
trv.heading(8, text='PLANT_ID')

trv.bind('<Double 1>', getrow)

query = "SELECT FILE_NAME, PLANT, DIST_KM, MAX_uSv, MEAN_uSv, MIN_uSv, LENGTH_Km, PLANT_ID from Nuclear_Facility_Locations"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

#Search Section 
lbl = Label(wrapper2, text="Search Plant Location")
lbl.grid(row=0, column = 0, padx=5, pady=3)
ent = Entry(wrapper2, textvariable=q, bd = 1)
ent.grid(row=0,column = 1, padx=5, pady=3)

lbl = Label(wrapper2, text="Search Mean Microsieverts")
lbl.grid(row=1, column = 0, padx=5, pady=3)
ent = Entry(wrapper2, textvariable=q3, bd = 1)
ent.grid(row=1, column = 1, padx=5, pady=3)

btn = Button(wrapper2, text="Search", command = search)
btn.grid(row=2, column = 1, padx=5, pady=3)
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.grid(row=2, column = 0, padx=5, pady=3)

#User Data Section
lbl1 = Label(wrapper3, text="File Name")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t1, width = 57, bd = 1)
ent1.grid(row=0, column=1, padx=5, pady=5)

lbl2 = Label(wrapper3, text="Nuclear Facility Name")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t2, width = 57, bd = 1)
ent2.grid(row=1, column=1, padx=5, pady=5)

lbl3 = Label(wrapper3, text="Distance(Km)")
lbl3.grid(row=2, column = 0, padx=5, pady = 3)
ent3 = Entry(wrapper3, textvariable=t3, width = 57, bd = 1)
ent3.grid(row=2, column = 1, padx=5, pady = 3)

lbl4 = Label(wrapper3, text="Max(uSv)")
lbl4.grid(row=3, column = 0, padx = 5, pady=3)
ent4 = Entry(wrapper3, textvariable=t4, width = 57, bd = 1)
ent4.grid(row=3, column = 1, padx = 5, pady=3)

lbl5 = Label(wrapper3, text="Mean(uSv)")
lbl5.grid(row=4, column = 0, padx = 5, pady=3)
ent5 = Entry(wrapper3, textvariable=t5, width = 57, bd = 1)
ent5.grid(row=4, column = 1, padx = 5, pady=3)

lbl6 = Label(wrapper3, text="Min(uSv)")
lbl6.grid(row=5, column = 0, padx = 5, pady=3)
ent6 = Entry(wrapper3, textvariable=t6, width = 57, bd = 1)
ent6.grid(row=5, column = 1, padx = 5, pady=3)

lbl7 = Label(wrapper3, text="Lenght(Km)")
lbl7.grid(row=6, column = 0, padx = 5, pady=3)
ent7 = Entry(wrapper3, textvariable=t7, width = 57, bd = 1)
ent7.grid(row=6, column = 1, padx = 5, pady=3)

lbl8 = Label(wrapper3, text="Plant(ID)")
lbl8.grid(row=7, column = 0, padx = 5, pady=3)
ent8 = Entry(wrapper3, textvariable=t8, width = 57, bd = 1)
ent8.grid(row=7, column = 1, padx = 5, pady=3)

up_btn = Button(wrapper3, text = "Update", command = update_plant)
add_btn = Button(wrapper3, text="Add New", command=add_new)
delete_btn = Button(wrapper3, text="Delete", command=delete_plant)
exit_btn = Button(wrapper3, text="Exit", command=Exit)

up_btn.grid(row=1, column = 3, padx=5, pady=3)
add_btn.grid(row=3, column = 3, padx=5, pady=3)
delete_btn.grid(row=5, column = 3, padx=5, pady=3)
exit_btn.grid(row=7, column = 3, padx=5, pady=3)

root.title("Health Canada")
root.geometry("1445x800")


root.mainloop()