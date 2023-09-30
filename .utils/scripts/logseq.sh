#!/bin/sh
set -e

cd $(realpath $(dirname $0))
./sync.sh
logseq
./push.sh logseq
