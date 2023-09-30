#!/bin/sh
set -e

cd $(realpath $(dirname $0))
./sync.sh
xournalpp
./push.sh xournal
