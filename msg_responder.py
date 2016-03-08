#simple python messenger application
#ver02

import argparse
from Tkinter import *
from ttk import Frame, Button, Style

result = 0
comment = ""

class MsgResponder(Frame):
  
    def __init__(self, parent, text):
        Frame.__init__(self, parent)   
        self.grid() 
        self.parent = parent
        self.text = text
        self.initUI()

    def btnClickedPass(self):
        #button clicked method - sets var to 1 and gets comments
        result = 1
        comment = "<comment>" + self.textBox.get("1.0", END) + "</comment>" 
        print str(result)
        print comment
        self.quit()

    def btnClickedFail(self):
        #button clicked method - sets var to 0 and gets comments
        result = 0
        comment = "<comment>" + self.textBox.get("1.0", END) + "</comment>" 
        print str(result)
        print comment
        self.quit()
        
    def initUI(self):
        
        #some aesthetic definitions 
        self.parent.title("Message Responder")
        self.style = Style()
        self.style.theme_use("classic")


        #building frame
        # frame = Frame(self, relief=RAISED, borderwidth=1)
        # #frame.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
        # frame.pack(fill=BOTH, expand=True)


        # self.pack(fill=BOTH, expand=True)
        
        # #adding some widgets
        # label = Label(frame, text = self.text, wraplength = 495, justify = LEFT)
        # label.pack()
        # self.textBox = Text(frame, height = 2, width = 495)
        # self.textBox.pack(side = BOTTOM)
        # #self.textBox.insert(END, '#enter ye comments here')
        # labelBox = Label(frame, text = "Actual Results:")
        # labelBox.pack(anchor = W, side = BOTTOM)
        # passButton = Button(self, text="PASS", command=self.btnClickedPass)
        # passButton.pack(side=RIGHT, padx=5, pady=5)
        # failButton = Button(self, text="FAIL", command=self.btnClickedFail)
        # failButton.pack(side=RIGHT)



        #ver 02
        frame1 = Frame(master, bg = 'red')
        frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)  

root = MsgResponder()
app = Application(master=root)
app.mainloop()

              

# def main(text):
  
#     root = Tk()
#     root.geometry("500x300+300+300")
#     app = MsgResponder(root, text)
#     root.mainloop()  


# if __name__ == '__main__':

#     #handle command arguments
#     parser = argparse.ArgumentParser(description = 'Message responder - simple GUI to display user defined text and return value based on click of button to pass or fail a test. Returns value PASS=1, FAIL=0')
#     parser.add_argument('text', help = 'text to pass in and display on label')
    
#     args = parser.parse_args()

#     if args.text:
#         text = args.text

#     #start main
#     print "starting msg responder..."
#     main(text)  