from tkinter import *
from tkinter import messagebox
import random

TITLE_FONT = ("Georgia", 18, "normal")
FONT = ("Georgia", 14, "normal")

RANDOM_TEXT_OPTIONS = [
    "Finance is the soul and blood of any business and no firm can survive without finance. It concerns itself with "
    "the management of monetary affairs of the firm how money can be raised on the best terms available and how the "
    "procured money can be devoted to the best uses. Hence the nature of finance relates to the process of "
    "arrangement and application of funds. Utilization of finance requires payment of fees, rent or any such cost to "
    "the provider of finance. Business raises funds and in exchange it has to pay a cost to suppliers of the funds. "
    "If the finance is arranged by issuing shares the firm pays dividend in return or capital payment in the form of "
    "bonus shares. Economic application of finance helps to earn profit which ultimately creates value for the firm. "
    "Finance administers economic activities, enhances efficiency of the business operation, and thus ensures "
    "creation of surplus.",
    "Global warming is the latest alarm bell for earth’s environment. Global warming refers to the increase in average "
    "temperature of earth’s surface during the last century, from 1900-2000. Earth’s surface’s temperature has "
    "increased more than one degree Fahrenheit since 1900. Global warming is alarming because of its adverse effects "
    "on the ecological balance of earth. The resultant ecological imbalance, due to global warming, is the root cause "
    "of various natural calamities like floods, famines, etc. Also it is the root cause of various environmental "
    "threats like increase in sea level, glacier melting, changes in quantity and pattern of rainfall, heat waves, "
    "extreme seasons, etc. This is why global warming is the buzzword of almost all environmental talks, projects and "
    "discussions, etc.",
    "A cryptocurrency is a virtual or digital currency that is highly secured by cryptography or encryption "
    "techniques which makes it nearly impossible to counterfeit such cryptocurrency. These crypto currencies are "
    "designed to work as a medium of exchange. Crypto currencies are generally not issued by the government agency of "
    "any country. The decentralized nature of cryptocurrency networks shields it from any control of government "
    "regulatory bodies on it. Bitcoin is the first type of cryptocurrency that presently remains the most used, "
    "valuable, and popular. After bitcoin, many other alternative crypto currencies with varying degrees of functions "
    "and specifications have been created. Bitcoin which is the most popular cryptocurrency was launched in 2009 by "
    "an individual or group known by the Satoshi Nakamoto, in the month of April 2021.",
    "Having a healthy lifestyle is all about choosing to live your life in the healthiest way possible. There are a "
    "few things you have to do to start living your life in this way, i.e. the healthy way. This means doing some "
    "amount of exercise daily, such as jogging, yoga, playing sports, etc. Adding to this, you must also have a "
    "balanced and nutritional diet with all the food groups. It would be best if you were taking the right amount of "
    "proteins, carbohydrates, vitamins, minerals, and fats to help you have a proper diet. Grouped with these two "
    "essential aspects (diet and exercise), a healthy person also maintains the same sleep cycle, which should "
    "consist of around 7- 8 hours of sleep. However, we must remember that a healthy lifestyle not only refers to our "
    "physical and mental health.",
    "A debit card is a payment card that deducts money directly from a consumer’s checking account when it is used. "
    "Also called check cards or bank cards, they can be used to buy goods or services; or to get cash from an "
    "automated teller machine or a merchant who'll let you add an extra amount onto a purchase. Debit cards eliminate "
    "the need to carry cash or physical checks to make purchases, and they can also be used at ATMs to withdraw cash. "
    "Debit cards usually have daily purchase limits, meaning it may not be possible to make an especially large "
    "purchase with a debit card. Debit card purchases can usually be made with or without a personal identification "
    "number (PIN). You may be charged an ATM transaction fee if you use your debit card to withdraw cash from an ATM "
    "that's not affiliated with the bank that issued your card."
]

INSTRUCTIONS = "This typing speed test will measure how many gross and net words per minute (WPM) you can " \
               "type, as well as your accuracy.\n" \
               "To begin, you can click the next button below which will take you to the test.\nYou will have 60 " \
               "seconds to type the words you see in the textbox on the next screen after you click the start button.\n" \
               "The characters will turn green if you typed them correctly or " \
               "red if you typed them incorrectly.\nMake sure to type the characters exactly as they are (punctuation " \
               "and capitalization matter). \n" \
               "You have the opportunity to fix any mistakes you make by backspacing.\n" \
               "At the end of the minute, a pop-up box will come up with your results."


class Screen(Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test")
        self.config(padx=10, pady=10)
        self.random_text = ""
        self.text = Text(master=self, wrap=WORD, height=9, width=90, font=FONT)
        self.user_entry = Entry(master=self, width=90, font=FONT)
        self.display = Label(master=self, text="Typing Speed Test", font=TITLE_FONT)
        self.timer_label = Label(master=self, text="Timer: 60", font=FONT)
        self.timer = None
        self.start_button = Button(master=self, text="Start", font=FONT,command=self.start_timer)
        self.reset_button = Button(master=self, text="Reset",font=FONT, command=self.reset_screen)
        self.user_entry_text = ""
        self.correct_chars = 0
        self.typing_mistakes = 0
        self.gross_wpm = 0
        self.net_wpm = 0
        self.all_char = 0
        self.accuracy = 0
        self.instruction_label = Label(master=self, text="Instructions", font=TITLE_FONT)
        self.instructions = Label(master=self, text=INSTRUCTIONS, font=FONT)
        self.next_button = Button(text="Next", font=FONT, command=self.setup_screen)
        self.give_instructions()
        self.mainloop()

    def give_instructions(self):
        self.instruction_label.grid(row=0, column=0, columnspan=3)
        self.instructions.grid(row=1, column=0)
        self.next_button.grid(row=2, column=2)

    def setup_screen(self):
        self.instruction_label.destroy()
        self.instructions.destroy()
        self.next_button.destroy()
        self.display.grid(row=0, column=0, columnspan=3)
        self.start_button.grid(row=3, column=0)
        self.reset_button.grid(row=3, column=2)
        self.random_text = random.choice(RANDOM_TEXT_OPTIONS)
        self.text.insert(INSERT, self.random_text)
        self.text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.user_entry.bind('<KeyRelease>', self.change_char_color)
        self.user_entry.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.timer_label.grid(row=4, column=1)

    def timer_countdown(self, seconds):
        self.timer_label.configure(text=f"Timer: {seconds}")
        if seconds > 0:
            self.timer = self.after(1000, self.timer_countdown, seconds - 1)
        else:
            self.check_user_entry()

    def start_timer(self):
        self.timer_countdown(60)

    def check_user_entry(self):
        user_entry_text = self.user_entry.get()
        for index, char in enumerate(user_entry_text):
            if char == self.random_text[index]:
                self.correct_chars += 1
            else:
                self.typing_mistakes += 1
        self.all_char = self.correct_chars + self.typing_mistakes
        self.gross_wpm = self.all_char / 5
        self.net_wpm = self.gross_wpm - self.typing_mistakes
        self.accuracy = self.correct_chars / self.all_char * 100
        results = f"Gross WPM: {self.gross_wpm}\nNet WPM: {self.net_wpm}\nAccuracy: {self.accuracy}%"
        messagebox.showinfo("Results", results)

    def change_char_color(self, event):
        user_entry_text = self.user_entry.get()
        self.text.tag_delete("red")
        self.text.tag_delete("green")

        for index, char in enumerate(user_entry_text):
            if index < len(self.random_text):
                if char == self.random_text[index]:
                    tag = "green"
                else:
                    tag = "red"
                start_index = "1.0 + {} chars".format(index)
                end_index = "1.0 + {} chars".format(index + 1)
                self.text.tag_configure(tag, foreground=tag)
                self.text.tag_remove("green", start_index, end_index)
                self.text.tag_remove("red", start_index, end_index)
                self.text.tag_add(tag, start_index, end_index)

    def reset_screen(self):
        if self.timer:
            self.after_cancel(self.timer)
        self.timer_label.configure(text="Timer: 60")
        self.user_entry.delete(0, END)
        self.user_entry_text = ""
        self.correct_chars = 0
        self.typing_mistakes = 0
        self.gross_wpm = 0
        self.net_wpm = 0
        self.all_char = 0
        self.accuracy = 0

        self.text.tag_remove("red", "1.0", END)
        self.text.tag_remove("green", "1.0", END)
        self.text.delete("1.0", END)
        self.random_text = random.choice(RANDOM_TEXT_OPTIONS)
        self.text.insert(INSERT, self.random_text)

        self.start_button.config(state=NORMAL)

