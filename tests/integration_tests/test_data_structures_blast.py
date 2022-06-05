import os
from unittest import TestCase
from unittest.mock import patch

from Bio.Blast import NCBIXML

from testing_workshop.blast import BLAST
from testing_workshop.data_structures import Protein, Proteome
from tests import ROOT_DIR


class TestDataStructuresBLAST(TestCase):

    def setUp(self) -> None:
        data_folder = os.path.join(ROOT_DIR, 'data')
        self.blast_xml = os.path.join(data_folder, 'blast_response.xml')

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
        results = my_blast.run()
        for record in NCBIXML.parse(results[0]):
            self.assertEqual(3, len(record.alignments))

    def test_data_structures_mocked_blast(self):
        # NCBIWWW.qblast("blastp", "swissprot", sequence.get_sequence(), **self.kwargs)
        with patch('Bio.Blast.NCBIWWW.qblast') as mock_request:
            content = open(self.blast_xml)
            mock_request.return_value = content

            protein = Protein("MyID", "MASLMLSLGSTSLLPREINKDKLKL")
            proteome = Proteome(proteins=[protein])

            my_blast = BLAST(sequences=proteome, entrez_query="Arabidopsis thaliana[organism]")
            results = my_blast.run()
            for record in NCBIXML.parse(results[0]):
                self.assertEqual(3, len(record.alignments))

            mock_request.assert_called_once()
            mock_request.assert_called_with("blastp", "swissprot", 'MASLMLSLGSTSLLPREINKDKLKL', entrez_query='Arabidopsis thaliana[organism]')