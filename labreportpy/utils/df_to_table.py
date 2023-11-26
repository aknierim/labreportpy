import pandas as pd
from rich.table import Table
from rich.console import Console


def df_to_table(
    df: pd.DataFrame,
    index: bool=True,
    title: str=""
) -> None:
    """Converts and prints a pd.DataFrame to a rich.Table.

    Parameters
    ----------
    df: pd.DataFrame
        DataFrame to be converted to a rich table.
    index: bool
        If True, show the DataFrame index as the first column.
    title: str
        Optional title for the rich table.
    """
    console = Console()

    table = Table(
        title=title,
        box=None,
        header_style="bold magenta"
    )

    if index:
        table.add_column("")

    for col in df.columns:
        table.add_column(col)

    for i in df.itertuples(index=index):
        table.add_row(*map(str,i))

    console.print(table)
