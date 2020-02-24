release: psql postgres -c "CREATE USER qtie5 WITH PASSWORD 'password';"; 
psql postgres -c "CREATE DATABASE quicktutordb WITH OWNER qtie5;";
psql postgres -c "ALTER USER qtie5 SUPERUSER CREATEROLE CREATEDB REPLICATION;";
python manage.py makemigrations; 
python manage.py migrate
