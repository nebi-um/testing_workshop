import os
from unittest import TestCase

from testing_workshop.io import FASTAReader
from tests import ROOT_DIR


class TestIODataStructures(TestCase):

    def setUp(self) -> None:
        data_folder = os.path.join(ROOT_DIR, 'data')
        self.df_fasta_path = os.path.join(data_folder, 'proteins.faa')

    def test_fasta_reader_data_structures(self):
        reader = FASTAReader(self.df_fasta_path)
        proteome = reader.read_to_proteome()

        protein = proteome.get_protein_by_id(
            "WP_003399671.1")

        self.assertEqual("MGWVGKKKSTAGQLAGTANELTKEVLERAVHRESPVIRPDVVVGIPAVDRRPKQ", protein.get_sequence())
        self.assertEqual(3, len(proteome))
