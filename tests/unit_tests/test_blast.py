from unittest import TestCase
from unittest.mock import Mock

from Bio.Blast import NCBIXML

from testing_workshop.blast import BLAST


class TestBlast(TestCase):

    def setUp(self) -> None:
        self.proteome = Mock()
        self.protein1 = Mock()
        self.protein1.get_sequence.return_value = "MASLMLSLGSTSLLPREINKDKLKL"
        self.proteome.get_proteins.return_value = {"MyID": self.protein1}

    def test_blast(self):
        my_blast = BLAST(self.proteome, entrez_query="Arabidopsis thaliana[organism]")
        results = my_blast.run()
        for record in NCBIXML.parse(results[0]):
            self.assertEqual(3, len(record.alignments))
