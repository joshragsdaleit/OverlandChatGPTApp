import tkinter
import tkinter.messagebox
import customtkinter
import webbrowser
import openai
import random
from config import myKey

# Set up the OpenAI API client
openai.api_key = myKey

# Tag options to select
switch_options = ['a', 'title', 'p', 'Full HTML', 'Get All Text', 'span', 'id']

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    

    # Main Constructor
    def __init__(self):
        super().__init__()

        # configure window
        self.title("OverlandChatApp.py")
        self.geometry(f"{920}x{500}")

        # Bind global keys to main Window
        self.bind('<Return>', self.submit_to_chat_api)
        self.bind('1', self.sidebar_button_event2)
        self.bind('2', self.sidebar_button_event3)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((1, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Overland Technical\nSolutions:\nChatGPT App", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="About Overland", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Randomized Questions")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_2.bind('<g>', self.sidebar_button_event2)
        self.sidebar_button_2.bind('<Button-1>', self.sidebar_button_event2)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="More Questions!")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_3.bind('<w>', self.sidebar_button_event3)
        self.sidebar_button_3.bind('<Button-1>', self.sidebar_button_event3)
        # Donate to me please? Broke dad with four kids and relevant experience - I could really use a dev job!
        self.donate = customtkinter.CTkButton(self.sidebar_frame, text="Donate", command=self.donate_button_press)
        self.donate.grid(row=4, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark (Default)", "Light", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["100%", "80%", "90%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20)) # Scaling Menu

        # Creating Response TextBox
        self.textbox = customtkinter.CTkTextbox(self, width=650) 
        self.textbox.grid(row=0, rowspan=2, column=1, padx=(20, 0), pady=(10, 0), sticky="nsew")

        # Ask Chat Button
        self.main_button_1 = customtkinter.CTkButton(master=self, text="Ask ChatGPT", text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.main_button_1.bind('<Button-1>', self.submit_to_chat_api)

        # create Input Entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Input your question for ChatGPT here!")
        self.entry.grid(row=3, column=1, padx=(20, 0), pady=(20, 10), sticky="nsew")

        

        # set default value for Textbox
        self.textbox.insert(0.0, '''Welcome to my Basic ChatGPT API app! 
Hoping to build a simple tool that returns
API calls to ChatGPT, and displays them to the user. 
You can press either 1 or 2 for randomized questions, manually type in your question,
and press Enter or the 'Ask ChatGPT' button.
''')

    def change_appearance_mode_event(self, new_appearance_mode: str): # Function to update Appearance defaults that TKInter allows
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str): # Function to update Scaling
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self): # Clicking the 'about overland' button will take you to my website
        webbrowser.open('http://www.overlandtechnicalsolutions.com', new=2)

    def sidebar_button_event2(self, event): # fill Entry box with Google Search default URL 
        list_of_questions = [
            'What services do you provide?',
            'How much do your services cost?',
            'What is the process for getting started?',
            'What are the payment options?',
            'Do you have any special offers?',
            'Do you have any availability?',
            'How long does it take to receive results?',
            'Can I get a free consultation?',
            'Do you offer any guarantees?',
            'What sets you apart from other companies?',
            'What experience do you have in my industry?',
            'Do you have any case studies or references I can review?',
            'How can I contact you?']
        
        question_fill = list_of_questions[random.randint(0, len(list_of_questions)-1)]
        self.entry.delete(0, tkinter.END)
        self.entry.insert(0, question_fill)

    def sidebar_button_event3(self, event): # fill Entry box with Google Search default URL 
        list_of_questions = [
            'What can I do to improve my skills?',
            'How can I break into the industry?',
            'What resources are available to help me succeed?',
            'Where can I go for career advice?',
            'How do I stand out from other job applicants?',
            'What kind of salary can I expect?',
            'What certifications or educational background do I need?',
            'Are remote and contract jobs a viable option?',
            'What technology should I be familiar with?',
            'How do I network effectively?',
            'Is graduate school worth it?',
            'What are some of the biggest challenges in my field?',
            'What automation or programming languages are important?',
        ]
        question_fill = list_of_questions[random.randint(0, len(list_of_questions)-1)]
        self.entry.delete(0, tkinter.END)
        self.entry.insert(0, question_fill)      

    def donate_button_press(self): # Open CashApp for donations
        webbrowser.open('https://cash.app/$Jrags2010', new=2)

    def submit_to_chat_api(self, event):
        # Clear the textbox
        user_input_query = self.entry.get()
        self.textbox.delete("0.0", tkinter.END)
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=user_input_query,
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
            )
            message = response.choices[0].text
            self.textbox.insert(0.0, message)
        except Exception as err:
            self.textbox.insert(tkinter.END, "Error: \n" + str(err) +"\n")

        
# BS4 Documentation for reference - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Call Main loop
if __name__ == "__main__":
    app = App()
    app.mainloop()
