from customtkinter import *


window = CTk()
window.title('program')
window.geometry("500x500")

text_field = CTkTextbox(window, width=480, height=400)
text_field.pack(pady=15)

text_entry = CTkEntry(window, width=500)
text_entry.pack(pady=20)

btn = CTkButton(window, text='Надіслати повідомлення', width=300, height=100)
btn.pack()

def show_menu(self):
    self.menu_frame.configure(width=self.menu_frame.winfo_width() + self.speed_animate_menu)
    if not self.menu_frame.winfo_width() >= 250 and self.is_show_menu:
        self.after(10, self.show_menu)
    elif self.menu_frame.winfo_width() >= 50 and not self.is_show_menu:
        self.after(10, self.show_menu)
        if self.label and self.entry:
            self.label.destroy()
            self.entry.destroy()


def adaptive_ui(self):
    self.menu_frame.configure(height=self.winfo_height())

    self.after(50, self.adaptive_ui)


window.configure(fg_color="lightblue")
window.mainloop()  
