from pathlib import Path
from typing import Union, AnyStr, TextIO

from Bio import SeqIO
from typing import IO
import pandas as pd

from testing_workshop.data_structures import Protein, Proteome


class CSVReader:
    """
    Class that implements the class Reader and reads CSV, TSV and other format files.
    """

    def __init__(self, filepath_or_buffer: Union[str, Path, IO[AnyStr], TextIO], sep: str = ",", **kwargs):
        self.file_path_or_buffer = filepath_or_buffer
        self.sep = sep
        self.kwargs = kwargs

    def read(self):
        return pd.read_csv(self.file_path_or_buffer, **self.kwargs)


class CSVWriter:

    def __init__(self, filepath_or_buffer: Union[str, Path, IO[AnyStr], TextIO], sep: str = ",", **kwargs):
        self.file_path_or_buffer = filepath_or_buffer
        self.sep = sep
        self.kwargs = kwargs

    def write(self, df):
        df.to_csv(self.file_path_or_buffer, **self.kwargs)


class FASTAReader:

    def __init__(self, filepath_or_buffer: Union[str, Path, IO[AnyStr], TextIO], **kwargs):
        self.file_path_or_buffer = filepath_or_buffer
        self.kwargs = kwargs

    def read(self):
        fasta_sequences = SeqIO.parse(open(self.file_path_or_buffer), 'fasta', **self.kwargs)
        return fasta_sequences

    def read_to_proteome(self):
        fasta_sequences = SeqIO.parse(open(self.file_path_or_buffer), 'fasta', **self.kwargs)
        proteome = Proteome()
        for sequence in fasta_sequences:
            new_protein = Protein(identifier=sequence.id, sequence=sequence.seq)
            proteome.add_protein(new_protein)

        return proteome

