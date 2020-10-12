# SimplApi
 Simple API to register some products.

###### - Creating Virtual Enviorioment
 Go to the root directory of your projects and create a venv through the following commands:

Ex:
```
YOUR TERMINAL

yourpc>$ cd directory
yorpc\directory>$ ls
apiapp  apiproject  db.sqlite3  manage.py requirements.txt
yourpc\directory>$ python venv myvenv
yorpc\directory>$ cd myvenv/Scripts
yorpc\directory\ myvenv\Scripts >$ activate
yorpc\directory\ myvenv\Scripts>$ cd ..
yorpc\directory\ myvenv>$ cd ..
(myvenv)yorpc\directory>$
```

###### - Installing dependencies
Now, let’s install the packages, needed to run our Project ,inside the file “requirements.exe”. 
Ex:
```
(myvenv)yorpc\directory>$ ls
 apiapp  apiproject  db.sqlite3  manage.py requirements.txt
(myvenv)yorpc\directory>$ pip install requirements.txt
```
###### - Runing project
Now that we have our dependencies installed and we’ve already installed our dependencies, let’s run our Project through the the ‘manage.py’ file:
```
(myvenv)yorpc\directory>$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 12, 2020 - 19:41:35
Django version 3.1.2, using settings 'apiproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Ok! Our Api is runing!
### Using methods in /products/:

###### - Let's make a new register.
We'll use the POST command on our terminal to make a new register.
```
yourpc>$ curl -X POST -H "Content-Type: application/json" -d @../data/product.json http://127.0.0.1:8000/products
```


###### - Let's make a new register(json file).
We'll use the POST command on our terminal to make a new register with a json file.
```
yourpc>$ curl -X POST -H "Content-Type: application/json" -d @../data/product.json http://127.0.0.1:8000/products
```
###### - Let's consume our api
We'll use the GET command on our terminal to see the values inside.
```
yourpc>$ curl -X GET http://127.0.0.1:8000/products
```
### Using methods in /product-images/:

###### - Let's make a new register.
We'll use the POST command on our terminal to make a new register.
```
yourpc>$ curl -X POST -H "Content-Type: application/json" -d @../data/product.json http://127.0.0.1:8000/product-images
```

###### - Let's make a new register( json file).
We'll use the POST command on our terminal to make a new register with a json file.
```
yourpc>$ curl -X POST -H "Content-Type: application/json" -d @../data/product.json http://127.0.0.1:8000/product-images
```
###### - Let's consume our api
We'll use the GET command on our terminal to see the values inside.
```
yourpc>$ curl -X GET http://127.0.0.1:8000/product-images
```

