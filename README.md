# az
#Redis
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis
sudo redis-server


#PostgreSQL
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -u postgres psql
CREATE DATABASE libsite;
CREATE USER ikar WITH PASSWORD '18Fihihi.';
ALTER ROLE ikar SET client_encoding TO 'utf8';
ALTER ROLE ikar SET default_transaction_isolation TO 'read committed';
ALTER ROLE ikar SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE libsite TO ikar;
\q


#Project
source /lib/bin/activate
cd libsite
pip install -r requirements.txt
python3 manage.py makemigrations 
python3 manage.py migrate
python manage.py runserver  
