#q2-stray

qiime2 plugin for aldex2 for differential abundance analysis and time series analysis

#Installation Within your qiime2 environment run

```
conda install -c r r-devtools
echo "library(devtools); devtools::install_github('jsilve24/stray')" | R --no-save
pip install git+https://github.com/mortonjt/q2-stray.git
```

To look at the command line, type
```
qiime stray --help
```