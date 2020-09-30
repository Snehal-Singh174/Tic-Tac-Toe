from tkinter import *
from tkinter import messagebox


def btn_click(num):
    global x,y
    global plyr_1,plyr_2
    from itertools import permutations
    set1=permutations([1,2,3])
    set2=permutations([4,5,6])
    set3=permutations([7,8,9])
    set4=permutations([1,4,7])
    set5=permutations([2,5,8])
    set6=permutations([3,6,9])
    set7=permutations([1,5,9])
    set8=permutations([3,5,7])
    
    for i in set1,set2,set3,set4,set5,set6,set7,set8:
	    for j in list(i):
		    player_1=all(elem in plyr_1 for elem in j)
		    player_2=all(elem in plyr_2 for elem in j)
		    if player_1==True:
			    messagebox.showinfo("RESULT----","Player 1 Won!!!")
			    break
		    elif player_2==True:
			    messagebox.showinfo("RESULT----","Player 2 Won!!!")
		    else:pass
    if num == 1:
        if x%2==0:
            y="X"
            plyr_1.append(num)
            print(plyr_1)
        elif x%2!=0:
            y="O"
            plyr_2.append(num)
            print(plyr_2)

        b1.config(text=y,fg="white")
        x=x+1

    if num == 2:
        if x%2==0:
            y="X"
            plyr_1.append(num)
            print(plyr_1)
        elif x%2!=0:
            y="O"
            plyr_2.append(num)
            print(plyr_2)

        b2.config(text=y,fg="white")
        x=x+1

    if num == 3:
        if x%2==0:
            y="X"
            plyr_1.append(num)
            print(plyr_1)
        elif x%2!=0:
            y="O"
            plyr_2.append(num)
            print(plyr_2)

        b3.config(text=y,fg="white")
        x=x+1

    if num == 4:
        if x%2==0:
            y="X"
            plyr_1.append(num)
            print(plyr_1)
        elif x%2!=0:
            y="O"
            plyr_2.append(num)
            print(plyr_2)

        b4.config(text=y,fg="white")
        x=x+1

    if num == 5:
        if x%2==0:
            y="X"
            plyr_1.append(num)
            print(plyr_1)
        elif x%2!=0:
            y="O"
            plyr_2.append(num)
            print(plyr_2)

        b5.config(text=y,fg="white")
        x=x+1

    if num == 6:
        if x%2==0:
            y="X"
            plyr_1.append(num)
            print(plyr_1)
        elif x%2!=0:
            y="O"
            plyr_2.append(num)
            print(plyr_2)

        b6.config(text=y,fg="white")
        x=x+1

    if num == 7:
        if x%2==0:
            y="X"
            plyr_1.append(num)
            print(plyr_1)
        elif x%2!=0:
            y="O"
            plyr_2.append(num)
            print(plyr_2)

        b7.config(text=y,fg="white")
        x=x+1

    if num == 8:
        if x%2==0:
            y="X"
            plyr_1.append(num)
            print(plyr_1)
        elif x%2!=0:
            y="O"
            plyr_2.append(num)
            print(plyr_2)

        b8.config(text=y,fg="white")
        x=x+1

    if num == 9:
        if x%2==0:
            y="X"
            plyr_1.append(num)
            print(plyr_1)
        elif x%2!=0:
            y="O"
            plyr_2.append(num)
            print(plyr_2)

        b9.config(text=y,fg="white")
        x=x+1

y=""
x=2
plyr_1=[]
plyr_2=[]

root=Tk()
root.title("Welcome to The TIC-TAC-TOE dev by Snehal-Singh")

l1=Label(root,text="Player 1 : X",font="times 15")
l1.grid(row=0,column=0)

l2=Label(root,text="Player 2 : O",font="times 15")
l2.grid(row=0,column=1)
        
b1=Button(root,bg="gray",width=20,height=10,command=lambda: btn_click(1))
b2=Button(root,bg="gray",width=20,height=10,command=lambda: btn_click(2))
b3=Button(root,bg="gray",width=20,height=10,command=lambda: btn_click(3))
b4=Button(root,bg="gray",width=20,height=10,command=lambda: btn_click(4))
b5=Button(root,bg="gray",width=20,height=10,command=lambda: btn_click(5))
b6=Button(root,bg="gray",width=20,height=10,command=lambda: btn_click(6))
b7=Button(root,bg="gray",width=20,height=10,command=lambda: btn_click(7))
b8=Button(root,bg="gray",width=20,height=10,command=lambda: btn_click(8))
b9=Button(root,bg="gray",width=20,height=10,command=lambda: btn_click(9))

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)

root.mainloop()
