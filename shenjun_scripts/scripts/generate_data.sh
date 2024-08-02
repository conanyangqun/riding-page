#!/bin/bash
# generate data manually.

set -e

export IGNORE_START_END_RANGE=200
export IGNORE_RANGE=200
export IGNORE_BEFORE_SAVING=1
title="我的骑行记录"
YOUR_NAME="神骏"

cd /root/running_page

python3 run_page/fit_sync.py

python3 run_page/gen_svg.py \
    --from-db \
    --title "${title}" \
    --type grid \
    --athlete "$YOUR_NAME" \
    --output assets/grid.svg \
    --min-distance 10.0 \
    --special-color yellow \
    --special-color2 red \
    --special-distance 20 \
    --special-distance2 40 \
    --use-localtime

python3 run_page/gen_svg.py \
    --from-db --title "${title}" \
    --type github \
    --athlete "$YOUR_NAME" \
    --special-distance 10 \
    --special-distance2 20 \
    --special-color yellow \
    --special-color2 red \
    --output assets/github.svg \
    --use-localtime \
    --min-distance 0.5

python3 run_page/gen_svg.py \
    --from-db \
    --type circular \
    --use-localtime
