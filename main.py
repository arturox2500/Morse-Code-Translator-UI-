import tkinter as tk
from tkinter import messagebox
BG = "#c3aed6"
Tit = "#09015f"
Language_List = ["English", "Morse"]
###################################### MAIN CODE ###########################################
morse_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}


def convert():
    answer.delete(1.0, "end")
    text = my_input.get("1.0", "end")[:-1]
    if variable1.get() == variable2.get():
        messagebox.showerror("Something went wrong...", "Can't translate from the same language")

    elif variable1.get() == "English" and variable2.get() == "Morse":
        result = encript(text)

    elif variable1.get() == "Morse" and variable2.get() == "English":
        result = decript(text)

    else:
        messagebox.showerror("Something went wrong...","select valid language")

    answer.insert('end -1 chars', result)
    return


def encript(text):
    text = text.upper()
    final_res = ""
    for letter in text:
        if letter != " ":
            final_res += morse_dict[letter] + " "
        else:
            final_res += " "
    return final_res


def decript(text):
    text += " "
    end_word = ""
    end_letter = ""

    for letter in text:
        if letter != " ":
            counter = 0
            end_letter += letter

        else:
            counter += 1

            if counter == 2:
                end_word += " "

            else:
                end_word += list(morse_dict.keys())[list(morse_dict.values()).index(end_letter)]
                end_letter = ""
    return end_word.capitalize()

########################################################### INTERFACE #######################################################################


window = tk.Tk()

variable1 = tk.StringVar(window)
variable2 = tk.StringVar(window)
variable1.set("From: ")
variable2.set("To: ")

window.title("Morse Code Translator")
window.config(padx=45, pady=10, bg=BG)
window.geometry('600x400')
window.maxsize(600,450)
window.minsize(600,450)


logo = tk.PhotoImage(file="images/morse code logo.png")
img_label = tk.Label(image=logo, bg=BG)
img_label.grid(row=1, column=0, columnspan=2, sticky='EW', pady=20)

title = tk.Label(text="Morse Code Translator", bg=BG, fg=Tit, font=("Arial", 25, "bold"))
title.grid(row=0, column=0, columnspan=2, sticky='EW')

my_input = tk.Text(width=30, height=10, borderwidth=5)
my_input.grid(row=3, column=0)

answer = tk.Text(width=30, height=10, borderwidth=5)
answer.grid(row=3, column=1)

from_language = tk.OptionMenu(window, variable1, *Language_List)
from_language.grid(row=2, column=0, pady=10)

to_language = tk.OptionMenu(window, variable2, *Language_List)
to_language.grid(row=2, column=1, pady=10)

translate_button = tk.Button(text="Translate", command=convert)
translate_button.grid(row=4, column=0, columnspan=2, pady=15)

window.mainloop()