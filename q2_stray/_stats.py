from qiime2.plugin import SemanticType, model
from q2_types.sample_data import SampleData


StrayPosterior = SemanticType('StrayPosterior',
                              variant_of=SampleData.field['type'])


class StrayPosteriorFormat(model.TextFileFormat):
    def validate(*args):
        pass


StrayPosteriorDirFmt = model.SingleFileDirectoryFormat(
    'StrayPosteriorDirFmt', 'posterior.tsv', StrayPosteriorFormat)
