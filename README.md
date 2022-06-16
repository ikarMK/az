# az
#Redis<br/>
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg<br/>
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list<br/>
sudo apt-get update<br/>
sudo apt-get install redis<br/>
sudo redis-server<br/>


#PostgreSQL<br/>
sudo apt update<br/>
sudo apt install postgresql postgresql-contrib<br/>
sudo -u postgres psql<br/>
CREATE DATABASE libsite;<br/>
CREATE USER ikar WITH PASSWORD '18Fihihi.';<br/>
ALTER ROLE ikar SET client_encoding TO 'utf8';<br/>
ALTER ROLE ikar SET default_transaction_isolation TO 'read committed';<br/>
ALTER ROLE ikar SET timezone TO 'UTC';<br/>
GRANT ALL PRIVILEGES ON DATABASE libsite TO ikar;<br/>
\q<br/>


#Project<br/>
source /lib/bin/activate<br/>
cd libsite<br/>
pip install -r requirements.txt<br/>
python3 manage.py makemigrations <br/>
python3 manage.py migrate<br/>
python manage.py runserver  <br/>
