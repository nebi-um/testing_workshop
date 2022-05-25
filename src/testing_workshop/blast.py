from io import StringIO
from typing import List

from testing_workshop.data_structures import Protein, Proteome

from Bio.Blast import NCBIWWW


class BLAST:

    def __init__(self, sequences: Proteome, **kwargs):
        """

        Parameters
        ----------
        sequences: Proteome
            Proteome object
        kwargs
            arguments to be passed to NCBIWWW.qblast
        """
        self.query_sequences = sequences
        self.kwargs = kwargs

    def _run(self, sequence: Protein) -> StringIO:
        """
        Private method to run blast with a protein as query sequence

        Parameters
        ----------
        sequence: Protein
            Protein object

        Returns
        -------
        result_handle: StringIO
            result handle
        """
        result_handle = NCBIWWW.qblast("blastp", "swissprot", sequence.get_sequence(), **self.kwargs)
        return result_handle

    def run(self) -> List[StringIO]:
        """

        Method to run the BLAST

        Returns
        -------
        result_reports: List[StringIO]
        """
        result_reports = []
        for sequence in self.query_sequences.get_proteins().values():
            result = self._run(sequence)
            result_reports.append(result)

        return result_reports

