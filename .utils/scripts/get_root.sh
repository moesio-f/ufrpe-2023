#!/bin/sh
set -e

scripts_dir="$(realpath $(dirname $0))"
utils_dir="$(dirname $scripts_dir)"
root="$(dirname $utils_dir)"
echo $root