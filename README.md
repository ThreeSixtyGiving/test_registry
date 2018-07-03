# Test the 360Giving Registry

This repository contains nightly tests against the [360Giving data registry](http://www.threesixtygiving.org/data/data-registry/).

The list of test runs is [on Travis](https://travis-ci.org/ThreeSixtyGiving/test_registry/builds). We use Travis Cron to trigger nightly builds.

Running locally:

```
python3 -m venv .ve
source .ve/bin/activate
pip install -r requirements.txt 
py.test
```
