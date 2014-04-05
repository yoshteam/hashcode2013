#!/bin/bash

# TODO: write some code for the following translation
# input.txt ---> header.txt, links.txt, nodes.txt

grep '^[^ ]* [^ ]* 2' links.txt | awk '{print $2,$1,$3,$4,$5}' > links-duplicated-tmp.txt

cat links.txt links.duplicated-tmp.txt > links-duplicated.txt
