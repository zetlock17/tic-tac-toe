from tkinter import *
from tkinter import messagebox
import random

b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0
a9 = 0
rndm = 0
tips = 'O'
run = True


def winner_b():
	messagebox.showinfo(' ', 'Вы проиграли!')
	exit()


def winner_x():
	messagebox.showinfo(' ', 'Вы выиграли!')
	exit()


def draw():
	messagebox.showinfo(' ', 'Ничья!')
	exit()


def main():
	if a1 == 1 and a2 == 1 and a3 == 1 and a4 == 1 and a5 == 1 and a6 == 1 and a7 == 1 and a8 == 1 and a9 == 1:
		draw()

	if b1 == 1 and b2 == 1 and b3 == 1:
		winner_b()

	elif b4 == 1 and b5 == 1 and b6 == 1:
		winner_b()

	elif b7 == 1 and b8 == 1 and b9 == 1:
		winner_b()

	elif b3 == 1 and b6 == 1 and b9 == 1:
		winner_b()

	elif b2 == 1 and b5 == 1 and b8 == 1:
		winner_b()

	elif b1 == 1 and b4 == 1 and b7 == 1:
		winner_b()

	elif b1 == 1 and b5 == 1 and b9 == 1:
		winner_b()

	elif b3 == 1 and b5 == 1 and b7 == 1:
		winner_b()

	elif x1 == 1 and x2 == 1 and x3 == 1:
		winner_x()

	elif x4 == 1 and x5 == 1 and x6 == 1:
		winner_x()

	elif x7 == 1 and x8 == 1 and x9 == 1:
		winner_x()

	elif x3 == 1 and x6 == 1 and x9 == 1:
		winner_x()

	elif x2 == 1 and x5 == 1 and x8 == 1:
		winner_x()

	elif x1 == 1 and x4 == 1 and x7 == 1:
		winner_x()

	elif x1 == 1 and x5 == 1 and x9 == 1:
		winner_x()

	elif x3 == 1 and x5 == 1 and x7 == 1:
		winner_x()

	elif tips == 'X':
		computer_tips()


def setText(text, ti, btn):
	global b1, b2, b3, b4, b5, b6, b7, b8, b9, x1, x2, x3, x4, x5, x6, x7, x8, x9, a1, a2, a3, a4, a4, a5, a6, a7, a8, a9, tips
	tips = ti

	if btn == 1:
		a1 = 1
		btn_1.config(text=text)

		if text == 'X':
			x1 = 1
			btn_1.config(fg='#cc0000')

		elif text == 'O':
			b1 = 1
			btn_1.config(fg='#0000cc')

		elif a2 == 1 and a3 == 1 and a4 == 1 and a5 == 1 and a6 == 1 and a7 == 1 and a8 == 1 and a9 == 1:
			draw()


	elif btn == 2:
		a2 = 1
		btn_2.config(text=text)

		if text == 'X':
			x2 = 1
			btn_2.config(fg='#cc0000')

		elif text == 'O':
			b2 = 1
			btn_2.config(fg='#0000cc')

		elif a1 == 1 and a3 == 1 and a4 == 1 and a5 == 1 and a6 == 1 and a7 == 1 and a8 == 1 and a9 == 1:
			draw()


	elif btn == 3:
		a3 = 1
		btn_3.config(text=text)

		if text == 'X':
			x3 = 1
			btn_3.config(fg='#cc0000')

		elif text == 'O':
			b3 = 1
			btn_3.config(fg='#0000cc')

		elif a1 == 1 and a2 == 1 and a4 == 1 and a5 == 1 and a6 == 1 and a7 == 1 and a8 == 1 and a9 == 1:
			draw()


	elif btn == 4:
		a4 = 1
		btn_4.config(text=text)

		if text == 'X':
			x4 = 1
			btn_4.config(fg='#cc0000')

		elif text == 'O':
			b4 = 1
			btn_4.config(fg='#0000cc')

		elif a1 == 1 and a2 == 1 and a3 == 1 and a5 == 1 and a6 == 1 and a7 == 1 and a8 == 1 and a9 == 1:
			draw()


	elif btn == 5:
		a5 = 1
		btn_5.config(text=text)

		if text == 'X':
			x5 = 1
			btn_5.config(fg='#cc0000')

		elif text == 'O':
			b5 = 1
			btn_5.config(fg='#0000cc')

		elif a1 == 1 and a2 == 1 and a3 == 1 and a4 == 1 and a6 == 1 and a7 == 1 and a8 == 1 and a9 == 1:
			draw()


	elif btn == 6:
		a6 = 1
		btn_6.config(text=text)

		if text == 'X':
			x6 = 1
			btn_6.config(fg='#cc0000')

		elif text == 'O':
			b6 = 1
			btn_6.config(fg='#0000cc')

		elif a1 == 1 and a2 == 1 and a3 == 1 and a4 == 1 and a5 == 1 and a7 == 1 and a8 == 1 and a9 == 1:
			draw()


	elif btn == 7:
		a7 = 1
		btn_7.config(text=text)

		if text == 'X':
			x7 = 1
			btn_7.config(fg='#cc0000')

		elif text == 'O':
			b7 = 1
			btn_7.config(fg='#0000cc')

		elif a1 == 1 and a2 == 1 and a3 == 1 and a4 == 1 and a5 == 1 and a6 == 1 and a8 == 1 and a9 == 1:
			draw()


	elif btn == 8:
		a8 = 1
		btn_8.config(text=text)

		if text == 'X':
			x8 = 1
			btn_8.config(fg='#cc0000')

		elif text == 'O':
			b8 = 1
			btn_8.config(fg='#0000cc')

		elif a1 == 1 and a2 == 1 and a3 == 1 and a4 == 1 and a5 == 1 and a6 == 1 and a7 == 1 and a9 == 1:
			draw()


	elif btn == 9:
		a9 = 1
		btn_9.config(text=text)

		if text == 'X':
			x9 = 1
			btn_9.config(fg='#cc0000')

		elif text == 'O':
			b9 = 1
			btn_9.config(fg='#0000cc')

		elif a1 == 1 and a2 == 1 and a3 == 1 and a4 == 1 and a5 == 1 and a6 == 1 and a7 == 1 and a8 == 1:
			draw()

	main()



def random_tips():
	global run
	run = True

	while run:
		rndm = random.randrange(1, 10)

		if rndm == 1:
			if b1 == 0 and x1 == 0:
				run = False
				setText('O', 'O', 1)

		elif rndm == 2:
			if b2 == 0 and x2 == 0:
				run = False
				setText('O', 'O', 2)

		elif rndm == 3:
			if b3 == 0 and x3 == 0:
				run = False
				setText('O', 'O', 3)

		elif rndm == 4:
			if b4 == 0 and x4 == 0:
				run = False
				setText('O', 'O', 4)

		elif rndm == 5:
			if b5 == 0 and x5 == 0:
				run = False
				setText('O', 'O', 5)

		elif rndm == 6:
			if b6 == 0 and x6 == 0:
				run = False
				setText('O', 'O', 6)

		elif rndm == 7:
			if b7 == 0 and x7 == 0:
				run = False
				setText('O', 'O', 7)

		elif rndm == 8:
			if b8 == 0 and x8 == 0:
				run = False
				setText('O', 'O', 8)

		elif rndm == 9:
			if b9 == 0 and x9 == 0:
				run = False
				setText('O', 'O', 9)



def computer_tips():

	if b2 == 1 and b3 == 1 and a1 == 0:
		setText('O', 'O', 1)

	elif b4 == 1 and b7 == 1 and a1 == 0:
		setText('O', 'O', 1)

	elif b5 == 1 and b9 == 1 and a1 == 0:
		setText('O', 'O', 1)


	elif b1 == 1 and b3 == 1 and a2 == 0:
		setText('O', 'O', 2)
			
	elif b5 == 1 and b8 == 1 and a2 == 0:
		setText('O', 'O', 2)


	elif b1 == 1 and b2 == 1 and a3 == 0:
		setText('O', 'O', 3)

	elif b6 == 1 and b9 == 1 and a3 == 0:
		setText('O', 'O', 3)
			
	elif b5 == 1 and b7 == 1 and a3 == 0:
		setText('O', 'O', 3)
			

	elif b1 == 1 and b7 == 1 and a4 == 0:
		setText('O', 'O', 4)
			
	elif b5 == 1 and b6 == 1 and a4 == 0:
		setText('O', 'O', 4)
			

	elif b1 == 1 and b9 == 1 and a5 == 0:
		setText('O', 'O', 5)
			
	elif b2 == 1 and b8 == 1 and a5 == 0:
		setText('O', 'O', 5)

	elif b3 == 1 and b7 == 1 and a5 == 0:
		setText('O', 'O', 5)
			
	elif b4 == 1 and b6 == 1 and a5 == 0:
		setText('O', 'O', 5)
			

	elif b3 == 1 and b9 == 1 and a6 == 0:
		setText('O', 'O', 6)
			
	elif b4 == 1 and b5 == 1 and a6 == 0:
		setText('O', 'O', 6)
			

	elif b1 == 1 and b4 == 1 and a7 == 0:
		setText('O', 'O', 7)
			
	elif b3 == 1 and b5 == 1 and a7 == 0:
		setText('O', 'O', 7)
			
	elif b8 == 1 and b9 == 1 and a7 == 0:
		setText('O', 'O', 7)
			

	elif b2 == 1 and b5 == 1 and a8 == 0:
		setText('O', 'O', 8)
			
	elif b7 == 1 and b9 == 1 and a8 == 0:
		setText('O', 'O', 8)
			

	elif b1 == 1 and b5 == 1 and a9 == 0:
		setText('O', 'O', 9)
			
	elif b3 == 1 and b6 == 1 and a9 == 0:
		setText('O', 'O', 9)
			
	elif b7 == 1 and b8 == 1 and a9 == 0:
		setText('O', 'O', 9)
			



	elif x2 == 1 and x3 == 1 and a1 == 0:
		setText('O', 'O', 1)
			
	elif x4 == 1 and x7 == 1 and a1 == 0:
		setText('O', 'O', 1)
			
	elif x5 == 1 and x9 == 1 and a1 == 0:
		setText('O', 'O', 1)
			

	elif x1 == 1 and x3 == 1 and a2 == 0:
		setText('O', 'O', 2)
			
	elif x5 == 1 and x8 == 1 and a2 == 0:
		setText('O', 'O', 2)
		

	elif x1 == 1 and x2 == 1 and a3 == 0:
		setText('O', 'O', 3)
		
	elif x6 == 1 and x9 == 1 and a3 == 0:
		setText('O', 'O', 3)
		
	elif x5 == 1 and x7 == 1 and a3 == 0:
		setText('O', 'O', 3)
		

	elif x1 == 1 and x7 == 1 and a4 == 0:
		setText('O', 'O', 4)
		
	elif x5 == 1 and x6 == 1 and a4 == 0:
		setText('O', 'O', 4)
		

	elif x1 == 1 and x9 == 1 and a5 == 0:
		setText('O', 'O', 5)
		
	elif x2 == 1 and x8 == 1 and a5 == 0:
		setText('O', 'O', 5)
		
	elif x3 == 1 and x7 == 1 and a5 == 0:
		setText('O', 'O', 5)
		
	elif x4 == 1 and x6 == 1 and a5 == 0:
		setText('O', 'O', 5)
		

	elif x3 == 1 and x9 == 1 and a6 == 0:
		setText('O', 'O', 6)
		
	elif x4 == 1 and x5 == 1 and a6 == 0:
		setText('O', 'O', 6)
		

	elif x1 == 1 and x4 == 1 and a7 == 0:
		setText('O', 'O', 7)
		
	elif x3 == 1 and x5 == 1 and a7 == 0:
		setText('O', 'O', 7)
		
	elif x8 == 1 and x9 == 1 and a7 == 0:
		setText('O', 'O', 7)
		

	elif x2 == 1 and x5 == 1 and a8 == 0:
		setText('O', 'O', 8)
		
	elif x7 == 1 and x9 == 1 and a8 == 0:
		setText('O', 'O', 8)
		

	elif x1 == 1 and x5 == 1 and a9 == 0:
		setText('O', 'O', 9)
		
	elif x3 == 1 and x6 == 1 and a9 == 0:
		setText('O', 'O', 9)
		
	elif x7 == 1 and x8 == 1 and a9 == 0:
		setText('O', 'O', 9)



	elif a5 == 0:
		setText('O', 'O', 5)
		


	elif x8 == 1 and x6 == 1 and a9 == 0:
		setText('O', 'O', 9)

	elif x2 == 1 and x6 == 1 and a3 == 0:
		setText('O', 'O', 3)

	elif x2 == 1 and x4 == 1 and a1 == 0:
		setText('O', 'O', 1)

	elif x8 == 1 and x4 == 1 and a7 == 0:
		setText('O', 'O', 7)



	elif x5 == 1 and x1 == 1 and a3 == 0: 
		setText('O', 'O', 3)

	elif x5 == 1 and x1 == 1 and a7 == 0: 
		setText('O', 'O', 7)


	elif x5 == 1 and x3 == 1 and a1 == 0:
		setText('O', 'O', 1)

	elif x5 == 1 and x3 == 1 and a9 == 0:
		setText('O', 'O', 9)


	elif x5 == 1 and x9 == 1 and a7 == 0:
		setText('O', 'O', 7)

	elif x5 == 1 and x9 == 1 and a3 == 0:
		setText('O', 'O', 3)


	elif x5 == 1 and x7 == 1 and a9 == 0:
		setText('O', 'O', 9)

	elif x5 == 1 and x7 == 1 and a1 == 0:
		setText('O', 'O', 1)



	elif a5 == 1 and a1 == 0:
		setText('O', 'O', 1)

	elif a5 == 1 and a3 == 0:
		setText('O', 'O', 3)

	elif a5 == 1 and a7 == 0:
		setText('O', 'O', 7)

	elif a5 == 1 and a9 == 0:
		setText('O', 'O', 9)



	elif a2 == 1 and a3 == 1:
		random_tips()

	elif a4 == 1 and a7 == 1:
		random_tips()

	elif a5 == 1 and a9 == 1:
		random_tips()

	elif a1 == 1 and a3 == 1:
		random_tips()

	elif a5 == 1 and a8 == 1:
		random_tips()

	elif a1 == 1 and a2 == 1:
		random_tips()

	elif a6 == 1 and a9 == 1:
		random_tips()

	elif a5 == 1 and a7 == 1:
		random_tips()

	elif a1 == 1 and a7 == 1:
		random_tips()

	elif a5 == 1 and a6 == 1:
		random_tips()

	elif a3 == 1 and a9 == 1:
		random_tips()

	elif a4 == 1 and a5 == 1:
		random_tips()

	elif a1 == 1 and a4 == 1:
		random_tips()

	elif a8 == 1 and a9 == 1:
		random_tips()

	elif a5 == 1 and a3 == 1:
		random_tips()

	elif a2 == 1 and a5 == 1:
		random_tips()

	elif a7 == 1 and a9 == 1:
		random_tips()

	elif a1 == 1 and a5 == 1:
		random_tips()

	elif a3 == 1 and a6 == 1:
		random_tips()

	elif a7 == 1 and a8 == 1:
		random_tips()



	else:
		random_tips()



def btn_1():
	if a1 == 0:
		setText('X', 'X', 1)


def btn_2():
	if a2 == 0:
		setText('X', 'X', 2)

def btn_3():
	if a3 == 0:
		setText('X', 'X', 3)


def btn_4():
	if a4 == 0:
		setText('X', 'X', 4)


def btn_5():
	if a5 == 0:
		setText('X', 'X', 5)


def btn_6():
	if a6 == 0:
		setText('X', 'X', 6)


def btn_7():
	if a7 == 0:
		setText('X', 'X', 7)


def btn_8():
	if a8 == 0:
		setText('X', 'X', 8)


def btn_9():
	if a9 == 0:
		setText('X', 'X', 9)
	


root = Tk()
root.title('Tic-Tac-Toe')

btn_1 = Button(text='-', font='Arial 100', bg='#DCDCDC', command=btn_1)
btn_2 = Button(text='-', font='Arial 100', bg='#DCDCDC', command=btn_2)
btn_3 = Button(text='-', font='Arial 100', bg='#DCDCDC', command=btn_3)
btn_4 = Button(text='-', font='Arial 100', bg='#DCDCDC', command=btn_4)
btn_5 = Button(text='-', font='Arial 100', bg='#DCDCDC', command=btn_5)
btn_6 = Button(text='-', font='Arial 100', bg='#DCDCDC', command=btn_6)
btn_7 = Button(text='-', font='Arial 100', bg='#DCDCDC', command=btn_7)
btn_8 = Button(text='-', font='Arial 100', bg='#DCDCDC', command=btn_8)
btn_9 = Button(text='-', font='Arial 100', bg='#DCDCDC', command=btn_9)

btn_1.grid(row = 0, column = 0)
btn_2.grid(row = 0, column = 1)
btn_3.grid(row = 0, column = 2)
btn_4.grid(row = 1, column = 0)
btn_5.grid(row = 1, column = 1)
btn_6.grid(row = 1, column = 2)
btn_7.grid(row = 2, column = 0)
btn_8.grid(row = 2, column = 1)
btn_9.grid(row = 2, column = 2)


root.mainloop()