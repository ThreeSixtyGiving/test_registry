#!/bin/bash
rm -rf datagetter || true
git clone https://github.com/ThreeSixtyGiving/datagetter.git
cd datagetter
pip install -r requirements.txt
mkdir -p data/{original,json_all,json_valid,json_acceptable_license,json_acceptable_license_valid}
# Don't convert big file becasue Travis doesn't have the RAM
python get.py --no-convert-big-files
exit_status=$?
python report.py
echo $GIST_TOKEN > ~/.gist
gist -u https://gist.github.com/30d835ae16e2a30efde8a63acf03628d data/report.csv
exit $exit_status
