#!/bin/zsh

mkdir -p ${1}

wrk2 -t4 -c10 -d30s -R100 --timeout 1s -s get.lua "${2}/query?id=abc" > ${1}/report_100.txt
wrk2 -t6 -c50 -d30s -R500 --timeout 1s -s get.lua "${2}/query?id=abc" > ${1}/report_500.txt
wrk2 -t8 -c100 -d30s -R1000 --timeout 1s -s get.lua "${2}/query?id=abc" > ${1}/report_1000.txt
wrk2 -t8 -c500 -d30s -R5000 --timeout 1s -s get.lua "${2}/query?id=abc" > ${1}/report_5000.txt
wrk2 -t8 -c1000 -d30s -R10000 --timeout 1s -s get.lua "${2}/query?id=abc" > ${1}/report_10000.txt
