#!/bin/sh
set -e

cd $(realpath $(dirname $0))
./sync.sh
xournalpp $1
./push.sh xournal
