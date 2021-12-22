#!/bin/sh

set -e

until mysql -h ${NETOPSIO_DB_HOST} -p${NETOPSIO_DB_PASS} -e "show databases"; do
    >&2 echo "${NETOPSIO_DB_HOST} not ready, yet."
    sleep 1
done

>&2 echo "${NETOPSIO_DB_HOST} ready, proceeding."
exec "$@"
