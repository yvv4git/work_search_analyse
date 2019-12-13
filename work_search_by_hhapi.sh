#!/bin/bash
DATE=`date +%Y-%m-%d`;
python	hh_search.py -r 'python' -m 100000 -p 10 -o dump/work_hhapi_python_$DATE.txt;
python	hh_search.py -r 'php' -m 100000 -p 10 -o dump/work_hhapi_php_$DATE.txt;
python	hh_search.py -r 'perl' -m 100000 -p 10 -o dump/work_hhapi_perl_$DATE.txt;
python	hh_search.py -r 'java' -m 100000 -p 10 -o dump/work_hhapi_java_$DATE.txt;
python	hh_search.py -r 'android' -m 100000 -p 10 -o dump/work_hhapi_android_$DATE.txt;
python	hh_search.py -r 'js' -m 100000 -p 10 -o dump/work_hhapi_js_$DATE.txt;
python	hh_search.py -r 'системный администратор' -m 100000 -p 10 -o dump/work_hhapi_admin_$DATE.txt;
python	hh_search.py -r 'golang' -m 100000 -p 10 -o dump/work_hhapi_golang_$DATE.txt;
