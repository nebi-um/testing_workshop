from unittest import TestCase
from unittest.mock import MagicMock

from testing_workshop.data_structures import Protein, Proteome


class TestDataStructures(TestCase):

    def test_protein(self):
        protein = Protein("MyID", "MGWVGKKKSTAGQLAGTANELTKEVLERAVHRESPVIRPDVVVGIPAVDRRPKQ")
        self.assertEqual("MyID", protein.get_identifier())
        self.assertEqual("MGWVGKKKSTAGQLAGTANELTKEVLERAVHRESPVIRPDVVVGIPAVDRRPKQ", protein.get_sequence())

    def test_proteome(self):
        protein1 = MagicMock()
        protein1.get_sequence.return_value = "MASLMLSLGSTSLLPREINKDKLKL"
        protein1.get_identifier.return_value = "MyID"
        proteome = Proteome(proteins=[protein1])
        self.assertIn("MyID", proteome.get_proteins().keys())
        self.assertIn(proteome.get_proteins()["MyID"].get_sequence(), "MASLMLSLGSTSLLPREINKDKLKL")

        sequence = proteome.get_protein_by_id("MyID")
        self.assertEqual(sequence.get_sequence(), "MASLMLSLGSTSLLPREINKDKLKL")
