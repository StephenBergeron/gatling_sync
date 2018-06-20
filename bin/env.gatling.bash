#!/bin/bash


if [ -z ${GATLING_HOME+x} ]; then
    (echo "[ env.gatling.bash ] set GATLING_HOME and PATH") |& fmt --width=132
    GATLING_HOME=${HOME}/Downloads/gatling-charts-highcharts-bundle-2.3.1
    export GATLING_HOME
    export PATH=$PATH:$GATLING_HOME/bin
else
    (echo "[ env.gatling.bash ] GATLING_HOME is already set") |& fmt --width=132
fi

(echo "[ env.gatling.bash ] ${GATLING_HOME}") |& fmt --width=132
