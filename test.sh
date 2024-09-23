#!/bin/bash

# Define test cases with input and expected output
declare -a test_cases=(
    "1 3 2"  # Input list for test 1
    "10 20 30 40"  # Input list for test 2
    "5 2 9 1 7"  # Input list for test 3
)

declare -a expected_outputs=(
    "Median: 2.00"  # Expected output for test 1
    "Median: 25.00"  # Expected output for test 2
    "Median: 5.00"  # Expected output for test 3
)

# Function to run each test case
run_test() {
    local input="$1"
    local expected_output="$2"

    # Run the Python script with the provided input
    output=$(echo "$input" | python3 student.py)

    # Compare the actual output with the expected output
    if [[ "$output" == "$expected_output" ]]; then
        echo "Test passed for input: $input"
    else
        echo "Test failed for input: $input"
        echo "Expected: $expected_output"
        echo "Got: $output"
    fi
}

# Iterate over test cases and run each one
for i in "${!test_cases[@]}"; do
    run_test "${test_cases[$i]}" "${expected_outputs[$i]}"
done
