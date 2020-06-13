from tkinter import *
import time
from chat_bot import bot_class
import threading
from font_colour_menus import font_colour_menus
from suggestion_list import suggestion_list
from tabs import tabs
from hyperlink import HyperlinkManager
import webbrowser

global window_size

saved_username = ["You"]
window_size = "400x400+200+100"

class ChatInterface(bot_class,font_colour_menus,suggestion_list,tabs,threading.Thread):

    def __init__(self):
        bot_class.__init__(self)
        font_colour_menus.__init__(self)
        suggestion_list.__init__(self)
        tabs.__init__(self)
        threading.Thread.__init__(self)
        self.start()

    def callback_for_opening_browser(self):
        webbrowser.open(self.ob)

    def replies(self):
        if "http" not in self.ob:
            self.text_box.insert(END,self.pr)    # if its not an link so reply simple
        if "fill the form" in self.ob.lower():
            self.display_web_frame()
        elif "hidden" in self.ob:
            self.hide_additional_frames()        # hide the additional unrequired frames
        elif "http" in self.ob:
            self.text_box.insert(END, "PyBot : This is the ")  # insert half text
            self.text_box.insert(END, "Link" + "\n", self.hyperlink.add(self.callback_for_opening_browser)) # add hyperlink for ob variable

    def send_message_insert(self, message):
        user_input = self.entry_field.get()
        pr1 = "Human : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.ob = self.chat(user_input)
        self.pr = "PyBot : " + str(self.ob) + "\n"
        self.text_box.configure(state=NORMAL)

        self.replies()

        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.sent_label.config(text=(str(time.strftime("Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p'))))
        self.entry_field.delete(0, END)
        self.entry_field.focus()
        time.sleep(0)

    def callback(self):
        self.window.destroy()

    def close(self,event=""):
        self.window.wm_state('iconic')

    def downkey_pressed(self, event):
        self.listbox_suggestion.focus_set()  # to set the focus on the listbox

    def up_arrow(self,event):
        w = event.widget
        try:
            index = int(w.curselection()[0])
        except IndexError as e:
            print(e)
        if index == 0:
            self.entry_field.focus_set()  # to bring the focus to the entry box
            self.entry_field.icursor("end")  # to move the cursor at the end of the entry box

    def on_select(self,event):
        # display element selected on list
        try:
            self.s.set(event.widget.get(event.widget.curselection()))  # to put the current selected value in the var "s" which is attached entry widget
        except:
            self.s.set(event.widget.get(1))

    def run(self):
        self.window = Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.callback)

        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
        self.font = "Verdana 10"

        menu = Menu(self.window)
        self.window.config(menu=menu, bd=5)
        # Menu bar

        # File
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
        # file.add_command(label="Save Chat Log", command=self.save_chat)
        file.add_command(label="Clear Chat", command=self.clear_chat)
        #  file.add_separator()
        file.add_command(label="Exit", command=self.chatexit)
        # Options
        options = Menu(menu, tearoff=0)
        menu.add_cascade(label="Options", menu=options)

        # username

        # font
        font = Menu(options, tearoff=0)
        options.add_cascade(label="Font", menu=font)
        font.add_command(label="Default", command=self.font_change_default)
        font.add_command(label="Times", command=self.font_change_times)
        font.add_command(label="System", command=self.font_change_system)
        font.add_command(label="Helvetica", command=self.font_change_helvetica)
        font.add_command(label="Fixedsys", command=self.font_change_fixedsys)

        # color theme
        color_theme = Menu(options, tearoff=0)
        options.add_cascade(label="Color Theme", menu=color_theme)
        color_theme.add_command(label="Default", command=self.color_theme_default)
        # color_theme.add_command(label="Night",command=self.)
        color_theme.add_command(label="Grey", command=self.color_theme_grey)
        color_theme.add_command(label="Blue", command=self.color_theme_dark_blue)

        color_theme.add_command(label="Torque", command=self.color_theme_turquoise)
        color_theme.add_command(label="Hacker", command=self.color_theme_hacker)

        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)

        self.text_frame = Frame(self.window, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # list_box contains messages
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                             width=10, height=8)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)
        self.hyperlink = HyperlinkManager(self.text_box)   # we are passing textbox to hyperlink class which we imported above

        self.sent_label = Label(self.window, font="Verdana 7",text="No Message Sent.", bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=BOTTOM, anchor="w")

        # Frame contianing suggestion listbox
        self.listbox_suggestion_frame = Frame(self.window, height=0)
        self.listbox_suggestion_frame.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.listbox_suggestion = Listbox(self.listbox_suggestion_frame,height=0)
        self.listbox_suggestion.pack(fill=BOTH,expand=1)
        self.listbox_suggestion_frame.forget()  # to hide the suggestion frame when the tkinter form loads firsttime
        self.listbox_suggestion.bind('<<ListboxSelect>>', self.on_select) # when element is selected in the list box the func will run
        self.listbox_suggestion.bind('<Up>', self.up_arrow) # when 0 index element is selected and up key is pressed so activate entry box

        # frame containing user entry field
        self.entry_frame = Frame(self.window, bd=1)
        self.entry_frame.pack(side=LEFT, fill=X, expand=1)

        # entry field
        self.s = StringVar()
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT,textvariable=self.s)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
        self.entry_field.focus()
        self.entry_field.bind("<KeyRelease>",self.suggestion_func)
        self.entry_field.bind('<Down>', self.downkey_pressed)

        # frame containing send button and emoji button
        self.send_button_frame = Frame(self.window)
        self.send_button_frame.pack(side=RIGHT)

        # send button
        self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.send_message_insert, activebackground="#FFFFFF",
                                  activeforeground="#000000")
        self.send_button.pack(side=LEFT, ipady=8)

        self.window.bind("<Return>", self.send_message_insert)
        self.window.bind('<Escape>', self.close)
        self.window.title("PyBot")
        self.window.geometry(window_size)
        self.window.mainloop()

a = ChatInterface()
