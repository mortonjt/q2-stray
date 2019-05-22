from qiime2.plugin import SemanticType, model
from q2_types.feature_data import FeatureData


StrayPosterior = SemanticType('StrayPosterior',
                           variant_of=FeatureData.field['type'])


class StrayPosteriorFormat(model.TextFileFormat):
    def validate(*args):
        pass


StrayPosteriorDirFmt = model.SingleFileDirectoryFormat(
    'StrayPosteriorDirFmt', 'conditionals.tsv', StrayPosteriorFormat)
