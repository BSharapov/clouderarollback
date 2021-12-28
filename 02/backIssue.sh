#!/bin/bash

curl -X POST -u "admin:admin" -i http://localhost:7180/api/v33/clusters/NC-DE-CDH6.3/services/yarn/commands/start &>/dev/null

