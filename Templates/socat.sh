#!/bin/bash
EXPECTED_ARGS=1
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` {arg}"
  exit $E_BADARGS
fi

echo "PORT: 2323 Binary: $1"
socat TCP-LISTEN:2323,reuseaddr,fork EXEC:./$1
