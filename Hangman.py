import tkinter as tk
import random

# WORDS
words = ["skola", "pappersark", "kaffekopp", "python", "stol", "cykel"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6


def guess():
    global attempts
    letter = entry.get().lower()
    entry.delete(0, tk.END)




    if letter in word:
        for i, ch in enumerate(word):
            if ch == letter:
                guessed[i] = letter

    else:

        attempts -= 1


    label_word.config(text=" ".join(guessed))
    label_info.config(text=f"Guesses left: {attempts}")

    if "_" not in guessed:
        label_info.config(text=" 🔥 You won")
        guess_button.config(state="disabled")
        play_again_button.pack(pady=20)

    elif attempts == 0:
        label_info.config(text=f" You loose!!! The word was: {word}")
        guess_button.config(state="disabled")
        play_again_button.pack(pady=20)

    
def reset_hangman():
    global word, guessed, attempts
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6

    label_word.config(text="_".join(guessed))
    label_info.config(text=f"Guesses left: {attempts}")
    guess_button.config(state="normal")
    play_again_button.pack_forget()




    

# GUI
root = tk.Tk()
root.title("Hangman")
root.geometry("600x600")  # <- fixed the dot here

# LABEL
label_word = tk.Label(root, font=("Arial", 24), text="_".join(guessed))
label_word.pack(pady=15)


# LABEL INFO
label_info = tk.Label(root, text=f"Guesses left: {attempts}")
label_info.pack()


# ENTRY BOX
entry = tk.Entry(root)
entry.pack(pady=5)


# BUTTON 1
guess_button = tk.Button(root, text="Guess", command=guess)
guess_button.pack(pady=25)


# BUTTON 2
play_again_button = tk.Button(root, text="Play again?", command=reset_hangman)
play_again_button.pack(pady=25)



    

root.mainloop()