#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Print each command before executing it
set -x

# Ensure NEURDBPATH is set
NEURDBPATH=${NEURDBPATH:-/code/neurdb-dev}

# Clean files
rm -rf $NEURDBPATH/psql || true
rm $NEURDBPATH/logfile  || true

# Print and execute commands
mkdir -p $NEURDBPATH/psql

cd $NEURDBPATH

make distclean || true

# Compile the PostgreSQL.
./configure --prefix=$NEURDBPATH/psql
make -j
make install

echo "Done! Now start the database"
mkdir -p $NEURDBPATH/psql/data
./psql/bin/initdb -D $NEURDBPATH/psql/data
$NEURDBPATH/psql/bin/pg_ctl -D $NEURDBPATH/psql/data -l logfile start

# Wait a few seconds to ensure the database is up and running
until $NEURDBPATH/psql/bin/psql -h localhost -p 5432 -U postgres -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

# Load dataset
$NEURDBPATH/psql/bin/psql -h localhost -p 5432 -U postgres -f $NEURDBPATH/dataset/iris_psql.sql
echo "DB Started!"

# Install packages
pip3 install -r $NEURDBPATH/contrib/nr/pysrc/requirement.txt

# Run python server
nohup python3 $NEURDBPATH/contrib/nr/pysrc/pg_interface.py &
echo "Python Server started!"

# Compile Extension
cd /code/neurdb-dev/contrib/nr
cargo pgrx init --pg16 $NEURDBPATH/psql/bin/pg_config
cargo clean
cargo pgrx install --pg-config $NEURDBPATH/psql/bin/pg_config --release
echo "Extension Compile Done"

$NEURDBPATH/psql/bin/psql -h localhost -U postgres -p 5432 -c "CREATE EXTENSION neurdb_extension;"
echo "Install Extension Done"

echo "Plese use 'control + c' to exist the logging print"

# Continue
tail -f /dev/null

