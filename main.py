from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import *
import tkinter.messagebox as tmsg
##########################################################################

root = Tk()
root.title("ToDo - A task manager of your by Soumya Jana")
#######################################################################
reamining_task = []
com_list = []
save_task_val = 0




def save_task():

    
    i = task_val.get()
    j = cal.get_date()
    k = sub_task_val.get()
    print(i)
    with open('task.txt' , 'a') as f:
        f.write(f" {j} {i} --> {k}\n")
        f.close()
    list_of_reamining_task = []
    with open('task.txt' ,'r') as fi:
        data = fi.readlines()
        for line in data:
            # word = line.split(',')
            # print(word)
            list_of_reamining_task.append(line.split('\n'))
    tasklist.delete(0,END)
    print(list_of_reamining_task)
    for item in list_of_reamining_task:
        tasklist.insert(END,item[0])
        
    fi.close()
    print(tasklist.size())
    add1 = tasklist.size()
    add2 = completelist.size()
    add3 = add1+add2
    if add3 == 0:
        calculas = (100*add2)/1
    else:
        calculas = (100*add2)/add3
        # calculas = 100*(mark_as_completed_val/total_val)

    print(add2)
    print(add3)
    print(calculas)
    progress['value'] = calculas
    cal_var.set(f"you have {calculas} %  completed of your total task")
    root.update_idletasks() 


def mark_as_completed():
   
    list_of_reamining_task = []
    del_item_list = []
    main_list = []
    have_to_del = tasklist.curselection()

#for create a list and append item by task.txt file_____________________________________________________________
    with open('task.txt' ,'r') as fi:
        data = fi.readlines()
        for line in data:
            # word = line.split(',')
            # print(word)
            list_of_reamining_task.append(line.split('\n'))

#for append those item in a list called del_item_list for deleleting later____________________________________________
    for item in have_to_del:
        i = list_of_reamining_task[item]
        del_item_list.append(i)

#add del_item_list content on a txt file called completed.txt___________________________________________________________
    with open('completed.txt','a') as r:
        for item in del_item_list:
            r.write(f"{item[0]}\n")
    print(del_item_list)

#add the item of del-item_list in our gui litbox called completelist_________________________________________________________
    with open ('completed.txt','r') as q:
        dataa = q.readlines()
        for line in dataa:
            main_list.append(line.split('\n'))
    completelist.delete(0,END)
    for item in main_list:
        completelist.insert(END,item[0])

#delet the item from the tak.txt file for avoiding reuse__________________________________________________________________

    a_file = open("task.txt", "r")
    
    
    lines = a_file.readlines()
    print(lines)
    for item in del_item_list:
        print(item)
        for ite in list_of_reamining_task:
            if ite[0] == item[0]:
                list_of_reamining_task.remove(ite)
    print(list_of_reamining_task)

    with open('task.txt' , "w") as written:
        for item in list_of_reamining_task:
            print(item)
            written.write(f"{item[0]}\n")

    

    tasklist.delete(0,END)
    for item in list_of_reamining_task:
        tasklist.insert(END,item[0])

    print(tasklist.size())
    add1 = tasklist.size()
    add2 = completelist.size()
    add3 = add1+add2
    if add3 == 0:
        calculas = (100*add2)/1
    else:
        calculas = (100*add2)/add3
        # calculas = 100*(mark_as_completed_val/total_val)

    print(add2)
    print(add3)
    print(calculas)
    progress['value'] = calculas
    cal_var.set(f"you have {calculas} %  completed of your total task")
    root.update_idletasks() 

def clear_mark_as_completed():
   
    history = open('history.txt','a')
    with open('completed.txt','r') as overide:
        history.write(overide.read())
    history.close()
    history_list = []
    mAsC = []
    com_list = []
    with open('history.txt','r') as upload:
        upl = upload.readlines()
        for item in upl:
            history_list.append(item.split('\n'))
    print(history_list)
    for item in history_list:
        History.insert(END,item[0])
    open('completed.txt', 'w').close()
    with open ('completed.txt','r') as q:
        dataa = q.readlines()
        for line in dataa:
            com_list.append(line.split('\n'))
            k = k+1
    
        completelist.delete(0,END)
        for item in com_list:
            completelist.insert(END,item[0])
    add1 = tasklist.size()
    add2 = completelist.size()
    add3 = add1+add2
    if add3 == 0:
        calculas = (100*add2)/1
    else:
        calculas = (100*add2)/add3
        # calculas = 100*(mark_as_completed_val/total_val)

    print(add2)
    print(add3)
    print(calculas)
    progress['value'] = calculas
    cal_var.set(f"you have {calculas} %  completed of your total task")
    root.update_idletasks()


def clear_hitory_list():
    open('history.txt', 'w').close()
    History.delete(0,END)




def delet_selected_task():
    list_of_reamining_task = []
    del_item_list = []
    main_list = []
    have_to_del = tasklist.curselection()

#for create a list and append item by task.txt file_____________________________________________________________
    with open('task.txt' ,'r') as fi:
        data = fi.readlines()
        for line in data:
            # word = line.split(',')
            # print(word)
            list_of_reamining_task.append(line.split('\n'))

#for append those item in a list called del_item_list for deleleting later____________________________________________
    for item in have_to_del:
        i = list_of_reamining_task[item]
        del_item_list.append(i)



#delet the item from the tak.txt file for avoiding reuse__________________________________________________________________

    a_file = open("task.txt", "r")
    
    
    lines = a_file.readlines()
    print(lines)
    for item in del_item_list:
        print(item)
        for ite in list_of_reamining_task:
            if ite[0] == item[0]:
                list_of_reamining_task.remove(ite)
    print(list_of_reamining_task)

    with open('task.txt' , "w") as written:
        for item in list_of_reamining_task:
            print(item)
            written.write(f"{item[0]}\n")

    

    tasklist.delete(0,END)
    for item in list_of_reamining_task:
        tasklist.insert(END,item[0])
    print(tasklist.size())
    add1 = tasklist.size()
    add2 = completelist.size()
    add3 = add1+add2
    if add3 == 0:
        calculas = (100*add2)/1
    else:
        calculas = (100*add2)/add3
        # calculas = 100*(mark_as_completed_val/total_val)

    print(add2)
    print(add3)
    print(calculas)
    progress['value'] = calculas
    cal_var.set(f"you have {calculas} %  completed of your total task")
    root.update_idletasks()



    
######################################################################
frame1 = Frame(root)
frame1.pack(anchor = "nw",pady = 10)
Label(frame1,text = "Add task").grid(row = 0 , column = 0,padx = 10)
task_val = StringVar()
task_en = Entry(frame1,textvariable = task_val,width = 35)
task_en.grid(row = 0 , column = 1)
Label(frame1,text = "Add sub task").grid(row = 0 , column = 2,padx = 30)
sub_task_val = StringVar()
sub_task_en = Entry(frame1,textvariable = sub_task_val,width = 35)
sub_task_en.grid(row = 0 , column = 3)
Label(frame1,text = "date").grid(row = 0 , column = 4 , padx = 20)
cal = DateEntry(frame1, width=16, background='darkblue',
                    foreground='white', borderwidth=2)
cal.grid(row = 0 , column = 5, padx = 20)
######################################################################
frame2 = Frame(root)
frame2.pack(anchor = "nw")
b1 = Button(frame2,text = "save task",width = 25,command = save_task)
b1.config()
b1.grid(row = 0 , column = 0)
b2 = Button(frame2,text = "mark as completed",width = 25,command = mark_as_completed)
b2.config()
b2.grid(row = 0 , column = 1)
b3 = Button(frame2,text = "delet selected task",width = 25,command = delet_selected_task)
b3.config()
b3.grid(row = 0 , column = 2)
b4 = Button(frame2,text = "clear mark as completed list",command = clear_mark_as_completed)
b4.config()
b4.grid(row = 0 , column = 3)
b5 = Button(frame2,text = "clear history list ",width = 25,command = clear_hitory_list)
b5.config()
b5.grid(row = 0 , column = 4)
######################################################################
frame3 = Frame(root)
frame3.pack(anchor = "nw",pady=10 )
from tkinter.ttk import *
progress = Progressbar(frame3, orient = HORIZONTAL, 
              length = 800, mode = 'determinate')
progress.grid(row = 0 , column = 0,padx = 3)
from tkinter import *
cal_var = StringVar()
completed = Label(frame3,text = "you have 0 %  completed of your total task",textvariable = cal_var)
completed.grid(row = 0 , column = 1 , padx = 10)
#########################################################################
frame4 = Frame(root)
frame4.pack(anchor = "nw")
scrol1 = Scrollbar(frame4)
scr = Scrollbar(frame4,orient = 'horizontal')
scrol1.grid(row = 1 , column = 1)
tasklist = Listbox(frame4,width = 45 ,height = 26 ,selectmode = EXTENDED,yscrollcommand = scrol1.set,xscrollcommand = scr.set)
Label(frame4,text = "remaining task").grid(row = 0 , column = 0)
tasklist.grid(row = 1 , column = 0)
scrol1.config(command = tasklist.yview)
scr.grid(row = 2 , column = 0)
scr.config(command = tasklist.xview)
scrol2 = Scrollbar(frame4)
scr2 = Scrollbar(frame4,orient = 'horizontal')
scrol2.grid(row = 1 , column = 3)
completelist = Listbox(frame4,width = 43,height = 26 ,selectmode = EXTENDED,yscrollcommand = scrol2.set ,xscrollcommand = scr2.set)
Label(frame4,text = "completed task").grid(row = 0 , column = 2)
completelist.grid(row = 1 , column = 2)
scrol2.config(command = completelist.yview)
scr2.grid(row = 2 , column = 2)
scr2.config(command = tasklist.xview)
scrol3 = Scrollbar(frame4)
scr3 = Scrollbar(frame4,orient = 'horizontal')
scrol3.grid(row = 1 , column = 5)
History = Listbox(frame4,width = 43,height = 26 , yscrollcommand = scrol3.set ,xscrollcommand = scr3.set )
Label(frame4,text = "task history").grid(row = 0 , column = 4)
History.grid(row = 1 , column = 4)
scrol3.config(command = History.yview)
scr3.grid(row = 2 , column = 4)
scr3.config(command = tasklist.xview)
##############################################################################################################
frame5 = Frame(root)
frame5.pack(anchor = "nw",pady = 12)
fb = Button(frame5,text = "Help")
fb.config()
fb.grid(row = 0 , column = 0)
f1 = Button(frame5,text = "Clear History")
f1.config()
f1.grid(row = 0 , column = 1)
##########################################################################################################
j = 0
with open('task.txt' ,'r') as fi:
    data = fi.readlines()
    for line in data:
        # word = line.split(',')
        # print(word)
        reamining_task.append(line.split('\n'))
tasklist.delete(0,END)
print(reamining_task)
for item in reamining_task:
    tasklist.insert(END,item[0])
    j = j+1


#  --------------------------------------------
inn= 0
with open ('completed.txt','r') as q:
    dataa = q.readlines()
    for line in dataa:
        com_list.append(line.split('\n'))
    
    completelist.delete(0,END)
    for item in com_list:
        completelist.insert(END,item[0])
        inn = inn+1

#-------------------------------------
hislist = []
with open('history.txt','r') as upload:
    upl = upload.readlines()
    for item in upl:
        hislist.append(item.split('\n'))
print(hislist)
for item in hislist:
    History.insert(END,item[0])

total = inn+j
if total==0:
    # calculas = 100*(mark_as_completed_val/0.00001)
    calculas = (100*inn)/1
else:
    calculas = (100*inn)/total
    # calculas = 100*(mark_as_completed_val/total_val)

print(inn)
print(total)
print(calculas)
progress['value'] = calculas
cal_var.set(f"you have {calculas} %  completed of your total task")
root.update_idletasks() 

#############################################################################################
root.mainloop()
