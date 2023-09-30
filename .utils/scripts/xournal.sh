#!/bin/sh
set -e

cd $(realpath $(dirname $0))
./sync.sh
xournalapp
./push.sh xournal
