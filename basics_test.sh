#!/bin/bash

pycodestyle style.py

pycodestyle get_column_stats.py


run python3 get_column_stats.py --input_file data.txt --col_num 2
  assert_exit_code 0

python get_column_stats.py data.txt

# random testing

echo Test exit code and error message
(for i in `seq 1 100`; do
    echo -e "$RANDOM,$RANDOM,$RANDOM,$RANDOM,$RANDOM";
done )> data.txt
run random_bad_comma python3 get_column_stats.py --input_file data.txt --col_num 2
assert_in_new_std "Input file has incorrect formatting in row"
assert_exit_code 1

V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py data.txt 2
