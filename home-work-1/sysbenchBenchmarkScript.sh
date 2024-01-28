#!/bin/bash

TestCases=(
    #"cpu --cpu-max-prime= 1000"
    #"cpu --cpu-max-prime= 1000"
    #"memory --memory-block-size= 2K"
    #"memory --memory-block-size= 4K"
    "fileio --file-test-mode=rndrw --file-total-size=3G"
    "fileio --file-test-mode=seqwr --file-total-size=3G"
    )

# Iterate over test cases
for testCase in "${TestCases[@]}"; do
    read -r mode parameter value <<<"$testCase"
    echo "Running sysbench with Mode: $mode, Parameter: $parameter, Value: $value"
    
    filename="${mode}_${parameter}_${value// /}.text"

    if [[ $mode == "fileio" ]]; then
        sysbench --test=fileio --file-total-size=3G --time=30 --file-test-mode=$value prepare
    fi

    for ((i=1; i<=5; i++)); do
        echo "Run $i:" | tee -a "$filename"
        results=$(sysbench $mode $parameter$value --time=30 run)
        echo "Results:" | tee -a "$filename"
        echo "$results" | tee -a "$filename"
        echo "----------------------------------------"| tee -a "$filename"
    done

    if [[ $mode == "fileio" ]]; then
        sysbench --test=fileio --file-total-size=3G --time=30 --file-test-mode=$value cleanup
    fi

done
