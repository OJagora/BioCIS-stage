from rdkit import Chem
import hashlib
from rdkit.DataStructs import CreateFromBitString

def getASPfinger(mol, atom = -1, n = 1024) :
    """getASPfinger calculates the fingerprint of a molecule using the All-Shortest-Path method

    :param mol: RDKit molecule to process
    :param atom: index of the atom to supress for the calculation of the fingerprint. By default, this argument is set to -1,
    meaning that every atom is taken in consideration. The ability to 'supress' an atom is usefull when drawing similarity map,
    so that it is possibe to quantify the impact of the chosen atom in the fingerprint
    :param n: number of bits used to code the fingerprint

    :return: fingerprint in the form of a bit vector of size n"""

    paths = []  #list to contain the shortest path beetween every atom pair
    num_atoms = mol.GetNumAtoms()   #list of atom indices

    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):
            path = Chem.rdmolops.GetShortestPath(mol, i, j) #get shortest path between atom of index i and j
            if path and not(atom in list(path)):
                atom_indices = [i] + list(path) + [j]
                path_smiles = Chem.MolFragmentToSmiles(mol, atom_indices, atomSymbols=None, bondSymbols=None) 
                #get smiles string of the shortest path beetween the two atoms
                path_smiles_bis = path_smiles[::-1] #backward string
                paths.append(max(path_smiles_bis,path_smiles))

    #Hashing paths
    binary_vector = [0] * n

    for path in paths:
        path_hash = hashlib.sha256(path.encode()).hexdigest()  # Hashing the path using SHA-256
        path_index = int(path_hash, 16) % n  # Convert hash to integer and modulo by n to get the index
        binary_vector[path_index] = 1

    return CreateFromBitString("".join(str(bit) for bit in binary_vector))