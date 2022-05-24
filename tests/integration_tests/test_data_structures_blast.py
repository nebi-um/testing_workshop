from unittest import TestCase

from Bio.Blast import NCBIXML

from testing_workshop.blast import BLAST
from testing_workshop.data_structures import Protein, Proteome


class TestDataStructuresBLAST(TestCase):

    def test_data_structures(self):
        protein = Protein("MyID", "MASLMLSLGSTSLLPREINKDKLKL")
        proteome = Proteome(proteins=[protein])

        self.assertIn("MyID", proteome.get_proteins().keys())
        self.assertIn(proteome.get_proteins()["MyID"].get_sequence(), "MASLMLSLGSTSLLPREINKDKLKL")

        sequence = proteome.get_protein_by_id("MyID")
        self.assertEqual(sequence.get_sequence(), "MASLMLSLGSTSLLPREINKDKLKL")

    def test_data_structures_blast(self):
        protein = Protein("MyID", "MASLMLSLGSTSLLPREINKDKLKL")
        proteome = Proteome(proteins=[protein])

        my_blast = BLAST(sequences=proteome, entrez_query="Arabidopsis thaliana[organism]")
        my_blast.run()
        results = my_blast.run()
        for record in NCBIXML.parse(results[0]):
            self.assertEqual(3, len(record.alignments))
