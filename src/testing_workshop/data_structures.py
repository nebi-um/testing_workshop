from typing import List


class Protein:

    def __init__(self, identifier: str, sequence: str):
        self.identifier = identifier
        self.sequence = sequence

    def get_sequence(self):
        return self.sequence

    def get_identifier(self):
        return self.identifier


class Proteome:

    def __init__(self, proteins: List[Protein] = None):
        if proteins is None:
            proteins = []
        self.proteins = {}

        for protein in proteins:
            self.proteins[protein.get_identifier()] = protein

    def __len__(self):
        return len(self.proteins.keys())

    def get_proteins(self):
        return self.proteins

    def add_protein(self, protein: Protein):
        self.proteins[protein.get_identifier()] = protein

    def get_protein_by_id(self, identifier):
        if identifier in self.proteins.keys():
            return self.proteins[identifier]
        else:
            raise KeyError("That protein does not belong to this proteome!")
