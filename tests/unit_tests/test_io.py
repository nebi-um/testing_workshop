import os
from unittest import TestCase

from testing_workshop.io import CSVReader, FASTAReader, CSVWriter
from tests import ROOT_DIR


class TestIO(TestCase):

    def setUp(self) -> None:
        data_folder = os.path.join(ROOT_DIR, 'data')
        self.df_path_csv = os.path.join(data_folder, 'proteins.csv')
        self.df_path_to_write_csv = os.path.join(data_folder, 'df_to_write.csv')
        self.df_fasta_path = os.path.join(data_folder, 'proteins.faa')

    def tearDown(self) -> None:
        paths_to_remove = [self.df_path_to_write_csv]

        for path in paths_to_remove:
            if os.path.exists(path):
                os.remove(path)

    def test_csv_reader(self):
        reader = CSVReader(self.df_path_csv)
        df = reader.read()
        self.assertEqual(3, df.shape[0])
        self.assertEqual(2, df.shape[1])

    def test_csv_writer(self):
        reader = CSVReader(self.df_path_csv)
        df = reader.read()

        writer = CSVWriter(self.df_path_to_write_csv, index=False)
        writer.write(df)

        self.assertTrue(os.path.exists(self.df_path_to_write_csv))

        reader = CSVReader(self.df_path_to_write_csv)
        df = reader.read()

        self.assertEqual(df.shape[0], 3)
        self.assertEqual(df.shape[1], 2)

    def test_fasta_reader(self):
        reader = FASTAReader(self.df_fasta_path)
        sequences = reader.read()
        self.assertEqual(3, len(list(sequences)))
