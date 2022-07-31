#!/bin/bash

rm -r /usr/local/bin/merge-pages-src &> /dev/null
rm -r /usr/local/bin/merge-pages &> /dev/null
cp -f -r ./merge-pages-src /usr/local/bin/merge-pages-src
cp -f ./merge-pages /usr/local/bin/merge-pages
chmod +x /usr/local/bin/merge-pages
