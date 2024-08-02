#!/bin/bash
# copy fit file from source to FIT_OUT one by one.

set -e

if [ $# -ne 1 ]
then
    echo "usage: $0 <source_path>"
    exit
fi

source_path=$1
app_path="/root/running_page"
dest_path="${app_path}/FIT_OUT"

ls ${source_path}/*.fit | while read f
do
    cp ${f} ${dest_path}
    bash "${app_path}/shenjun_scripts/fit2db.sh"
done
