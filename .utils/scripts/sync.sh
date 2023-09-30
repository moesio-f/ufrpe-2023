#!/bin/sh
set -e

cd $(realpath $(dirname $0))
cd $(./get_root.sh)
git pull
