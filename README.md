# teme

## Provisioning

Using [Vagrant](https://www.vagrantup.com) like a boss.

```
vagrant up
vagrant ssh
cd /vagrant
# Make a superuser
./manage.py createsuperuser
# Start the server
./manage.py runserver 0.0.0.0:8000
```

Go to http://localhost:8889

## Production

http://salty-stream-1920.herokuapp.com/

The assets are served from `mds.palcu.ro` because Heroku is shitty.
