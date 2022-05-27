#!/usr/bin/env python3

from tkinter_utilities import *
from cpptraj_clustering import *

##########################################################
###################### Main Analyses #####################
##########################################################
### RMSD vs. Time
class RMSD(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"RMSD vs. Time")
        self.RMSD_FRAME = ENTRY_FIELD(self,"RMSD Selection Mask",":1-100")
        ### File Output Frame
        self.OUTFILE = ENTRY_FIELD(self,"Output Filename?","RMSD.dat")
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
        
    def command_string(self):
        full_string = commentary(f"Root-Mean-Squared Deviation of all atoms in {self.RMSD_FRAME.value()} over time, written to {self.OUTFILE.value()}.")
        full_string += f"rms first perres {self.RMSD_FRAME.value()} out {self.OUTFILE.value()}\n"
        return full_string

### Distance between two atoms vs. Time
class Distance(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Distance Analysis")
        self.DATASET = ENTRY_FIELD(self,"Dataset Name","d1","","")
        ### Atom Selections Frame
        
        self.ATOMS_FRAME = tk.Frame(self)
        self.ATOMS_FRAME.pack(side="top",fill='both')
        self.ATOM1_FRAME = ENTRY_FIELD(self.ATOMS_FRAME,"Atom 1 Selection Mask","@1")
        self.ATOM2_FRAME = ENTRY_FIELD(self.ATOMS_FRAME,"Atom 2 Selection Mask","@2")
        ### File Output Frame
        self.OUTFILE = ENTRY_FIELD(self,"Output Filename?","Distances.dat")
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
        
    def command_string(self):
        dataset = self.DATASET.value()
        atom1 = self.ATOM1_FRAME.value()
        atom2 = self.ATOM2_FRAME.value()
        fileout = self.OUTFILE.value()
        full_string = commentary(f"Calculation of distance between centroids of [{atom1}] and [{atom2}] over time, written to {fileout}.  Dataset named [{dataset}]")
        full_string += f"distance {dataset} {atom1} {atom2} out {fileout}\n"
        return full_string

### Angle between three atoms vs. Time
class Angle(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Angle Analysis")
        self.DATASET = ENTRY_FIELD(self,"Dataset Name","a1","","")
        ### Atom Selections Frame
        self.ATOMS_FRAME = tk.Frame(self)
        self.ATOMS_FRAME.pack(side="top",fill='both')
        self.ATOM1_FRAME = ENTRY_FIELD(self.ATOMS_FRAME,"Atom 1 Selection Mask","@1")
        self.ATOM2_FRAME = ENTRY_FIELD(self.ATOMS_FRAME,"Atom 2 Selection Mask","@2")
        self.ATOM3_FRAME = ENTRY_FIELD(self.ATOMS_FRAME,"Atom 3 Selection Mask","@3")
        ### File Output Frame
        self.OUTFILE = ENTRY_FIELD(self,"Output Filename?","Angles.dat")
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
        
    def command_string(self):
        dataset = self.DATASET.value()
        atom1 = self.ATOM1_FRAME.value()
        atom2 = self.ATOM2_FRAME.value()
        atom3 = self.ATOM3_FRAME.value()
        fileout = self.OUTFILE.value()
        full_string  = commentary(f"Angle between atoms [{atom1}] [{atom2}] and [{atom3}] over time, written to {fileout}.  Dataset named [{dataset}]")
        full_string +=f"angle {dataset} {atom1} {atom2} {atom3} out {fileout}\n"
        return full_string
    
### Dihedral/Torsion between four atoms v. Time
class Torsion(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Dihedral/Torsion Analysis")
        self.DATASET = ENTRY_FIELD(self,"Dataset Name","t1","","")
        ### Atom Selections Frame
        self.ATOMS_FRAME = tk.Frame(self)
        self.ATOMS_FRAME.pack(side="top",fill='both')
        self.ATOM1_FRAME = ENTRY_FIELD(self.ATOMS_FRAME,"Atom 1 Selection Mask","@1")
        self.ATOM2_FRAME = ENTRY_FIELD(self.ATOMS_FRAME,"Atom 2 Selection Mask","@2")
        self.ATOM3_FRAME = ENTRY_FIELD(self.ATOMS_FRAME,"Atom 3 Selection Mask","@3")
        self.ATOM4_FRAME = ENTRY_FIELD(self.ATOMS_FRAME,"Atom 4 Selection Mask","@4")
        ### File Output Frame
        self.OUTFILE = ENTRY_FIELD(self,"Output Filename?","Torsions.dat")
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
        
    def command_string(self):
        dataset = self.DATASET.value()
        atom1 = self.ATOM1_FRAME.value()
        atom2 = self.ATOM2_FRAME.value()
        atom3 = self.ATOM3_FRAME.value()
        atom4 = self.ATOM4_FRAME.value()
        fileout = self.OUTFILE.value()
        full_string = commentary(f"Dihedral/Torsion of atoms in [{atom1}] [{atom2}] [{atom3}] [{atom4}] over time, written to {fileout}.  Dataset named [{dataset}]")
        full_string += f"dihedral {dataset} {atom1} {atom2} {atom3} {atom4} out {fileout}\n"
        return full_string
    
### Nucleotide Sugar Puckering v. Time
class NucleotidePucker(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Nucleotide Sugar Pucker Analysis")
        self.DATASET = ENTRY_FIELD(self,"Dataset Name","pucker1","","")
        ### Atom Selections Frame
        self.ATOMS_FRAME = tk.Frame(self)
        self.ATOMS_FRAME.pack(side="top",fill='both')
        self.ATOM1_FRAME = ENTRY_FIELD(self.ATOMS_FRAME,"Residue Number",":1")
        ### File Output Frame
        self.OUTFILE = ENTRY_FIELD(self,"Output Filename?","NucleotidePucker.dat")
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
        
    def command_string(self):
        dataset = self.DATASET.value()
        res_num = self.ATOM1_FRAME.value()
        fileout = self.OUTPUT.value()
        full_string = commentary(f"Nucleotide Sugar Puckering for residue {res_num} over time, written to {fileout}.  Dataset named [{dataset}].")
        full_string += f"pucker {dataset} :{res_num}@C1’ :{res_num}@C2’ :{res_num}@C3’ :{res_num}@C4’ :{res_num}@O4’ range360 out {fileout}\n"
        return full_string

### RMSF By Residue
class RMSF(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"RMSF By Residue")
        self.DATASET = ENTRY_FIELD(self,"Dataset Name","RMSF_ByRes","","")
        ### RMSF Selection Mask Frame
        self.RMSF_FRAME = ENTRY_FIELD(self,"RMSF Selection Mask",":1-100")
        ### File Output Frame
        self.OUTFILE = ENTRY_FIELD(self,"Output Filename?","RMSF_ByRes.dat")
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
    def command_string(self):
        dataset = self.DATASET.value()
        sel_mask = self.RMSF_FRAME.value()
        fileout = self.OUTFILE.value()
        full_string = commentary(f"Root-Mean-Squared Fluctuation for atoms in [{sel_mask}], written to {fileout}.  Dataset named [{dataset}]")
        full_string += f"atomicfluct {dataset} {sel_mask} out {fileout} byres\n"
        return full_string
        

### Correlated Motion between Residues
class CorrelatedMotion(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Correlated Motion")
        self.DATASET = ENTRY_FIELD(self,"Dataset Name","corrpath","","")
        ### RMSF Selection Mask Frame
        self.CORREL_FRAME = ENTRY_FIELD(self,"Correlation Selection Mask",":1-100")
        ### File Output Frame
        self.OUTFILE = ENTRY_FIELD(self,"Output Filename?","Correl.dat")
        
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
    def command_string(self):
        dataset = self.DATASET.value()
        sel_mask = self.CORREL_FRAME.value()
        fileout = self.OUTFILE.value()
        full_string = commentary(f"Correlated motion of residues in [{sel_mask}], written to {fileout}.  Dataset named [{dataset}].")
        full_string+= f"matrix correl name {dataset} out {fileout} {sel_mask} byres\n"
        return full_string

### Normal Mode Analysis
class NormalModes(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Normal Modes Analysis")
        self.DATASET = ENTRY_FIELD(self,"Dataset Name","nma_data","","")
        ### RMSF Selection Mask Frame
        self.NMA_FRAME = ENTRY_FIELD(self,"Normal Modes Selection Mask",":1-100@CA")
        self.NUM_MODES = ENTRY_FIELD(self,"Number of Modes","100")
        ### File Output Frame
        self.OUTFILE = ENTRY_FIELD(self,"Output Filename?","normal_modes.nmd")
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
    def command_string(self):
        dataset = self.DATASET.value()
        sel_mask = self.NMA_FRAME.value()
        num_modes = self.NUM_MODES.value()
        fileout = self.OUTFILE.value()
        full_string = commentary(f"Normal Mode Analysis of atoms in [{sel_mask}], calculating the first {num_modes} modes.  Dataset named [{dataset}].  File output written to {fileout}.")
        full_string = f"matrix covar name {dataset} {sel_mask}\n"
        full_string+= f"diagmatrix {dataset} \\\n"
        full_string+= f"vecs {num_modes} \\\n"
        full_string+= f"reduce nmwiz mnwizvecs {num_modes} \\\n"
        full_string+= f"nmwizfile {fileout} \\\n"
        full_string+= f"nmwizmask {sel_mask}\n"
        return full_string

### Hydrogen Bonding Analysis
class HydrogenBonds(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Hydrogen Bond Analysis")
        self.DISTANCE = ENTRY_FIELD(self,"H-Bond cutoff distance","3.0")
        self.INTRAMOL = BOOLEAN_RESPONSE(self,"Exclude intramolecular hydrogen bonds?","nointramol ","")
        ### File Output Frame
        self.OUTFILE = ENTRY_FIELD(self,"Output Filename?","HBonds.dat")
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
    def command_string(self):
        nointramol = self.INTRAMOL.value()
        fileout = self.OUTFILE.value()
        distance = self.DISTANCE.value()
        temp_string = f"Hydrogen Bonding Analysis performed with a {distance}A cutoff distance. "
        if nointramol == "nointramol ":
            temp_string+="Intramolecular hydrogen bonds have been excluded from this calculation. "
        full_string = commentary(temp_string)
        full_string +=f"hbond dist {distance} avgout {fileout} {nointramol}\n"
        return full_string

### Radial Distribution Function
class RadialDistribution(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Radial Distribution Function")
        self.BINSPLIT = ENTRY_FIELD(self,"Bin Separation","0.5")
        self.MAXDIST  = ENTRY_FIELD(self,"Maximum Distance","10.0")
        self.SOLVENT  = ENTRY_FIELD(self,"Solvent Molecule Mask",":WAT")
        ### File Output Frame
        self.OUTFILE = ENTRY_FIELD(self,"Output Filename?","RadialDistribution.dat")
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
    def command_string(self):
        fileout = self.OUTFILE.value()
        split   = self.BINSPLIT.value()
        maxdist = self.MAXDIST.value()
        solvent = self.SOLVENT.value()
        full_string = commentary(f"Radial Distribution Function calculated with a bin separation of {split}A out to a maximum distance of {maxdist}A, using [{solvent}] for solvent.  File written to {fileout}. ")
        full_string += f"rdf out {fileout} {split} {maxdist} {solvent}\n"
        return full_string

    
class Clustering(tk.Frame):
    def __init__(self,master):
        super().__init__(master, highlightbackground="black", highlightthickness=2)
        self.master = master
        self.pack(fill='both')
        self.TITLE = TITLE(self,"Clustering")
        self.options=["SELECT CLUSTERING ALGORITHM","Heirarchical Agglomerative", "DBSCAN", "Density Peaks","K-means"]
        self.algo_type = tk.StringVar(self,"SELECT CLUSTERING ALGORITHM")
        self.algo_type.set("SELECT CLUSTERING ALGORITHM")
        
### ADD THIS   # cluster↓ [crdset <crd set> | nocoords]
        
        ### Select Algorithm Frame
        self.ALGORITHM = tk.Frame(self, highlightbackground="grey", highlightthickness=2)
        self.ALGORITHM.pack(fill="both")
        self.WORKING = tk.Frame(self.ALGORITHM)
        self.CURR_ALGO = tk.Frame(self.WORKING)
        self.CURR_ALGO.pack(side="top")
        self.algo_choice = tk.OptionMenu(self.ALGORITHM ,self.algo_type, *self.options, command=self.update_working)
        self.algo_choice.pack(side="top")
        
        ### Chosen Algorithm Frame
        self.WORKING.pack(side="top")
        self.DIST_OPTS = Clust_Distance_Options(self)
        self.OUTP_OPTS = Clust_Output_Options(self)
        self.COOR_OPTS = Clust_Coordinate_Output_Options(self)
        self.DIST_OPTS.pack(side="top")
        self.OUTP_OPTS.pack(side="top")
        self.COOR_OPTS.pack(side="top")
        ### SELF-DESTRUCT BUTTON
        SELF_DESTRUCT_BUTTON(self)
        
    def update_working(self,event):
        ## clear previous algorithm choice
        self.CURR_ALGO.pack_forget()
        if self.algo_type.get() == "Heirarchical Agglomerative":
            self.CURR_ALGO = HeirAgglo(self.WORKING)
        elif self.algo_type.get() == "DBSCAN":
            self.CURR_ALGO = DBScan(self.WORKING)
        elif self.algo_type.get() == "Density Peaks":
            self.CURR_ALGO = DPeaks(self.WORKING)
        elif self.algo_type.get() == "K-means":
            self.CURR_ALGO = Kmeans(self.WORKING)
        else:
            self.CURR_ALGO = tk.Frame(self.WORKING)
        self.CURR_ALGO.pack(side="top",fill="both")
        
    def command_string(self):
        full_string = commentary("Clustering performed.  Please see the CPPTRAJ manual for details of keywords below.")
        full_string += "cluster "
        full_string += self.CURR_ALGO.command_string()
        full_string += self.DIST_OPTS.command_string()
        full_string += self.OUTP_OPTS.command_string()
        full_string += self.COOR_OPTS.command_string()
        return full_string
        
         
### Main Analysis Frame
class Analysis_Frame(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.options=["SELECT ANALYSIS","RMSD","RMSF","Correlated Motion","Normal Modes",
                      "Hydrogen Bond Analysis","Radial Distribution Function",
                      "Distance","Angle","Dihedral/Torsion","Clustering"]
        self.analysis_type = tk.StringVar()
        self.analysis_type.set("SELECT ANALYSIS")
        self.pack(fill="both")

        ### ADD NEW ANALYSIS FRAME
        self.ADD_ANALYSIS_FRAME = tk.Frame(self)
        self.ADD_ANALYSIS_FRAME.pack(side="bottom")
        self.drop = tk.OptionMenu(self.ADD_ANALYSIS_FRAME ,self.analysis_type, *self.options)
        self.drop.pack(side="left")
        self.button = tk.Button(self.ADD_ANALYSIS_FRAME,text="ADD ANALYSIS",command=self.add_analysis)
        self.button.pack(side="left")

    def add_analysis(self):
        antype = self.analysis_type.get()
        self.ADD_ANALYSIS_FRAME.pack_forget()
        if antype == "RMSD":
            newframe = RMSD(self)
        if antype == "RMSF":
            newframe = RMSF(self)
        if antype == "Correlated Motion":
            newframe = CorrelatedMotion(self)
        if antype == "Normal Modes":
            newframe = NormalModes(self)
        if antype == "Hydrogen Bond Analysis":
            newframe = HydrogenBonds(self)
        if antype == "Radial Distribution Function":
            newframe = RadialDistribution(self)
        if antype == "Distance":
            newframe = Distance(self)
        if antype == "Angle":
            newframe = Angle(self)
        if antype == "Dihedral/Torsion":
            newframe = Torsion(self)
        if antype == "Clustering":
            newframe = Clustering(self)
        if antype != "SELECT ANALYSIS":
            newframe.pack(side="top")
        self.ADD_ANALYSIS_FRAME.pack(side="bottom")
    def command_string(self):
        return_string = commentary("Full set of analyses listed below.  Each individual analysis is provided with additional explanation based on values given.")
        for frame in self.pack_slaves():
            if getattr(frame,"command_string",False):
                return_string += frame.command_string()
                return_string += "\n"
        return_string += "\n"
        return return_string
        
        
