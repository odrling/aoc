#!/bin/sh
# arnold didn't like to get the file all at once
./format_input.sh < input_1 | xargs -I _ sh -c "echo _ && sleep 0.001" | arnoldc -run solution_01.arnoldc
