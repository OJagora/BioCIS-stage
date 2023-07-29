from rdkit import Chem
import hashlib
from rdkit.DataStructs import CreateFromBitString

def getASPfinger(mol, atom = -1, n = 1024) :
    #calculates mol fingerprint without atom of index atom and in a bit vector of size n
    paths = []
    num_atoms = mol.GetNumAtoms()
    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):
            path = Chem.rdmolops.GetShortestPath(mol, i, j)
            #get shortest path between atom of index i and j
            if path and not(atom in list(path)):
                atom_indices = [i] + list(path) + [j]  
                path_atoms = [mol.GetAtomWithIdx(idx) for idx in atom_indices]
                path_smiles = Chem.MolFragmentToSmiles(mol, atom_indices, atomSymbols=None, bondSymbols=None)
                path_smiles_bis = path_smiles[::-1] #backward string
                paths.append(max(path_smiles_bis,path_smiles))

    binary_vector = [0] * n

    for path in paths:
        path_hash = hashlib.sha256(path.encode()).hexdigest()  # Hashing the path using SHA-256
        path_index = int(path_hash, 16) % n  # Convert hash to integer and modulo by n to get the index
        binary_vector[path_index] = 1

    return CreateFromBitString("".join(str(bit) for bit in binary_vector))