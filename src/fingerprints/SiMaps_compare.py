from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from rdkit.Chem.Draw import SimilarityMaps
from rdkit import DataStructs
import os
from all_shortest_paths import getASPfinger

#=================== EXEMPLES ==================#
#===============================================#

#======= Construction des fichiers =============#
num = 0
print('Index of the example :')
num = input()
current = os.path.dirname(os.path.realpath(__file__))
path = current + '/output/'
file = 'example'+str(num)+'/'
os.mkdir(path+file)

#======= Generation des molecules ==============#
m1 = 'CC1(C=CN2[C@@H](CC13C(=O)C4=CC=CC=C4N3)C(=O)N5CCC=C5C2=O)C'
print("Enter first molecule's SMILES :")
m1 = input()
m2 = 'CC1=CC2=C(C(=C1)O)C(=C3C(=O)CC[C@@H]([C@@]3(O2)C(=O)OC)O)O'
print("Enter second molecule's SMILES :")
m2 = input()

mol = Chem.MolFromSmiles(m1)
refmol = Chem.MolFromSmiles(m2)

#======= Affichage des molecules ===============#

im = Draw.MolsToGridImage((mol,refmol),molsPerRow=2, subImgSize=(500,500),legends=["(a)","(b)"])
im.save(path+file+'sideBside.png')

Draw.MolToFile(mol,path+file+'mol.png')
Draw.MolToFile(refmol,path+file+'refmol.png')

#======= Construction des cartes de similarite =#
# definition des generateur

def GetSimMorgan(refmol, mol):
    fig, maxweight = SimilarityMaps.GetSimilarityMapForFingerprint(refmol,
                    mol, lambda m,idx: SimilarityMaps.GetMorganFingerprint(m, atomId=idx, radius=2),
                    metric=DataStructs.TanimotoSimilarity)
    return fig

def GetSimASP(refmol, mol):
    fig, maxweight = SimilarityMaps.GetSimilarityMapForFingerprint(refmol,
                    mol, lambda m,idx: getASPfinger(m, atom=idx),
                    metric=DataStructs.TanimotoSimilarity)
    return fig

#calculation of the 4 different similarity maps

ref_sim_morg = GetSimMorgan(refmol,mol)
mol_sim_morg = GetSimMorgan(mol,refmol)

ref_sim_asp = GetSimASP(refmol,mol)
mol_sim_asp = GetSimASP(mol,refmol)

#save the figures
ref_sim_morg.savefig(path+file+'morganSimMap1.png',dpi = 150, bbox_inches='tight')
mol_sim_morg.savefig(path+file+'morganSimMap2.png',dpi = 150, bbox_inches='tight')

ref_sim_asp.savefig(path+file+'AspSimMap1.png',dpi = 150, bbox_inches='tight')
mol_sim_asp.savefig(path+file+'AspSimMap2.png',dpi = 150, bbox_inches='tight')

#========== Calcul des fingerprints ==========#

mol_MFP = AllChem.GetMorganFingerprintAsBitVect(mol, useChirality=True, radius=2)
refmol_MFP = AllChem.GetMorganFingerprintAsBitVect(refmol, useChirality=True, radius=2)

mol_ASP = getASPfinger(mol, atom = -1)
refmol_ASP = getASPfinger(refmol, atom = -1)

#========= Calcul des Tanimoto ===============#

MG_score = DataStructs.TanimotoSimilarity(mol_MFP,refmol_MFP)
ASP_score = DataStructs.TanimotoSimilarity(mol_ASP,refmol_ASP)
#ASP_score = SimiASP(mol_ASP,refmol_ASP)

#========== Write file ===============#

f = open(path+file+'data.txt','w')
data = "mol : " + m1 + '\n' + "refmol : " + m2 + '\n'
data += '\n'
data += "Morgan Tanimoto : " + str(MG_score) + '\n'
data += "All Shortest Paths : " + str(ASP_score)

f.write(data)
f.close()




