MeatUpServer
============

first, create a virtualenv
```
$ virtualenv env --distibute
```
when running the server, set your bash source to our virtual env
```   
 $ source env/bin/activate
```
then install the dependencies with pip
```
pip install -r requirements.txt
```
and finally start the server with foreman, a tool that comes with the [heroku toolbelt](https://toolbelt.heroku.com/)
```
$ foreman start
```
The server defaults to running on ```localhost:5000```
