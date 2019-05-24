# q2-stray

qiime2 plugin for aldex2 for differential abundance analysis and time series analysis

# Installation

Within your qiime2 environment run

```
conda install -c r r-devtools
echo "library(devtools); devtools::install_github('jsilve24/stray')" | R --no-save
pip install git+https://github.com/mortonjt/q2-stray.git
```

To look at the command line, type
```
qiime stray --help
```

# Quick start

Let's try testing this out with the [88 soils study](https://aem.asm.org/content/75/15/5111).
First, let's import the abundance table as a qiime2 Artifact.

```
qiime tools import \
    --input-path 88soils-table.biom \
    --output-path 88soils-table.qza \
    --type FeatureTable[Frequency]
```

This table is quite sparse, so we'll limit it to microbe that are observed in at least 10 samples
for the sake of this tutorial

```
qiime feature-table filter-features \
    --i-table 88soils-table.qza \
    --p-min-samples 10 \
    --o-filtered-table 88soils-filtered-table.qza
```