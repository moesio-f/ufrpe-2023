#!/bin/sh
set -e

scripts_dir="$(realpath $(dirname $0))"
github_dir="$(dirname $scripts_dir)"
root_dir="$(dirname $github_dir)"
xournal_dir="$root_dir/xournal"

for f in $(find $xournal_dir -type f -path '**/*.xopp')
do
    fname="${f%.*}.pdf"
    xournalpp -p $fname $f
    rm $f
done

