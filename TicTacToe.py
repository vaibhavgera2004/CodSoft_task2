import tkinter as tk
from tkinter import messagebox
import math

# Initialize game state
board = [' ' for _ in range(9)]
buttons = []

# Check winner
def check_winner(board, player):
    win_conditions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    return any(all(board[i]==player for i in condition) for condition in win_conditions)

def is_draw(board):
    return ' ' not in board

def minimax(board, depth, is_max):
    if check_winner(board,'O'): return 1
    if check_winner(board,'X'): return -1
    if is_draw(board): return 0
    if is_max:
        best=-math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='O'
                score=minimax(board,depth+1,False)
                board[i]=' '
                best=max(best,score)
        return best
    else:
        best=math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='X'
                score=minimax(board,depth+1,True)
                board[i]=' '
                best=min(best,score)
        return best

def ai_move():
    best_score=-math.inf
    move=None
    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            score=minimax(board,0,False)
            board[i]=' '
            if score>best_score:
                best_score=score
                move=i
    board[move]='O'
    buttons[move].config(text='O', state='disabled', disabledforeground='red')
    check_game_end()

def check_game_end():
    if check_winner(board,'O'):
        if messagebox.askyesno('Game Over','AI wins! Do you want to play again?'):
            reset_board()
        else:
            window.destroy()
    elif check_winner(board,'X'):
        if messagebox.askyesno('Game Over','You win! Do you want to play again?'):
            reset_board()
        else:
            window.destroy()
    elif is_draw(board):
        if messagebox.askyesno('Game Over','It is a draw! Do you want to play again?'):
            reset_board()
        else:
            window.destroy()

def on_click(index):
    if board[index]==' ':
        board[index]='X'
        buttons[index].config(text='X', state='disabled', disabledforeground='blue')
        check_game_end()
        if not check_winner(board,'X') and not is_draw(board):
            ai_move()

def reset_board():
    global board
    board=[' ' for _ in range(9)]
    for btn in buttons:
        btn.config(text=' ', state='normal')

# Tkinter window design
window=tk.Tk()
window.title('Tic-Tac-Toe AI')
window.configure(bg='#f0f0f0')

for i in range(9):
    btn=tk.Button(window, text=' ', font=('Arial',40), width=5, height=2,
                  bg='white', activebackground='#ddd',
                  command=lambda i=i:on_click(i))
    btn.grid(row=i//3,column=i%3,padx=5,pady=5)
    buttons.append(btn)

window.mainloop()