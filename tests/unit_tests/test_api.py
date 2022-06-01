from unittest import TestCase
from unittest.mock import patch, MagicMock, Mock

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
        with self.assertRaises(ValueError) as exception:
            UniProtAPI().get_protein_sequence_by_id(identifier)

        self.assertEqual(str(exception.exception), "Identifier does not exist")

    def test_with_mock(self):
        with patch('urllib.request.urlopen') as mock_request:
            content = ">sp|Q99J83|ATG5_MOUSE Autophagy protein 5 OS=Mus musculus OX=10090 GN=Atg5 PE=1 SV=1\nAAAAATTTTAAAA"
            content = bytes(content, 'utf-8')
            mock_request.return_value.__enter__.return_value.read.return_value = content

            sequence = UniProtAPI().get_protein_sequence_by_id(self.identifier)
            self.assertEqual(13, len(sequence.seq))
            self.assertEqual('sp|Q99J83|ATG5_MOUSE Autophagy protein 5 OS=Mus musculus OX=10090 GN=Atg5 PE=1 SV=1',
                             sequence.description)
            self.assertEqual('sp|Q99J83|ATG5_MOUSE', sequence.id)
            mock_request.assert_called_once()
            mock_request.return_value.__enter__.return_value.read.assert_called_once()