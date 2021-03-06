from atom import Atom
import re

mole = 6.02214076*(10**23)

class PeriodicTable:
    def __init__(self, atoms):
        self.atoms = atoms
        self.size = len(atoms)
        self.groups = dict()
        self.groups["Alkali metali"] = ["Li", "Na" ,"K" ,"Rb", "Cs","Fr"]
        self.groups["Alkaline earth metal"] = ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"]
        self.groups["Group 3 elements"] = ["O", "S", "Se", "Te", "Po", "Lv"]
        self.groups["Chalcogen the oxygen family"] = ["F", "Cl", "Br", "I", "At", "Ts"]
        self.groups["Noble Gases"] = ["He", "Ne", "Ar", "Kr", "Xe", "Rn"]

    def __len__(self):
        return len(self.atoms)

    def get(self, index):
        return self.atoms[index]

    def add(self, atom):
        return self.atoms.append(atom)

    def delete(self, atom):
        return self.atoms.delete(atom)

    def __repr__(self):
        represent = ""
        counter = 0
        for atom in self.atoms:
            represent += atom.symbol + " " 
            counter += 1
            if counter % 8 == 0:
                represent += "\n" 
        return represent
    
    def find(self, query):
        for atom in atoms:
            if atom.symbol == query or atom.name == query:
                return True
        return False

    def checkgroup(self, query):
        for atom in self.atoms:
            if atom.symbol == query or atom.name == query:
                for key in self.groups.keys():
                    if atom.symbol in self.groups[key]:
                        return (key, atom)
        return None

    def createcompound(self, formula):
            for idx, name in enumerate(formula[:]):
                if isinstance(name,str):
                    if sum(c.isupper() for c in name)>1:
                        tmp = []
                        for c in name:
                            if c.isupper():
                                tmp.append([c])
                            else:
                                tmp[-1].append(c)
                        formula.pop(idx)
                        for t in tmp[::-1]:
                            formula.insert(idx,"".join(t))
            return formula

        

file = open("atoms.txt", "r")
atoms = []

for line in file.readlines():
    first = line.find("\t")
    numbr = line[0:first].strip('\n\t')
    symbol = line[first+1:first+3].strip('\t\n')
    name = line[first+3:len(line)].strip('\t\n')

    a = Atom(numbr, symbol, name)
    a.importdata()
    
    atoms.append(a)

periodicTable = PeriodicTable(atoms)
print(periodicTable)
file.close()
