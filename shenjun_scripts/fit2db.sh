#!/bin/bash
# process fit files and save to db.

set -e

export IGNORE_START_END_RANGE=200
export IGNORE_RANGE=200
export IGNORE_BEFORE_SAVING=1
title="我的骑行记录"
YOUR_NAME="神骏"

cd /root/running_page

python3 run_page/fit_sync.py
