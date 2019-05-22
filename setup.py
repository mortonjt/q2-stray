# ----------------------------------------------------------------------------
# Copyright (c) 2017-2019, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
from setuptools import setup, find_packages

import versioneer

setup(
    name="q2-stray",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author="Justin Silverman",
    author_email="Justin Silverman <justin.silverman@duke.edu>",
    description=("Bayesian Multinomial Logistic Normal Models through "
                 "Marginally Latent Matrix-T Processes"),
    license='GPLv3',
    url="https://github.com/jsilve24/stray",
    entry_points={
        'qiime2.plugins': ['q2-stray=q2_stray.plugin_setup:plugin']
    },
    scripts=['q2_stray/assets/run_pibble.R'],
    package_data={
        "q2_stray": ['citations.bib'],
    },
    zip_safe=False,
)
