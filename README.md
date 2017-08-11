# Test the 360Giving Registry

This repository contains nightly tests against the [360Giving data registry](http://www.threesixtygiving.org/data/data-registry/).

The list of test runs is [on Travis](https://travis-ci.org/ThreeSixtyGiving/test_registry/builds). We use Travis Cron to trigger nightly builds.

We have two Travis jobs, on which runs `py.test` and the other runs `test_datagetter.sh`, see [.travis.yml](.travis.yml) for the full definition.
