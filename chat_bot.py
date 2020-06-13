from Chrome_Browser import Web_Automations
from tabs import tabs
import threading
import ast

class bot_class(Web_Automations,tabs):

    def __init__(self):
        Web_Automations.__init__(self)
        tabs.__init__(self)

        with open("question_answer_data.txt") as f:
            self.content = f.read()
            self.list_of_dict = ast.literal_eval(self.content) # removing the '' from the str
            self.extract_qtns_from_list(self.list_of_dict)     # running the below method

    def extract_qtns_from_list(self,lists):
        self.list_of_questions = []
        for dic in self.list_of_dict:
            for qtn,ans in dic.items():
                self.list_of_questions.append(qtn)

    def get_answer_from_text_file(self,question):
        for dic in self.list_of_dict:
            if question in dic.keys():
                return dic[question]
            if question not in dic:
                continue
            else:
                return "I am able to get you, please ask an different question"
        return "I am able to get you, please ask an different question"

    def chat(self, user_response):
        user_response = user_response.strip().lower()
        if user_response == "run the browser":
            thread = threading.Thread(target=self.run_browser_threaded)
            thread.start()
        elif user_response != "bye":
            return self.get_answer_from_text_file(user_response)
        elif user_response == "bye":
            return "bye, Have a great day!"