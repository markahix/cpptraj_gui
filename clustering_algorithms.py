#!/usr/bin/env python3
from tkinter_utilities import *

#################################################################################################
##################################### CLUSTERING ALGORITHMS #####################################    
#################################################################################################
class HeirAgglo(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"HeirAgglo Clustering")
        self.EPSILON     = ENTRY_FIELD(self,"Epsilon","0.5")
        self.CLUSTERS    = ENTRY_FIELD(self,"Clusters","10")
        self.LINKAGE_OPT = RADIO_OPTIONS(self,"Linkage Options",{"Linkage":"linkage","Average Linkage":"averagelinkage","Complete":"complete"},"linkage")
        self.EPS_PLOT = BOOLEAN_WITH_ENTRY(self,"Save Epsilon Plot?","Filename","epsilon_plot.dat","","epsilonplot ","")
        self.INCL_SIEVED = BOOLEAN_RESPONSE(self,"Include Sieved C-distance?","includesieved_cdist ","")
        self.INCL_SIEVED.pack(side="top")
    def command_string(self):
        full_string  =  "heiragglo "
        full_string += f"epsilon {self.EPSILON.value()} "
        full_string += f"clusters {self.CLUSTERS.value()} "
        full_string += f"{self.LINKAGE_OPT.value()} "
        full_string += f"{self.EPS_PLOT.value()} "
        full_string += f"{self.INCL_SIEVED.value()}"
        return full_string

class DBScan(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"DBSCAN Clustering")
        
        ### Variables
        self.MINPOINTS = ENTRY_FIELD(self,"Minimum Number of Points","1","minpoints ","")
        self.EPSILON = ENTRY_FIELD(self,"Epsilon value (cutoff distance)","2.0","epsilon ","")
        self.SIEVETOFRAME = BOOLEAN_RESPONSE(self,"Compare sieved frames to all?","sievetoframe ","")
        self.KDIST_FRAME = BOOLEAN_WITH_SUBFRAMES(self,"Generate K-dist plot? ")
        self.KDIST_FRAME.SUBFRAMES["distance"] = ENTRY_FIELD(self.KDIST_FRAME,"K value","1","kdist ","")
        self.KDIST_FRAME.SUBFRAMES["filename"] = BOOLEAN_WITH_ENTRY(self.KDIST_FRAME,"Save D-dist file?","File Prefix","kdist","","kfile ","")
        ### Options Frame
        
    def command_string(self):
        full_string  = f"dbscan "
        full_string += f"{self.MINPOINTS.value()} "
        full_string += f"{self.EPSILON.value()} "
        full_string += f"{self.SIEVETOFRAME.value()} "
        full_string += f"{self.KDIST_FRAME.value()} "
        return full_string
        
        
class DPeaks(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Density Peaks Clustering")
        
        ### Variables
        self.EPSILON   = ENTRY_FIELD(self,"Epsilon","0.5","epsilon ","")
        self.NOISE = BOOLEAN_RESPONSE(self,"Treat points within epsilon of another cluster as noise?","noise ","")
        self.DVD = BOOLEAN_WITH_ENTRY(self,"Write Density v. Distance File?","Filename","denvdist.dat","","dvdfile ","")
        self.CHOOSEPOINTS = RADIO_OPTIONS(self,"Choose cluster points?",{"Manual":"choosepoints manual ","Automatic":"choosepoints auto "},"choosepoints auto ")
        self.DISTCUT = BOOLEAN_WITH_ENTRY(self,"Distance cutoff for manually chosen cluster points?","Cutoff in Angstroms", "5.0", "" , "distancecut ", "")
        self.DENSCUT = BOOLEAN_WITH_ENTRY(self,"Density cutoff for manually chosen cluster points?","Cutoff ", "10.0", "" , "densitycut ", "")
        self.RUNAVG = BOOLEAN_WITH_ENTRY(self,"Running average for automatically chosen cluster points?", "Filename", "RunningAverage.dat", "", "runavg ", "")
        self.DELTAFILE = BOOLEAN_WITH_ENTRY(self,"Save Delta file for automatically chosen cluster points?", "Filename", "Delta.dat", "","deltafile ","")
        self.GAUSS = BOOLEAN_RESPONSE(self,"Calculate density with Gaussian kernels?","gauss ","")
        ### Options Frame
        
    def command_string(self):
        full_string  = f"dpeaks "
        full_string += f"{self.EPSILON.value()} "
        full_string += f"{self.NOISE.value()} "
        full_string += f"{self.DVD.value()} "
        full_string += f"{self.CHOOSEPOINTS.value()} "
        full_string += f"{self.DISTCUT.value()} "
        full_string += f"{self.DENSCUT.value()} "
        full_string += f"{self.RUNAVG.value()} "
        full_string += f"{self.DELTAFILE.value()} "
        full_string += f"{self.GAUSS.value()} "
        return full_string
    
    
    
    
### K-means
# [kmeans clusters <n> 
# [randompoint [kseed <seed>]] 
# [maxit <iterations>]
# [{readtxt|readinfo} infofile <file>]

class Kmeans(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"K-means Clustering")
        
        ### Variables
        
        self.CLUSTERS   = ENTRY_FIELD(self,"Number of Clusters",10,"clusters ","")
        
        self.RANDOMPOINT = BOOLEAN_WITH_ENTRY(self,"Randomize initial points?","Random Seed","8675309","","randompoint kseed ","")
        
        self.MAXIT = ENTRY_FIELD(self,"Max Iterations", "100","maxit ","")
        self.READINFO = BOOLEAN_WITH_ENTRY(self,"Read in previous clustering information?","Filename","","","readinfo infofile ","")
        
    def command_string(self):
        full_string  = f"kmeans "
        full_string += f"{self.CLUSTERS.value()} "
        full_string += f"{self.RANDOMPOINT.value()} "
        full_string += f"{self.MAXIT.value()} "
        full_string += f"{self.READINFO.value()} "
        return full_string