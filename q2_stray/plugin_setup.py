import qiime2
from qiime2.plugin import (Str, Int, Float, Choices, Citations,
                           Metadata, Categorical, Plugin)
from q2_types.feature_table import FeatureTable, Frequency, Composition
from q2_types.feature_data import FeatureData, Differential

import q2_stray
from q2_stray._method import pibble
from q2_stray._type import StrayPosterior


# TODO: will need to fix the version number
__version__ = '0.0.1'

plugin = Plugin(
    name='stray',
    version=__version__,
    website='https://github.com/mortonjt/q2-stray',
    package='q2_stray',
    description=('Analysis Of Differential Abundance Taking '
                 'Sample Variation Into Account'),
    short_description='Plugin for differential abundance analysis.',
    citations=Citations.load('citations.bib', package='q2_stray')
)

plugin.methods.register_function(
    function=pibble,
    name=('Analysis Of Differential Abundance'),
    description=('Performs differential abundance test with phylogenetic prior.'),
    inputs={'table': FeatureTable[Frequency]},
    parameters={'metadata': Metadata,
                'formula': Str,
                'learning_rate': Float,
                'beta1': Float,
                'beta2': Float
    },
    outputs=[('differentials', FeatureData[Differential],
             ('posterior', StrayPosterior)
    )],
    input_descriptions={
        'table': 'The feature table of abundances.'
    },
    parameter_descriptions={
        'metadata': 'Sample metadata',
        'formula': 'The experimental condition of interest.',
        'learning_rate': 'The learning rate of the gradient descent.',
        'beta1': 'First momentum operator in ADAM gradient descent',
        'beta2': 'Second momentum operator in ADAM gradient descent'
    },
    output_descriptions={
        'differentials': 'The estimated per-feature differentials.',
        'posterior': 'The posterior distribution over all of the differentials.'
    }
)

# TODO: Need to add a visualizer to summarize the stray results
