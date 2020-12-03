#!/bin/bash
DATE=`date +%Y-%m-%d`;
DIR_DUMP='/app/dump';
DIR_CMD='/app/cmd';

python	$DIR_CMD/hh_search.py -r 'python' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_python_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'php' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_php_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'perl' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_perl_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'java' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_java_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'android' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_android_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'js' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_js_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'nodejs' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_nodejs_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'системный администратор' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_admin_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'golang' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_golang_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'ruby' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_ruby_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'data scince' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_data_science_$DATE.txt;
python	$DIR_CMD/hh_search.py -r 'AI' -m 100000 -p 10 -o $DIR_DUMP/work_hhapi_ai_$DATE.txt;

python3 cmd/analyse_salary.py work_hhapi_python_2017-12-11.txt.csv
python3 cmd/analyse_salary.py work_hhapi_python_2020-12-03.txt.csv