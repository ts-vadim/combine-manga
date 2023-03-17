#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_ROOT="${SCRIPT_DIR}/.."
INSTALL_DIR="/usr/local/bin"

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

rm -f "${INSTALL_DIR}/merge-pdf.pyz"
rm -f "${INSTALL_DIR}/merge-pdf"

ensure_succeded \
    python -m zipapp -m "main:main" -o "merge-pdf.pyz" src
ensure_succeded \
    cp -f "./merge-pdf.pyz" "${INSTALL_DIR}/merge-pdf.pyz"

ensure_succeded \
    cp -f "./merge-pdf" "${INSTALL_DIR}/merge-pdf"
ensure_succeded \
    chmod +x "${INSTALL_DIR}/merge-pdf"

ensure_succeded \
    merge-pdf -h
