from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.title('Rock, Paper, Scissors')

choices = {'rock': 0, 'paper': 1, 'scissor': 2}

frame = Frame(root, width=200, height=10, pady=100)
frame.pack()

user_label = Label(root)
comp_label = Label(root)

win_label = Label(root)

rock = Button(frame, text="ROCK", bg='grey', fg='black',
              height=1, padx=5, command=lambda: choose(0))
paper = Button(frame, text="PAPER", fg='black', height=1,
               padx=5, command=lambda: choose(1))
scissor = Button(frame, text="SCISSOR", bg='red', fg='black',
                 height=1, padx=5, command=lambda: choose(2))


def choose(choice):
    computer_choice = random.randint(0, 2)
    if choice == 0:
        user_label.configure(text='You choose Rock')
        if computer_choice == 0:
            comp_label.configure(text='Computer chooses Rock')
            win_label.configure(text='Tie')
        elif computer_choice == 1:
            comp_label.configure(text='Computer chooses Paper')
            win_label.configure(text='Loss')
        elif computer_choice == 2:
            comp_label.configure(text='Computer chooses Scissors')
            win_label.configure(text='Victory')
    elif choice == 1:
        user_label.configure(text='You choose Paper')
        if computer_choice == 0:
            comp_label.configure(text='Computer chooses Rock')
            win_label.configure(text='Victory')
        elif computer_choice == 1:
            comp_label.configure(text='Computer chooses Paper')
            win_label.configure(text='Tie')
        elif computer_choice == 2:
            comp_label.configure(text='Computer chooses Scissor')
            win_label.configure(text='Loss')
    elif choice == 2:
        user_label.configure(text='You choose scissor')
        if computer_choice == 0:
            comp_label.configure(text='Computer chooses Rock')
            win_label.configure(text='Loss')
        elif computer_choice == 1:
            comp_label.configure(text='Computer chooses Paper')
            win_label.configure(text='Victory')
        elif computer_choice == 2:
            comp_label.configure(text='Computer chooses Scissor')
            win_label.configure(text='Tie')
    else:
        win_label.configure(text='Invalid choice')


rock.pack(side=LEFT)
paper.pack(side=LEFT)
scissor.pack(side=LEFT)

rock.pack(side=LEFT)
paper.pack(side=LEFT)
scissor.pack(side=LEFT)

user_label.pack()
comp_label.pack()
win_label.pack()

root.mainloop()
