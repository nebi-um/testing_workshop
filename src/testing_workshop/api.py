import urllib
from io import StringIO
from urllib.error import HTTPError
from urllib.request import Request

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


class UniProtAPI:

    def __init__(self):
        """
        Constructor of the API
        """
        self.url = "https://www.uniprot.org/uniprot/"

    @staticmethod
    def make_request(url: str) -> bytes:
        """

        Parameters
        ----------
        url: str
            URL to perform request

        Returns
        -------
        bytes: bytes
            should be decoded afterwards
        """
        request = urllib.request.Request(url)

        try:
            with urllib.request.urlopen(request) as response:
                res = response.read()
        except HTTPError:
            raise ValueError("Identifier does not exist")

        return res

    def get_protein_sequence_by_id(self, uniprot_id: str) -> SeqRecord:
        """

        Parameters
        ----------
        uniprot_id: str
            uniprot entry identifier

        Returns
        -------
        sequence record: SeqRecord
            Biopython SeqRecord object
        """
        url_to_request = f"{self.url}{uniprot_id}&format=fasta"

        res = self.make_request(url_to_request)

        sequences = SeqIO.parse(StringIO(res.decode("utf-8")), format="fasta")
        sequences = list(sequences)
        if len(sequences) > 0:
            return sequences[0]
        else:
            raise ValueError("marmelada")
