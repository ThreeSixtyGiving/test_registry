# Test the 360Giving Registry

test_registry is a simple check on the [360Giving data registry](http://data.threesixtygiving.org); it checks that the registry contains the fields that we expect, and that they contain the expected data type. The nightly cron is run on [TravisCI](https://travis-ci.org/ThreeSixtyGiving/test_registry/builds). We use Travis Cron to trigger nightly builds.

To run locally:

```
python3 -m venv .ve
source .ve/bin/activate
pip install -r requirements.txt
py.test
```
