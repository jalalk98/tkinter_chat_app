from tkinter import *
import getpass
import threading

class tabs():

    def hide_additional_frames(self):
        try:
            self.frame_web_form.forget()  # hide the additional frame
        except AttributeError as e:
             print(e)
        self.window.geometry("400x400+200+100")
        self.text_frame.pack(expand=1,fill=BOTH)
        self.text_box.config(width=10, height=8)
        self.text_box.pack(expand=True,fill=BOTH)

    def display_web_frame(self):

        print("display tab method is running")
        self.text_frame.forget()
        self.entry_frame.forget()
        self.send_button_frame.forget()
        self.listbox_suggestion_frame.forget()

        self.window.geometry("750x600")

        if "pearl" in self.ob.lower():
            self.display_pearl_web_form()
        elif "smart" in self.ob.lower():
            self.display_smart_web_form()

        self.text_frame.pack(side=TOP, anchor="nw",expand=1,fill=BOTH)
        self.text_box.config(width=35, height=13)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        self.entry_frame.pack(side=BOTTOM, anchor='sw')
        self.entry_field.config(width=3)
        self.send_button_frame.pack(side=RIGHT, anchor='se')

    def display_pearl_web_form(self):
        try:
            self.frame_web_form.forget()  # if the frame is displayed then hide it
        except AttributeError as e:
            print(e)

        self.frame_web_form = Frame(self.window, width=400, height=400, bg="blue")
        self.frame_web_form.pack(side=RIGHT, anchor='ne', expand=1, fill=BOTH)  # ,fill=Y,expand=1,anchor='ne')

        self.button_submit = Button(self.frame_web_form, text="SUBMIT",command=self.run_browser_threaded_pearl)
        self.button_submit.pack(side=BOTTOM, padx=10, pady=10, anchor="center")

        self.userid_var = StringVar()
        self.label_userid = Label(self.frame_web_form, text="USER ID")
        self.label_userid.pack(side=LEFT,padx=10,pady=10,anchor='nw')
        self.entry_userid = Entry(self.frame_web_form,textvariable=self.userid_var)
        self.entry_userid.pack(side=LEFT,padx=10,pady=10,anchor='nw')
        self.userid_var.set(getpass.getuser())  # getting the user id using getpass module
        self.entry_userid.bind("<Key>",self.do_white_colour)

        self.label_password = Label(self.frame_web_form, text="PASSWORD")
        self.label_password.pack(side=LEFT,padx=10,pady=10,anchor='nw')
        self.entry_password = Entry(self.frame_web_form,show="*")
        self.entry_password.pack(side=LEFT,padx=10,pady=10,anchor='nw')
        self.entry_password.bind("<Key>",self.do_white_colour)
        self.frame_web_form.after(200,lambda:self.entry_password.focus()) # to set the focus with some delay

    def display_smart_web_form(self):
        try:
            self.frame_web_form.forget()  # if the frame is displayed then hide it
        except AttributeError as e:
            print(e)

        self.frame_web_form = Frame(self.window, width=400, height=400, bg="green")
        self.frame_web_form.pack(side=RIGHT, anchor='ne', expand=1, fill=BOTH)  # ,fill=Y,expand=1,anchor='ne')

        self.button_submit = Button(self.frame_web_form, text="SUBMIT",command=self.run_browser_threaded_smart)
        self.button_submit.pack(side=BOTTOM, padx=10, pady=10, anchor="center")

        self.userid_var = StringVar()
        self.label_userid = Label(self.frame_web_form, text="USER ID")
        self.label_userid.pack(side=LEFT, padx=10, pady=10, anchor='nw')
        self.entry_userid = Entry(self.frame_web_form, textvariable=self.userid_var)
        self.entry_userid.pack(side=LEFT, padx=10, pady=10, anchor='nw')
        self.userid_var.set(getpass.getuser())  # getting the user id using getpass module
        self.entry_userid.bind("<Key>",self.do_white_colour)


        self.label_password = Label(self.frame_web_form, text="PASSWORD")
        self.label_password.pack(side=LEFT, padx=10, pady=10, anchor='nw')
        self.entry_password = Entry(self.frame_web_form, show="*")
        self.entry_password.pack(side=LEFT, padx=10, pady=10, anchor='nw')
        self.entry_password.bind("<Key>", self.do_white_colour)
        self.frame_web_form.after(200, lambda: self.entry_password.focus())  # to set the focus with some delay

    def do_red_colour(self,entry_widget):
        entry_widget.config(bg="red")

    def check_all_entry_boxes_has_value(self):
        for entry in filter(lambda w:isinstance(w,Entry), self.frame_web_form.children.values()):  #
            if entry.get() == "":
                self.do_red_colour(entry)
                return False
        return True

    def do_white_colour(self,event):
        event.widget.config(bg="white")