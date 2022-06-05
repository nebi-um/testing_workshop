import os
from unittest import TestCase

import pandas as pd

from testing_workshop.api import UniProtAPI
from testing_workshop.data_structures import Protein, Proteome
from testing_workshop.io import CSVWriter, CSVReader
from tests import ROOT_DIR


class TestUniprotPipeline(TestCase):

    def setUp(self) -> None:
        data_folder = os.path.join(ROOT_DIR, 'data')
        self.df_fasta_path = os.path.join(data_folder, 'proteins.faa')
        self.df_write_fasta_path = os.path.join(data_folder, 'proteins_written.faa')

    def tearDown(self) -> None:
        if os.path.exists(self.df_write_fasta_path):
            os.remove(self.df_write_fasta_path)

    def test_pipeline(self):
        seq_id = "Q99J83"
        ref_protein = UniProtAPI().get_protein_sequence_by_id(seq_id)
        ref_protein = Protein(ref_protein.id, ref_protein.seq)

        self.assertEqual(275, len(ref_protein.sequence))
        self.assertEqual('sp|Q99J83|ATG5_MOUSE', ref_protein.identifier)

        proteome = Proteome([ref_protein])
        df_dict = [{"identifier": prot.identifier, "sequence": prot.sequence} for key, prot in proteome.proteins.items()]
        df = pd.DataFrame.from_records(df_dict)

        writer = CSVWriter(self.df_write_fasta_path, index=False)
        writer.write(df)
        self.assertTrue(os.path.exists(self.df_write_fasta_path))

        reader = CSVReader(self.df_write_fasta_path)
        df = reader.read()

        self.assertEqual(df.shape[0], 1)
        self.assertEqual(df.shape[1], 2)