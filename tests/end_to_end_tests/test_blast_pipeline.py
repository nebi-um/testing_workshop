import os
from unittest import TestCase

from Bio.Blast import NCBIXML

from testing_workshop.blast import BLAST
from testing_workshop.io import FASTAReader
from tests import ROOT_DIR


class TestBLASTPipeline(TestCase):

    def setUp(self) -> None:
        data_folder = os.path.join(ROOT_DIR, 'data')
        self.df_fasta_path = os.path.join(data_folder, 'proteins.faa')

    def test_pipeline(self):
        reader = FASTAReader(self.df_fasta_path)
        proteome = reader.read_to_proteome()

        protein = proteome.get_protein_by_id(
            "WP_003399671.1")

        self.assertEqual("MGWVGKKKSTAGQLAGTANELTKEVLERAVHRESPVIRPDVVVGIPAVDRRPKQ", protein.get_sequence())
        self.assertEqual(3, len(proteome))

        my_blast = BLAST(proteome, entrez_query="Mycobacterium tubeculosis[organism]")
        results = my_blast.run()
        self.assertEqual(3, len(results))
        for result in results:
            for record in NCBIXML.parse(result):
                self.assertEqual(0, len(record.alignments))
