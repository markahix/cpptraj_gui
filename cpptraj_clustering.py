#!/usr/bin/env python3

from tkinter_utilities import *
from clustering_algorithms import *


##########################################################
################### Clustering Section ###################
##########################################################
class SIEVE_TRAJECTORY_FRAME(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        # Internal Variables
        self.bool_sieve = tk.BooleanVar(self,False)
        self.bool_random = tk.BooleanVar(self,False)
        
        # Internal subframes
        self.RADIO_FRAME = tk.Frame(self)
        self.ENTRY_FRAME = tk.Frame(self)
        self.USE_RANDOM_FRAMES = tk.Frame(self)
        self.RANDOM_SEED = tk.Frame(self)
        
        # Labels
        tk.Label(self.RADIO_FRAME, text = "Sieve Frames?").pack(side="left")
        tk.Label(self.USE_RANDOM_FRAMES, text = "Select Frames Randomly?").pack(side="left")
        self.ENTRY_PROMPT = tk.Label(self.ENTRY_FRAME,text="Stride")
        self.SEED_PROMPT  = tk.Label(self.RANDOM_SEED,text="seed")
        
        # Fields
        self.FIELD        = tk.Entry(self.ENTRY_FRAME)
        self.SEED_VALUE   = tk.Entry(self.RANDOM_SEED)
        
        # Packing and Positioning of Main Subframes
        self.RADIO_FRAME.pack(side="top")
        self.ENTRY_FRAME.pack(side="top")
        self.USE_RANDOM_FRAMES.pack(side="top")
        self.SEED_VALUE.pack(side="right")
        self.SEED_PROMPT.pack(side="right")

        # Radio Buttons
        for (text,value) in {"Yes":True,"No":False}.items():
            tk.Radiobutton(self.RADIO_FRAME, 
                           text     = text, 
                           variable = self.bool_sieve,
                           value    = value,
                           command  = self.update_radio_1).pack(fill="x",side="left",ipady = 2,ipadx=2)

        for (text,value) in {"Yes":True,"No":False}.items():
            tk.Radiobutton(self.USE_RANDOM_FRAMES, 
                           text     = text, 
                           variable = self.bool_random,
                           value    = value,
                           command  = self.update_radio_2).pack(fill="x",side="left",ipady = 2,ipadx=2)

        self.update_radio_1()
        self.update_radio_2()
        
    def update_radio_1(self):
        self.FIELD.pack_forget()
        self.ENTRY_PROMPT.pack_forget()
        self.USE_RANDOM_FRAMES.pack_forget()
        if self.bool_sieve.get():
            self.FIELD.pack(side="right")
            self.ENTRY_PROMPT.pack(side="right")
            self.USE_RANDOM_FRAMES.pack(side="top")
            self.FIELD.delete(0,tk.END)
            self.FIELD.insert(0,1)
    def update_radio_2(self):
        self.RANDOM_SEED.pack_forget()
        if self.bool_random.get():
            self.RANDOM_SEED.pack(side="top")
            self.SEED_VALUE.delete(0,tk.END)
            self.SEED_VALUE.insert(0,123456)
            
    def value(self):
        full_string = ""
        if self.bool_sieve.get():
            full_string += f"sieve {self.FIELD.get()} "
            if self.bool_random.get():
                full_string += "random "
                if self.SEED_VALUE.get() != "":
                    full_string += f"sieveseed {self.SEED_VALUE.get()} "
        return full_string


class Clust_Distance_Options(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="grey", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Clustering Distance Options")
        
        self.DISTANCE_SELECT = tk.Frame(self)
        self.DISTANCE_SELECT.pack(side="top")
        self.RADIO_1 = tk.Frame(self.DISTANCE_SELECT)
        self.RADIO_1.pack(side="top")
        
        ### FRAME SETS ###
        self.RMS_FRAME       = tk.Frame(self.DISTANCE_SELECT)
        self.RMS_FRAME.title = TITLE(self.RMS_FRAME,"RMS Distance")
        self.RMS_FRAME.mask  = BOOLEAN_WITH_ENTRY(self.RMS_FRAME,"Use selection mask?","Selection Mask",":1-100","")
        self.RMS_FRAME.mass  = BOOLEAN_RESPONSE(self.RMS_FRAME,"Use Mass?","mass","")
        self.RMS_FRAME.nofit = BOOLEAN_RESPONSE(self.RMS_FRAME,"No Fit?","nofit","")
        
        self.SRMSD_FRAME       = tk.Frame(self.DISTANCE_SELECT)
        self.SRMSD_FRAME.title = TITLE(self.SRMSD_FRAME,"SRMSD Distance")
        self.SRMSD_FRAME.mask  = BOOLEAN_WITH_ENTRY(self.SRMSD_FRAME,"Use selection mask?","Selection Mask",":1-100","")
        self.SRMSD_FRAME.mass  = BOOLEAN_RESPONSE(self.SRMSD_FRAME,"Use Mass?","mass","")
        self.SRMSD_FRAME.nofit = BOOLEAN_RESPONSE(self.SRMSD_FRAME,"No Fit?","nofit","")
        
        self.DME_FRAME       = tk.Frame(self.DISTANCE_SELECT)
        self.DME_FRAME.title = TITLE(self.DME_FRAME,"DME Distance")
        self.DME_FRAME.mask  = ENTRY_FIELD(self.DME_FRAME,"Selection Mask",":1-100")
        
        self.DATA_FRAME       = tk.Frame(self.DISTANCE_SELECT)
        self.DATA_FRAME.title = TITLE(self.DATA_FRAME,"Data Distance")
        self.DATA_FRAME.data  = ENTRY_FIELD(self.DATA_FRAME,"Dataset(s)","d1,a2,t3,...")
        
        self.radio_1 = tk.StringVar(self,"rms")
        for (value,text) in {"rms":"RMS","srmsd":"SRMSD","dme":"DME","data":"Data"}.items():
            tk.Radiobutton(self.RADIO_1, 
                           text     = text, 
                           variable = self.radio_1,
                           value    = value,
                           command  = self.update_radio_1).pack(fill="x",side="right",ipady = 2,ipadx=2)
            
        self.SIEVEFRAMES   = SIEVE_TRAJECTORY_FRAME(self)
        self.LOADPAIRDIST  = BOOLEAN_RESPONSE(self,"Load Pairwise Distance?","loadpairdist ","")
        self.SAVEPAIRDIST  = BOOLEAN_RESPONSE(self,"Save Pairwise Distance?","savepairdist ","")
        self.PAIRDISTFILE  = BOOLEAN_WITH_ENTRY(self,"Pairwise Distance Filename?","Filename","pairdist.dat",False)
        self.PAIRWISECACHE = RADIO_OPTIONS(self,"Pairwise Cache Option",{"Memory":"mem","Disk":"disk","None":"none"},"mem")
        self.INCLUDESIEVEINCALC = BOOLEAN_RESPONSE(self,"Include sieved frames in cluster average?","includesieveincalc ","")
        self.PWRECALC = BOOLEAN_RESPONSE(self,"Force Recalculation if pairwise file doesn't match?","pwrecalc ","")
        self.update_radio_1()
        
    def update_radio_1(self):
        self.RMS_FRAME.pack_forget()
        self.SRMSD_FRAME.pack_forget()
        self.DME_FRAME.pack_forget()
        self.DATA_FRAME.pack_forget()
        if self.radio_1.get() == "rms":
            self.RMS_FRAME.pack(side="top")
        if self.radio_1.get() == "srmsd":
            self.SRMSD_FRAME.pack(side="top")
        if self.radio_1.get() == "dme":
            self.DME_FRAME.pack(side="top")
        if self.radio_1.get() == "data":
            self.DATA_FRAME.pack(side="top")
        
    def command_string(self):
        full_string = ""
        if self.radio_1.get() == "RMS":
            full_string += f"rms {self.RMS_FRAME.mask.value()} {self.RMS_FRAME.mass.value()} {self.RMS_FRAME.nofit.value()} "
        if self.radio_1.get() == "SRMSD":
            full_string += f"srmsd {self.SRMSD_FRAME.mask.value()} {self.SRMSD_FRAME.mass.value()} {self.SRMSD_FRAME.nofit.value()} "
        if self.radio_1.get() == "DME":
            full_string += f"dme {self.DME_FRAME.mask.value()} "
        if self.radio_1.get() == "Data":
            full_string += f"data {self.DATA_FRAME.data.value()} "
        full_string += f"{self.SIEVEFRAMES.value()}{self.LOADPAIRDIST.value()}{self.SAVEPAIRDIST.value()}pairwisecache {self.PAIRWISECACHE.value()}"
        if self.PAIRDISTFILE.value():
            full_string += f"pairdist {self.PAIRDISTFILE.value()}"
        full_string += f"{self.INCLUDESIEVEINCALC.value()}{self.PWRECALC.value()} "
        return full_string
    
    
class Clust_Output_Options(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="grey", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Clustering Report Options")
        
        ### Options Frames
        self.OUT = ENTRY_FIELD(self,"Output Filename","cnumvtime.dat","out ","")
        self.GRACECOLOR = BOOLEAN_RESPONSE(self,"Use XMGrace Colors for Cluster Numbers?","gracecolor ","")
        self.SUMMARY = ENTRY_FIELD(self,"Summary Filename","summaryfile.dat","summary ","")
        self.INFO = ENTRY_FIELD(self,"Information Filename","infofile.dat","info ","")
        self.SUMMARYSPLIT = BOOLEAN_WITH_ENTRY(self,"Use Summary Split?","Filename","splitfile.dat","","summarysplit ","")
        self.SPLITFRAME = BOOLEAN_WITH_ENTRY(self,"Split Frames?","List of frames to split","<comma-separated-list>","","splitframe ","")
        self.BESTREP = RADIO_OPTIONS(self,"Best Representative",{"Cumulative":"bestrep cumulative ","Centroid":"bestrep centroid ","Cumulative No Sieve":"bestrep cumulative_nosieve "},"bestrep cumulative ")
        self.SAVENREPS = ENTRY_FIELD(self,"Number of Representatives to Save","1","savenreps ","")
        self.CLUSTERSVTIME = ENTRY_FIELD(self,"Clusters v. Time filename","clustersvtime.dat","clustersvtime ","")
        self.CTVWINDOW = ENTRY_FIELD(self,"Clusters v. Time window","50","cvtwindow ","")

        self.CPOPVTIME = tk.Frame(self)
        self.CPOPVTIME.pack(side="top",fill="both")
        self.CPOPVTIME_FILENAME = ENTRY_FIELD(self.CPOPVTIME,"Filename for cluster population v. time","cpopvtime.dat","cpopvtime ","")
        self.CPOPVTIME_NORMAL = RADIO_OPTIONS(self.CPOPVTIME,"Normalize Clusters?",{"No Normalization":"","Normalize by Cluster":"normpop ","Normalize by Population":"normframe "},"")
        
        self.SIL = BOOLEAN_WITH_ENTRY(self,"Write average cluster silhouette values?","Filename prefix","sil","","sil ","")
        
        self.ASSIGNREFS = BOOLEAN_WITH_SUBFRAMES(self,"Assign References to Structures?")
        self.ASSIGNREFS.pack(side="top",fill="both")
        self.ASSIGNREFS.SUBFRAMES["refcut"] = BOOLEAN_WITH_ENTRY(self.ASSIGNREFS,"Use RMSD Cutoff?","RMSD Cutoff in Angstroms","1.0","","refcut ","")
        self.ASSIGNREFS.SUBFRAMES["refmask"] = BOOLEAN_WITH_ENTRY(self.ASSIGNREFS,"Use Reference Mask?","Reference Mask","!@H","","refmask ","")        

        for frame in self.pack_slaves():
            frame.configure(highlightbackground="grey", highlightthickness=1)
            
    def command_string(self):
        full_string  = f""
        full_string += f"{self.OUT.value()}"
        full_string += f"{self.GRACECOLOR.value()} "
        full_string += f"{self.SUMMARY.value()} "
        full_string += f"{self.INFO.value()} "
        full_string += f"{self.SUMMARYSPLIT.value()} "
        full_string += f"{self.SPLITFRAME.value()} "
        full_string += f"{self.BESTREP.value()}"
        full_string += f"{self.SAVENREPS.value()} "
        full_string += f"{self.CLUSTERSVTIME.value()} "
        full_string += f"{self.CTVWINDOW.value()} "
        full_string += f"{self.CPOPVTIME_FILENAME.value()} "
        full_string += f"{self.CPOPVTIME_NORMAL.value()} "
        full_string += f"{self.SIL.value()} "
        full_string += f"{self.ASSIGNREFS.value()} "
        return full_string
    
class Clust_Coordinate_Output_Options(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="grey", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.frames     = {}
        self.variables  = {}
        self.checkboxes = {}
        self.is_checked = {}
        self.entry_labels = {}
        
        self.TITLE = TITLE(self,"Clustering Coordinate Output Options")
        ### Options Frames
        # clusterout <trajfileprefix> [clusterfmt <trajformat>] 
        key = "clusterout"
        self.frames[key] = tk.Frame(self)
        self.is_checked[key] = tk.IntVar(self,0)
        self.checkboxes[key] = tk.Checkbutton(self.frames[key], text=key+"\t", variable=self.is_checked[key])
        self.entry_labels[key] = tk.Label(self.frames[key],text="trajfileprefix")
        self.variables[key] = tk.Entry(self.frames[key])
        self.checkboxes[key].pack(side="left")
        self.variables[key].pack(side="right")
        self.entry_labels[key].pack(side="right")
        key = "cluserfmt"
        self.frames[key] = tk.Frame(self)
        self.is_checked[key] = tk.IntVar(self,0)
        self.checkboxes[key] = tk.Checkbutton(self.frames[key], text=key+"\t", variable=self.is_checked[key])
        self.entry_labels[key] = tk.Label(self.frames[key],text="trajformat")
        self.variables[key] = tk.Entry(self.frames[key])
        self.checkboxes[key].pack(side="left")
        self.variables[key].pack(side="right")
        self.entry_labels[key].pack(side="right")
        

        # singlerepout <trajfilename> [singlerepfmt <trajformat>]
        key = "singlerepout"
        self.frames[key] = tk.Frame(self)
        self.is_checked[key] = tk.IntVar(self,0)
        self.checkboxes[key] = tk.Checkbutton(self.frames[key], text=key+"\t", variable=self.is_checked[key])
        self.entry_labels[key] = tk.Label(self.frames[key],text="trajfilename")
        self.variables[key] = tk.Entry(self.frames[key])
        self.checkboxes[key].pack(side="left")
        self.variables[key].pack(side="right")
        self.entry_labels[key].pack(side="right")
        key = "singlerepfmt"
        self.frames[key] = tk.Frame(self)
        self.is_checked[key] = tk.IntVar(self,0)
        self.checkboxes[key] = tk.Checkbutton(self.frames[key], text=key+"\t", variable=self.is_checked[key])
        self.entry_labels[key] = tk.Label(self.frames[key],text="trajformat")
        self.variables[key] = tk.Entry(self.frames[key])
        self.checkboxes[key].pack(side="left")
        self.variables[key].pack(side="right")
        self.entry_labels[key].pack(side="right")
        
        # repout <repprefix> [repfmt <repfmt>] [repframe]
        key = "repout"
        self.frames[key] = tk.Frame(self)
        self.is_checked[key] = tk.IntVar(self,0)
        self.checkboxes[key] = tk.Checkbutton(self.frames[key], text=key+"\t", variable=self.is_checked[key])
        self.entry_labels[key] = tk.Label(self.frames[key],text="repprefix")
        self.variables[key] = tk.Entry(self.frames[key])
        self.checkboxes[key].pack(side="left")
        self.variables[key].pack(side="right")
        self.entry_labels[key].pack(side="right")
        key = "repfmt"
        self.frames[key] = tk.Frame(self)
        self.is_checked[key] = tk.IntVar(self,0)
        self.checkboxes[key] = tk.Checkbutton(self.frames[key], text=key+"\t", variable=self.is_checked[key])
        self.entry_labels[key] = tk.Label(self.frames[key],text="repfmt")
        self.variables[key] = tk.Entry(self.frames[key])
        self.checkboxes[key].pack(side="left")
        self.variables[key].pack(side="right")
        self.entry_labels[key].pack(side="right")

        # avgout <avgprefix> [avgfmt <avgfmt>] 
        key = "avgout"
        self.frames[key] = tk.Frame(self)
        self.is_checked[key] = tk.IntVar(self,0)
        self.checkboxes[key] = tk.Checkbutton(self.frames[key], text=key+"\t", variable=self.is_checked[key])
        self.entry_labels[key] = tk.Label(self.frames[key],text="avgprefix")
        self.variables[key] = tk.Entry(self.frames[key])
        self.checkboxes[key].pack(side="left")
        self.variables[key].pack(side="right")
        self.entry_labels[key].pack(side="right")
        key = "avgfmt"
        self.frames[key] = tk.Frame(self)
        self.is_checked[key] = tk.IntVar(self,0)
        self.checkboxes[key] = tk.Checkbutton(self.frames[key], text=key+"\t", variable=self.is_checked[key])
        self.entry_labels[key] = tk.Label(self.frames[key],text="avgfmt")
        self.variables[key] = tk.Entry(self.frames[key])
        self.checkboxes[key].pack(side="left")
        self.variables[key].pack(side="right")
        self.entry_labels[key].pack(side="right")

        for key in self.checkboxes.keys():
            self.frames[key].pack(side="top",fill="both")

    def command_string(self):
        full_string  =  ""
        for key in self.checkboxes.keys():
            if self.is_checked[key]:
                full_string += f"{key} {self.variables[key].get()} "
        return full_string
    
### MAIN CLUSTERING FRAME
