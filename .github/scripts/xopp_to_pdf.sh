#!/bin/sh
set -e

scripts_dir="$(realpath $(dirname $0))"
github_dir="$(dirname $scripts_dir)"
root_dir="$(dirname $github_dir)"
xournal_dir="$root/xournal"

for f in $(find $xournal_dir -type f -path '**/*.xopp')
do
    fname="${fname%.*}.pdf"
    xournalapp -p $fname $f
    rm $f
done

