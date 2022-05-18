#!/usr/bin/env python3

def InitializeCPPTRAJ(prmtop,trajectory):
    return f"""
### Read in prmtop and trajectory files
parm {prmtop}
trajin {trajectory}
"""

def StripSolvent():
    return """### Remove solvent water
strip :WAT
"""

def StripCounterions(cations="K+",anions="Cl-"):
    return f"""### Remove all counterions
strip :{cations},{anions}
"""

def AutoImage(sel_mask):
    return f"""
### Move the structures to the origin using center of mass of {sel_mask}
autoimage anchor {sel_mask}
"""

def RMSD(sel_mask):
    return f"""
### Orient frames referenced to first frame to minimize overall RMSD of {sel_mask}
### then produce RMSD.dat, which is RMSD vs. Time (recommend line plot)
rms first perres {sel_mask} out RMSD.dat
"""

def RMSF(sel_mask):
    return f"""
### Calculate the fluctuation of residues in the sel_mask selection and output to
### RMSF_ByRes.dat, which is Fluctuation vs. Residue number (recommend bar plot)
atomicfluct RMSF_ByRes {sel_mask} out RMSF_ByRes.dat byres
"""

def Correlation(sel_mask):
    return f"""
### Calculate correlated motion between all residue pairs in sel_mask and output
### to correlation.dat, which is a 2D array of values between -1 and +1. (recommend heatmap)
matrix correl name corrpath out correlation.dat {sel_mask} byres
"""

def NormalModesProtein(sel_mask):
    return f"""
### covariance matrix for protein normal modes
matrix covar name nma_protein {sel_mask}@CA
diagmatrix nma_protein out nma_protein_covar.dat \
vecs 100 reduce nmwiz mnwizvecs 100 \
nmwizfile nma_prot_first_100_modes.nmd \
nmwizmask {sel_mask}@CA
"""

def NormalModesNucleotides(sel_mask):
    return f"""
### covariance matrix for nucleotide normal modes
matrix covar name nma_nucleotide {sel_mask}@P
diagmatrix nma_nucleotide out nma_nucleotide_covar.dat \
vecs 100 reduce nmwiz mnwizvecs 100 \
nmwizfile nma_nucleotides_first_100_modes.nmd \
nmwizmask {sel_mask}@P
"""

def HydrogenBonds(nointramol=False):
    if nointramol:
        return f"""### Hydrogen Bond Analysis for intermolecular hydrogen bonds ONLY
### (useful if you want to see things like dimer interfaces or other                             
### multi-molecule interactions
hbond dist 3.0 avgout HBond_intermolecular.dat nointramol
"""
    return f"""
### Hydrogen Bond Analysis for hydrogen bonds
hbond dist 3.0 avgout HBonds.dat
"""

def RadialDistributionFunction(split=0.5,maxdist=10):
    return f"""
### Radial Distribution Function for solvent waters (:WAT)
### with bin separation of {split}A and a maximum bin size of {maxdist}A.
rdf out RDF.dat {split} {maxdist} :WAT
"""

def Distance(atom1,atom2):
    return f"""### Distance measurements between {atom1} and {atom2} 
### (distances are between centers of mass)
distance d1 {atom1} {atom2} out DISTANCE.dat
"""

def Angle(atom1,atom2,atom3):
    return f"""### Angle Measurements between {atom1}-{atom2}-{atom3}
angle a1 {atom1} {atom2} {atom3} out ANGLE.dat
"""

def Dihedral(atom1,atom2,atom3,atom4):
    return f"""
### Dihedral/Torsion of bond between {atom2} and {atom3} 
### with {atom1} and {atom4} as reference atoms.
dihedral t1 {atom1} {atom2} {atom3} {atom4} out DIHEDRAL.dat range360
"""

def ClusteringKmeans(num_clusters=10):
    return f"""
### Clustering (Requires datasets to cluster on beforehand)
cluster kmeans clusters {num_clusters} \ # specifies 5 clusters desired.
data t1,a1 \  # This is where the NAMED datasets to be clustered on are listed (comma-separated)
out cnumvtime.dat \ # specifies which cluster number each frame belongs to.
summary clustsummary.txt \ # summarizes each cluster
info clustinfo.txt \ # writes additional cluster information
repout clust \ # prefix of output cluster coordinates (clust.00001.rst7)
repfmt restart \ # specifies the ".rst7" format and file extension
bestrep centroid \ # representative frame for each cluster is closest to centroid of cluster.
savenreps 1 \ # save one frame per cluster
clustersvtime clustvtime.txt \ # writes the number of unique clusters seen over time below.
cvtwindow 50 \ # timewindow is 50 frames for clustersvtime above.
cpopvtime cpopvtime.dat # All cluster populations vs. time.
"""

def FinalizeCPPTRAJ():
    return f"""
### final command of the cpptraj input file should be "run" to execute all above queued tasks.
run
"""

prmtop = "file.prmtop"
trajectory = "trajectory.dcd"
sel_mask = ":1-20"


