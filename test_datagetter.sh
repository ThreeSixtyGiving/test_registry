#!/bin/bash
set -e
rm -rf datagetter || true
git clone https://github.com/ThreeSixtyGiving/datagetter.git
cd datagetter
pip install -r requirements.txt
mkdir -p data/{original,json_all,json_valid,json_acceptable_license,json_acceptable_license_valid}
# Don't convert because Travis probably doesn't have the RAM
python get.py --no-convert 
