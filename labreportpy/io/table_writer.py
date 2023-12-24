r"""Simple class to convert data from a DataFrame to
a LaTeX tabularx/tabularray readable format. Either
print out and copy the output of 'table_writer' or
(better) save it to a .tex file and use
```
\input{your_table_file.tex}
```
inside your tabularx or tabularray environment.
"""
import pandas as pd
from pathlib import Path


class TableWriter:
    r"""Simple class to convert data from a DataFrame to
    a LaTeX tabularx/tabularray readable format. Either
    print out and copy the output of 'table_writer' or
    (better) save it to a .tex file and use
    ``\input{your_table_file.tex}`` inside your tabularx
    or tabularray environment.
    """

    def __init__(self) -> None:
        pass

    def write(self) -> str:
        """
        Writes a table to a .tex file.

        Returns
        -------
        table : str
            String representation of the table.
        """
        table = ""
        for _, series in self.df.iterrows():
            v = [str(s) for s in series.values]
            s = " & ".join(v) + r" \\ " + "\n"
            table += s

        if self.output_file:
            with open(self.output_file, "w") as f:
                f.write(table)

        return table


    def from_df(
        self,
        df: pd.DataFrame,
        output_file: str or Path
    ) -> None:
        """
        Initializes the class with data from a DataFrame.

        Parameters
        ----------
        df : pd.DataFrame
            DataFrame to be converted to table format.
        output_file : str or Path
            Output file path for saving.
        """
        self.df = df
        self.output_file = output_file


    def from_file(
        self,
        input_file: str or Path,
        output_file: str or Path=None
    ) -> str:
        """
        Initializes the class with data from a file.

        Parameters
        ----------
        input_file : str or Path
            Input file containing the data.
        output_file : str or Path
            Output file to write to.

        Returns
        -------
        table: str
            A LaTeX (tabularx/tabularray) compatible string.
        """
        # check if input file is a .txt
        if not input_file.split(".")[-1] == "txt":
            self.df = pd.read_csv(input_file)
        else:
            # read data from .txt, header is first row, use
            # whitespace as delimiter
            self.df = pd.read_csv(
                input_file,
                header=None,
                delim_whitespace=True,
                comment='#'
            )

        self.output_file = output_file

