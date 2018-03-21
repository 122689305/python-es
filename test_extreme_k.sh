#!/bin/bash

for n in `seq 10 10 100`; do
    for k in `seq 4 2 8`; do
        python test_extreme_k.py $n $k
    done
done
