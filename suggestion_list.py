from tkinter import *

class suggestion_list:

    def update_listbox(self,data):
        # delete previous data
        self.listbox_suggestion.delete(0, 'end')

        # sorting data
        self.data = sorted(data, key=str.lower)

        # put new data
        for self.item in self.data:
            self.listbox_suggestion.insert('end', self.item)


    # hiding and un-hiding the frames in a proper sequence
    def suggestion_func(self,event):
        self.on_keyrelease()
        if self.entry_field.get() == "":
            print("Its blank")
            # packing the widget in the required order
            self.sent_label.pack(side=BOTTOM)
            self.entry_frame.pack(side=LEFT, fill=X, expand=1)
            self.send_button_frame.pack(side=RIGHT)
            self.listbox_suggestion_frame.forget() # hide the frame if nothing is there in the entry box
            self.text_box.see(END) # to see the last text , so scrollbar will be down
        else:
            print("Its non blank")
            self.entry_frame.forget() # hide the entry frame
            self.send_button_frame.forget()  # hide the send button frame
            # packing back again in a proper order
            self.listbox_suggestion_frame.pack(side=BOTTOM, fill=BOTH, expand=1)
            self.entry_frame.pack(side=LEFT, fill=X, expand=1)
            self.send_button_frame.pack(side=RIGHT)
            self.text_box.see(END) # to see the last text , so scrollbar will be down

    def on_keyrelease(self):
        # get text from entry
        self.value = self.entry_field.get()
        self.value = self.value.strip().lower()

        # get data from list_of_questions
        if self.value == '':
            self.data = []
        else:
            self.data = []
            for self.item in self.list_of_questions:
                if self.value in self.item.lower():
                    self.data.append(self.item)

        # update data in listbox
        self.update_listbox(self.data)
