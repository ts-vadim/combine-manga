#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_ROOT="${SCRIPT_DIR}/.."

cd "${PROJECT_ROOT}"

echo -n -e "\e[37m"

status() {
    echo -e "\e[0m> $@\e[37m"
}

ensure_succeded() {
    status $@
    $@
    if [ $? -ne 0 ]; then
        exit
    fi
}

ensure_succeded \
    python -m venv .venv

ensure_succeded \
    . ./.venv/bin/activate

ensure_succeded \
    pip install -r ./requirements.txt
