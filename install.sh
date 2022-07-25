#!/bin/bash

rm -r /usr/local/bin/combine-manga-src &> /dev/null
rm -r /usr/local/bin/combine-manga &> /dev/null
cp -f -r ./combine-manga-src /usr/local/bin/combine-manga-src
cp -f ./combine-manga /usr/local/bin/combine-manga
chmod +x /usr/local/bin/combine-manga
