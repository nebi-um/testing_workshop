from typing import List, Dict


class Protein:

    def __init__(self, identifier: str, sequence: str):
        """
        Constructor

        Parameters
        ----------
        identifier: str
            protein identifier
        sequence: str
            protein sequence
        """
        self.identifier = identifier
        self.sequence = sequence

    def get_sequence(self) -> str:
        """
        Access protein sequence

        Returns
        -------
        sequence: str
            protein sequence
        """
        return self.sequence

    def get_identifier(self) -> str:
        """
        Access identifier

        Returns
        -------
        identifier: str
            protein identifier
        """
        return self.identifier


class Proteome:

    def __init__(self, proteins: List[Protein] = None):
        """
        Constructor

        Parameters
        ----------
        proteins: List[Protein]

        """
        if proteins is None:
            proteins = []
        self.proteins = {}

        for protein in proteins:
            self.proteins[protein.get_identifier()] = protein

    def __len__(self):
        return len(self.proteins.keys())

    def get_proteins(self) -> Dict[str, Protein]:
        """

        Access proteins

        Returns
        -------
        proteins: Dict[str, Protein]
            dictionary with the identifiers as keys and the Prtein object as value
        """
        return self.proteins

    def add_protein(self, protein: Protein):
        """
        Method to add protein to the proteome

        Parameters
        ----------
        protein: Protein

        """
        self.proteins[protein.get_identifier()] = protein

    def get_protein_by_id(self, identifier: str) -> Protein:
        """
        Access Protein object that belongs to the proteome using the identifier

        Parameters
        ----------
        identifier: str
            protein identifier

        Returns
        -------
        protein: Protein
            protein object

        Raises
        -------
        KeyError: if the identifier does not exist.
        """
        if identifier in self.proteins.keys():
            return self.proteins[identifier]
        else:
            raise KeyError("That protein does not belong to this proteome!")
