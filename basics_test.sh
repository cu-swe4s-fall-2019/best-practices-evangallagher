#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
source ssshtest

echo "checking pep-8 formatting"

pycodestyle style.py

pycodestyle get_column_stats.py

pycodestyle basics_test.py

echo 'testing mean'

run test_mean python get_column_stats.py --file_name test.txt --column_number 2
assert_in_stdout
assert_no_stderr
assert_exit_code 1

echo 'testing a file of random integers'

(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run test_random_file python get_column_stats.py --file_name data1.txt --column_number 2
assert_stdout
assert_no_stderr
assert_exit_code 1

rm data.txt
