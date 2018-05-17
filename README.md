# gofast-server

### Before you start
  1. This was developed and designed on Linux using Linux tools. It should work on Mac as well, but I have not made any adjustments for Windows
  2. This project requires Python3+. It's amazing I promise!
  3. Make sure you have docker installed, the daemon running, and you are in the docker group

### Getting started
 1. create your virtual environment if you so desire
    - `python -m venv ./venv`
    - `source ./venv/bin/activate`
 2. install the dependencies from requiremetns.txt
    - `pip install -r requirements.txt`
 3. run docker-compose
    - `docker-compose build`
    - `docker-compose up`


### Todo:
 - [ ] Use gunicorn to manage the server
 - [x] Dockerize allthethings
 - [ ] Mount a volume so we don't have to continuously re-build
 - [ ] Nginx for reverse proxying and serving assets (It's faster)
 - [ ] ???
 - [ ] Profit