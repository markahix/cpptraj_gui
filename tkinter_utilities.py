#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
import os
import subprocess
#################################################################################################
######################################## COMMENT BLOCKS #########################################
#################################################################################################
def commentary(string):
    full_string=""
    comm_line = "".join(["#" for i in range(80)])+"\n"
    string = string.replace("\n"," ")
    full_string += comm_line
    current_line = "# "
    for word in string.split():
        if len(current_line) + len(word) + 1 > 76:
            current_line += "#".rjust(80-len(current_line))+"\n"
            full_string += current_line
            current_line = "# "
        current_line += f"{word} "
    current_line += "#".rjust(80-len(current_line))+"\n"
    full_string += current_line
    full_string += comm_line
    return full_string

#################################################################################################
######################################## Standard Frames ########################################
#################################################################################################
class TITLE(tk.Frame):
    def __init__(self,master=None,title="<Title Text>"):
        super().__init__(master)
        self.title_text = title
        self.TITLE = tk.Label(self,text=self.title_text)
        self.TITLE.pack(side="top")
        self.pack()
    def update(self,new_title):
        self.title_text = new_title
        self.TITLE.configure(text=self.title_text)
        return

class SELF_DESTRUCT_BUTTON(tk.Frame):
    def __init__(self,master=None,destruct_text="<REMOVE FRAME>",fg="red"):
        super().__init__(master)
        self.SELF_DESTRUCT = tk.Button(self,text=destruct_text,fg=fg,command=master.destroy)
        self.SELF_DESTRUCT.pack(side="right")


        
#################################################################################################
########################################## Input Frames #########################################
#################################################################################################
class ENTRY_FIELD(tk.Frame): #ENTRY_FIELD(master,label,default,prefix,suffix)
    def __init__(self,master=None,label="<Field Label>",default="<default text>",prefix="",suffix=""):
        super().__init__(master)
        self.prefix = prefix
        self.suffix = suffix
        self.pack(side="top",fill='both')
        textlabel = tk.Label(self,text=label)
        textlabel.pack(side="left")
        self.ENTRY = tk.Entry(self)
        self.ENTRY.insert(0, default)
        self.ENTRY.pack(side="right")
    def value(self):
        return f"{self.prefix}{self.ENTRY.get()}{self.suffix}"

class FILE_SELECT_BUTTON(tk.Frame): #FILE_SELECT_BUTTON(master,name,filetypes:tuple-of-tuples)
    def __init__(self,master=None,name="<Filetype>",filetypes=(("All Files","*.*"))):
        super().__init__(master)
        self.filename = ""
        self.name     = name
        self.filetypes= filetypes
        self.pack(side="top",fill='both')
        self.button = tk.Button(self,text=self.name,command=self.GetFile)
        self.button.pack(side="left")
    def GetFile(self):
        self.filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select a File",filetypes = self.filetypes)
        self.button.configure(fg="green")
        tk.Label(self,text=self.filename).pack(side="right")
    def value(self):
        return str(self.filename)
    
class RADIO_OPTIONS(tk.Frame): #RADIO_OPTIONS(master,radio_prompt,options_dict,default_option)
    def __init__(self,master=None,radio_prompt="<Choice Prompt>",options={},default_opt=""):
        super().__init__(master)
        tk.Label(self,text=radio_prompt).pack(side="left")
        self.FIELD  = tk.Entry(self)
        self.option = tk.StringVar(self,default_opt)
        self.pack(side="top",fill='both')
        for (text, value) in options.items():
            tk.Radiobutton(self,text=text,variable=self.option,value=value).pack(fill="x",side="right",ipady=2,ipadx=2)
    def value(self):
        return self.option.get()    
    

class BOOLEAN_RESPONSE(tk.Frame): #BOOLEAN_RESPONSE(master,bool_prompt,true_return,false_return)
    def __init__(self,master=None,bool_prompt="<Choice Prompt>",true_return="<True Return>",false_return="<False Return>"):
        super().__init__(master)
        tk.Label(self, text = bool_prompt).pack(side="left")
        self.FIELD        = tk.Entry(self)
        self.boolean      = tk.BooleanVar(self,False)
        self.true_return  = true_return
        self.false_return = false_return
        self.pack(side="top",fill='both')
        for (text, value) in {"Yes":True,"No":False}.items():
            tk.Radiobutton(self,text=text,variable=self.boolean,value=value).pack(fill="x",side="right",ipady=2,ipadx=2)
    def value(self):
        if self.boolean.get():
            return self.true_return
        return self.false_return

class BOOLEAN_WITH_ENTRY(tk.Frame): #BOOLEAN_WITH_ENTRY(master,bool_prompt,entry_prompt,default,false_return,prefix,suffix)
    def __init__(self,master=None,bool_prompt="<Choice Prompt>",entry_prompt="<Entry Prompt>",default="<Default Value>",false_return="<False Return>",prefix="",suffix=""):
        super().__init__(master)
        tk.Label(self, text = bool_prompt).pack(side="left")
        self.FIELD        = tk.Entry(self)
        self.ENTRY_PROMPT = tk.Label(self,text=entry_prompt)
        self.boolean      = tk.BooleanVar(self,False)
        self.default      = default
        self.false_return = false_return
        self.prefix       = prefix
        self.suffix       = suffix
        self.pack(side="top",fill='both')
        for (text, value) in {"Yes":True,"No":False}.items():
            tk.Radiobutton(self, text = text, variable = self.boolean,
                value = value,command=self.update).pack(fill="x",side="right", ipady = 2,ipadx=2)
        self.update()
    def update(self):
        if self.boolean.get():
            self.FIELD.pack_forget()
            self.ENTRY_PROMPT.pack_forget()
            self.FIELD.pack(side="right")
            self.ENTRY_PROMPT.pack(side="right")
            self.FIELD.delete(0,tk.END)
            self.FIELD.insert(0,self.default)
        else:
            self.FIELD.pack_forget()
            self.ENTRY_PROMPT.pack_forget()
    def value(self):
        if self.boolean.get():
            return f"{self.prefix}{self.FIELD.get()}{self.suffix}"
        return self.false_return
    
class BOOLEAN_WITH_SUBFRAMES(tk.Frame): #BOOLEAN_WITH_SUBFRAMES(master,bool_prompt) # Provides SUBFRAMES empty dictionary which may be added to with additional frames.  Assumption for .value() call is that all subframes have their own .value() call inside.
    def __init__(self,master=None,bool_prompt="<Choice Prompt>"):
        super().__init__(master)
        self.BOOLEAN = tk.Frame(self)
        self.BOOLEAN.pack(side="top",fill="both")
        tk.Label(self.BOOLEAN, text = bool_prompt).pack(side="left")
        self.boolean      = tk.BooleanVar(self,False)
        self.SUBFRAMES = {}
        self.pack(side="top",fill='both')
        
        for (text, value) in {"Yes":True,"No":False}.items():
            tk.Radiobutton(self.BOOLEAN, text = text, variable = self.boolean,
                value = value,command=self.update).pack(fill="x",side="right", ipady = 2,ipadx=2)
        self.update()
    def update(self):
        if self.status():
            for key in self.SUBFRAMES.keys():
                self.SUBFRAMES[key].pack(fill="both")
        else:
            for key in self.SUBFRAMES.keys():
                self.SUBFRAMES[key].pack_forget()
    def status(self):
        return self.boolean.get()
    def value(self):
        full_string = ""
        for key in self.SUBFRAMES.keys():
            full_string += self.SUBFRAMES[key].value()
        return full_string   
    
    
    