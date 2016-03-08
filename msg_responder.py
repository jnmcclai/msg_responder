#!/usr/bin/python
#coding: utf-8
#simple python messenger applications

__author__    = "jnmcclai"
__copyright__ = "Copyright 2016, Adtran, Inc."
__version__   = "2.7.7"

import argparse
from Tkinter import *
from ttk import Frame, Button, Style

result = 0
comment = ""

class MsgResponder(Frame):
  
    def __init__(self, parent, qc_step_name, qc_step_description, qc_step_expected_results):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.qc_step_name = qc_step_name
        self.qc_step_description = qc_step_description
        self.qc_step_expected_results = qc_step_expected_results
        self.initUI()

    def clearText(self, event):
        #clear actual results text box event when clicked
        self.text_qc_results_actual.delete("1.0", END)

    def btnClickedPass(self):
        #button clicked method - sets var to 1 and gets comments
        result = 1
        #get the qc step name, description, expected, and actual fields and return in mock xml
        # qc_step_name = "<qc_step_name>" + self.qc_step_name + "</qc_step_name>"
        # qc_step_description = "<qc_step_description>" + self.qc_step_description + "</qc_step_description>"
        # qc_step_expected = "<qc_step_expected>" + self.qc_step_expected_results + "</qc_step_expected>" 
        qc_step_actual = "<qc_step_actual>" + self.text_qc_results_actual.get("1.0", END) + "</qc_step_actual>" 
        #output = qc_step_name + qc_step_description + qc_step_expected + qc_step_actual
        output = qc_step_actual
        output = "<qc>{0}</qc>".format(output)
        print str(result)
        print output
        self.quit()

    def btnClickedFail(self):
        #button clicked method - sets var to 0 and gets comments
        result = 0
        #get the qc step name, description, expected, and actual fields and return in mock xml
        # qc_step_name = "<qc_step_name>" + self.qc_step_name + "</qc_step_name>"
        # qc_step_description = "<qc_step_description>" + self.qc_step_description + "</qc_step_description>"
        # qc_step_expected = "<qc_step_expected>" + self.qc_step_expected_results + "</qc_step_expected>" 
        qc_step_actual = "<qc_step_actual>" + self.text_qc_results_actual.get("1.0", END) + "</qc_step_actual>" 
        #output = qc_step_name + qc_step_description + qc_step_expected + qc_step_actual
        output = qc_step_actual
        output = "<qc>{0}</qc>".format(output)
        print str(result)
        print output
        self.quit()
        
    def initUI(self):
        
        #some aesthetic definitions 
        self.parent.title("Message Responder - {0}".format(self.qc_step_name))
        self.style = Style()
        self.style.theme_use("classic")

        #building frame
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        #create top vertical pane for qc desc
        pane_top = PanedWindow(frame, orient = VERTICAL)
        pane_top.pack(fill=BOTH, expand = 1)

        #create bottom panes for the qc expected and actual results fields
        pane_bottom = PanedWindow(frame)
        pane_bottom.pack(fill=BOTH, expand = 1)

        #add qc desc label frame to the top pane and a label for the text
        qc_step_description = "\n" + self.qc_step_description
        label_frame_qc_desc = LabelFrame(pane_top, text="QC Description")
        label_qc_desc = Label(label_frame_qc_desc, text=qc_step_description, wraplength=1020, justify=LEFT)
        label_qc_desc.pack(anchor=W)
        pane_top.add(label_frame_qc_desc)

        #add qc expected results label frame to the bottom pane and a label for the text
        qc_step_expected_results = "\n" + self.qc_step_expected_results
        label_frame_qc_results_expected = LabelFrame(pane_bottom, text="QC Expected Results", width=500)
        label_frame_qc_results_expected.pack_propagate(0)
        label_qc_results_expected = Label(label_frame_qc_results_expected, text=qc_step_expected_results, wraplength=496, justify=LEFT)
        label_qc_results_expected.pack(anchor=W)
        pane_bottom.add(label_frame_qc_results_expected)

        #add qc actual results text box with default text
        self.text_qc_results_actual = Text(pane_bottom, height=14)
        self.text_qc_results_actual.insert(END, "Actual Results...")
        self.text_qc_results_actual.bind('<FocusIn>', self.clearText)
        pane_bottom.add(self.text_qc_results_actual) 

        #adding buttons
        passButton = Button(self, text="PASS", command=self.btnClickedPass)
        passButton.pack(side=RIGHT, padx=5, pady=5)
        failButton = Button(self, text="FAIL", command=self.btnClickedFail)
        failButton.pack(side=RIGHT)



              

def main(qc_step_name, qc_step_description, qc_step_expected_results):
  
    root = Tk()
    root.geometry("1024x600+200+100")
    app = MsgResponder(root, qc_step_name, qc_step_description, qc_step_expected_results)
    root.mainloop()  


if __name__ == '__main__':

    #handle command arguments
    parser = argparse.ArgumentParser(description = 'Message responder - simple GUI to display user defined text and return value based on click of button to pass or fail a test. Returns value PASS=1, FAIL=0')
    parser.add_argument('-name', '--qc_step_name', help = 'the QC/ALM step name', default = "generic qc step name")
    parser.add_argument('-desc', '--qc_step_description', help = 'the QC/ALM step description', default = "generic qc description")
    parser.add_argument('-expected', '--qc_step_expected_results', help = 'the QC/ALM step expected results', default = "generic qc expected results")
    
    
    args = parser.parse_args()

    if args.qc_step_name:
        qc_step_name = args.qc_step_name
    if args.qc_step_description:
        qc_step_description = args.qc_step_description
    if args.qc_step_expected_results:
        qc_step_expected_results = args.qc_step_expected_results

    #start main
    main(qc_step_name, qc_step_description, qc_step_expected_results)  