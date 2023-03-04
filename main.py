import customtkinter
import check


root = customtkinter.CTk()
root.geometry("500x400")


frame = customtkinter.CTkFrame(master=root)
frame.pack(fill="both", expand=True)



entry = customtkinter.CTkEntry(master=frame, placeholder_text="URL")
entry.pack(pady=10)


label = customtkinter.CTkLabel(master=frame, text="")
label.pack()



def display_text():
    user = entry.get()
    user2 = check.short(user)
    label.configure(text=f"{user2}")
    print(user2)


button = customtkinter.CTkButton(master=frame, text="Click me!", command=display_text)
button.pack(pady=10)


root.mainloop()