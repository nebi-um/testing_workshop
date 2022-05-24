from unittest import TestCase

from testing_workshop.api import UniProtAPI


class TestUniProtAPI(TestCase):

    def setUp(self) -> None:
        self.identifier = "Q99J83"

    def test_get_sequence_by_id(self):
        sequence = UniProtAPI().get_protein_sequence_by_id(self.identifier)
        self.assertEqual(275, len(sequence.seq))
        self.assertEqual('sp|Q99J83|ATG5_MOUSE Autophagy protein 5 OS=Mus musculus OX=10090 GN=Atg5 PE=1 SV=1',
                         sequence.description)
        self.assertEqual('sp|Q99J83|ATG5_MOUSE', sequence.id)

    def test_invalid_id(self):
        identifier = "L90J53"
        with self.assertRaises(ValueError):
            UniProtAPI().get_protein_sequence_by_id(identifier)
