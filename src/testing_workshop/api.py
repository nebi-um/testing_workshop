import urllib
from io import StringIO
from urllib.error import HTTPError

from Bio import SeqIO


class UniProtAPI:

    def __init__(self):
        self.url = "https://www.uniprot.org/uniprot/"

    @staticmethod
    def make_request(url):
        request = urllib.request.Request(url)
        return request

    def get_protein_sequence_by_id(self, uniprot_id):
        url_to_request = f"{self.url}{uniprot_id}&format=fasta"
        request = self.make_request(url_to_request)
        try:
            with urllib.request.urlopen(request) as response:
                res = response.read()
        except HTTPError:
            raise ValueError("Identifier does not exist")

        sequences = SeqIO.parse(StringIO(res.decode("utf-8")), format="fasta")
        sequences = list(sequences)
        if len(sequences) > 0:
            return sequences[0]
        else:
            raise ValueError()
