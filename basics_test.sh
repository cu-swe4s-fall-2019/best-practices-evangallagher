#!/bin/bash

pycodestyle style.py

pycodestyle get_column_stats.py

(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py data.txt 2

stdev(col_num)
avg(col_num)


V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py data.txt 2
