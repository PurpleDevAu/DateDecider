import tkinter as tk

import dbAccessor as data

def main():

    print("in")
    window = tk.Tk()
    window.rowconfigure(0, minsize=50, weight=1)

    current_row = 0

    person_name_label = tk.Label(text="Name")
    person_name_entry = tk.Entry()
    person_name_label.grid(row=current_row, column=0)
    person_name_entry.grid(row=current_row, column=1)
    def get_peep():
        data.add_peep(person_name_entry.get())
    person_add = tk.Button(master=window, text="Add Person", command=get_peep) 
    current_row = current_row + 1
    person_add.grid(row=current_row, column=1)

    current_row = current_row + 1

    domain_key_label = tk.Label(text="Group")
    domain_key_entry = tk.Entry()
    domain_key_label.grid(row=current_row, column=0)
    domain_key_entry.grid(row=current_row, column=1)
    def get_domain_key():
        data.add_domain_key(domain_key_entry.get())
    domain_key_add = tk.Button(master=window, text="Add Person", command=get_domain_key) 
    current_row = current_row + 1
    domain_key_add.grid(row=current_row, column=1)


    window.mainloop()

main()