# Best Practices

### Description
This is a repository containing the best practices assignment for software engineering for scientists. It contains multiple files:

* style.py - a file containing various functions
* get_column_stats - A file that can take a given column and take the standard deviation as well as mean
* basics_test.py - a file containing unit tests for get_column_stats
* basics_test.sh - a shell script that can be run to get these tests working

## How to use


1. Make sure conda is installed

```
$ conda update --yes conda

$ conda config --add channels bioconda

$ echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
```

2. Install required libraries

```
$ conda install --yes python=3.6

$ conda install -y pycodestyle
```

3. Run basics_test.sh 
