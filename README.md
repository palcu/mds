# teme

```
# Get dependencies
sudo pip3 install -r requirements-dev.txt
# Configure database
./manage.py syncdb
# Make a superuser
./manage.py createsuperuser
# Start the server
./manage.py runserver 0.0.0.0:8000
```

# Production

http://salty-stream-1920.herokuapp.com/

The assets are served from `mds.palcu.ro` because Heroku is shitty.
