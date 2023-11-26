import pandas as pd
import numpy as np


def diff(
    df_meas: pd.DataFrame,
) -> pd.DataFrame:
    """Calculates the difference of two consecutive
    data points and saves it to a pd.DataFrame.

    Parameters
    ----------
    df_meas: pd.DataFrame
        Measurement data.
    
    Returns
    -------
    df: pd.DataFrame
        DataFrame containing the calculated differences.
    """
    diff_kernel = np.array([1,-1])

    df = pd.DataFrame()

    for col in df_meas.columns:
        df[col] = np.convolve(df_meas[col], diff_kernel, "same")

    return df
