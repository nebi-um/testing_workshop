from typing import List

from testing_workshop.data_structures import Protein, Proteome

from Bio.Blast import NCBIWWW


class BLAST:

    def __init__(self, sequences: Proteome, **kwargs):
        self.query_sequences = sequences
        self.kwargs = kwargs

    def _run(self, sequence: Protein):
        result_handle = NCBIWWW.qblast("blastp", "swissprot", sequence.get_sequence(), **self.kwargs)
        return result_handle

    def run(self):
        result_reports = []
        for sequence in self.query_sequences.get_proteins().values():
            result = self._run(sequence)
            result_reports.append(result)

        return result_reports

