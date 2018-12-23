#!/usr/bin/env bash
set -x
picocom -b 115200 "$1"
