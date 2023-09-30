#!/bin/sh
set -e

commit_msg="$1: update $(date +'%H:%M-%d/%m/%y')"
cd $(realpath $(dirname $0))
cd $(./get_root.sh)
git add .
git commit -m "$commit_msg"
git push