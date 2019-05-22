import os
import qiime2
import numpy as np
import pandas as pd
from biom import Table
import tempfile
import subprocess



def run_commands(cmds, verbose=True):
    if verbose:
        print("Running external command line application(s). This may print "
              "messages to stdout and/or stderr.")
        print("The command(s) being run are below. These commands cannot "
              "be manually re-run as they will depend on temporary files that "
              "no longer exist.")
    for cmd in cmds:
        if verbose:
            print("\nCommand:", end=' ')
            print(" ".join(cmd), end='\n\n')
        subprocess.run(cmd, check=True)


def pibble(table: pd.DataFrame,
           metadata: qiime2.Metadata,
           formula: str,
           learning_rate: float=1e-3,
           beta1: float=0.9,
           beta2: float=0.99) -> pd.DataFrame, pd.DataFrame:

    with tempfile.TemporaryDirectory() as temp_dir_name:
        biom_fp = os.path.join(temp_dir_name, 'input.tsv.biom')
        map_fp = os.path.join(temp_dir_name, 'input.map.txt')
        differential_fp = os.path.join(temp_dir_name, 'output.differential.csv')
        posterior_fp = os.path.join(temp_dir_name, 'output.posterior.csv')

        table.to_csv(biom_fp, sep='\t')
        metadata.to_dataframe().to_csv(map_fp, sep='\t')

        cmd = ['run_pibble.R', biom_fp, map_fp, formula, learning_rate, beta1, beta2,
               differential_fp, posterior_fp]
        cmd = list(map(str, cmd))

        try:
            run_commands([cmd])
        except subprocess.CalledProcessError as e:
            raise Exception("An error was encountered while running stray"
                            " in R (return code %d), please inspect stdout"
                            " and stderr to learn more." % e.returncode)

        lam_summary = pd.read_csv(differential_fp, index_col=0)

        alr_diffs = summary[['covariate', 'coord', 'mean']]
        alr_diffs = differentials.pivot('coord', 'covariate', 'mean')
        diffs = np.vstack((alr_diffs.values, np.zeros(alr_diffs.shape[1])))
        # convert to alr coordinates
        diffs = diffs - diffs.mean(axis=0)
        differential = pd.Dataframe(
            diff, columns=alr_diffs.columns, index=table.index)

        posterior = pd.read_csv(posterior_fp, index_col=0)
        return differential, posterior
