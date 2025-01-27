#!/usr/bin/env bash

if [ ! -f .env ]; then
  echo ".env file not found!"
  exit 1
fi

set -a
source .env
set +a