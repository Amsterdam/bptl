#!/bin/bash

set -e

queue=${1:-celery}
name=${2:-worker.$queue}

LOGLEVEL=${CELERY_LOGLEVEL:-INFO}
CONCURRENCY=${CELERY_WORKER_CONCURRENCY:-1}

echo "Starting celery worker"
celery worker \
    --app bptl \
    -n $name \
    -l $LOGLEVEL \
    --workdir src \
    -O fair \
    -c $CONCURRENCY \
    -Q $queue
