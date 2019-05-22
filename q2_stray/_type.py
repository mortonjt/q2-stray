import pandas as pd

from rhapsody.q2 import StrayPosteriorFormat
from rhapsody.q2.plugin_setup import plugin


@plugin.register_transformer
def _1(ff: StrayPosteriorFormat) -> pd.DataFrame:
    df = pd.read_csv(str(ff), sep='\t', comment='#', skip_blank_lines=True,
                     header=True, dtype=object)
    return df


@plugin.register_transformer
def _2(df: pd.DataFrame) -> StrayPosteriorFormat:
    ff = StrayPosteriorFormat()
    df.to_csv(str(ff), sep='\t', header=True, index=True)
    return ff
