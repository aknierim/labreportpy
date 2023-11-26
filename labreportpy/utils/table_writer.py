"""Simple script to convert data from a DataFrame to
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

    def __init__(self) -> None:
        pass

    def write(self) -> str:
        """
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


    def from_df(self, df: pd.DataFrame, output_file: str or Path) -> None:
        """
        """
        self.df = df
        self.output_file = output_file


    def from_file(self, input_file: str, output_file: str=None) -> str:
        """Simple function to convert data from a pd.DataFrame
        to a LaTeX compatible (inner) table format.

        Parameters:
        -----------
        input_file: str or Path
             containing your data.

        Returns:
        --------
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

