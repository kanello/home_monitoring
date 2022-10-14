#!/bin/bash
python3 pipeline/loader.py &>/dev/null
[[ $0 = /* ]] && script=$0 || script=$PWD/$0
at -f "$script" 'now + 60 seconds' &>/dev/null