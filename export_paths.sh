#!/bin/bash
export current_directory=$PWD
echo $current_directory
export PYTHONPATH="$PYTHONPATH:$current_directory"
echo $PYTHONPATH
