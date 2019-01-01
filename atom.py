import requests
import json

from pprint import pprint

class Atom:
    def __init__(self, *coeffs):
        self.coeffs = coeffs
        self.symbol = coeffs[1]
        self.name = coeffs[2]
        self.numbr = int(coeffs[0])
        self.electrons = None
        self.protons = coeffs[0]
        self.neutrons = None
        self.atomic_mass = None
        self.color = None
        self.electronic_configuration = None
        self.electronegativity = None
        self.atomic_radius = None
        self.ion_radius = None
        self.van_del_waals_radius = None
        self.ionization_energy = None
        self.electron_affinity = None
        self.oxidation_states = None
        self.standard_state = None
        self.bonding_type = None
        self.melting_point = None
        self.boiling_point = None
        self.density = None
        self.group = None
        
    def __repr__(self):
        return 'Atom(values: {!r})'.format(self.coeffs)

    def __add__(self, other):
        return Atom(*(x+y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass

    def curldata(self):
        with open('info.json.py') as f:
            self.data = json.load(f)
            self.atomic_mass = self.data[self.numbr-1]['atomicMass']
            self.color = self.data[self.numbr-1]['cpkHexColor']
            self.electronic_configuration = self.data[self.numbr-1]['electronicConfiguration']
            self.electronegativity = self.data[self.numbr-1]['electronegativity']
            self.atomic_radius = self.data[self.numbr-1]['atomicRadius']
            self.ion_radius = self.data[self.numbr-1]['ionRadius']
            del self.data
