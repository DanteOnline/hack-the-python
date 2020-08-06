# Hack the python

Test bench for testing python applications for penetration

# QuickStart
## Installation and Run

### from github

#### Install

You need python > 3.6 and pip

```sh
$ git clone https://github.com/DanteOnline/hack-the-python.git
$ cd hack-the-python
$ pip install -r requirements.txt
```

#### Run

If you user python command run runall.py

```sh
$ python runall.py
```

If you user python3 command run runall3.py

```sh
$ python3 runall3.py
```

Go to main menu on [http://127.0.0.1:8000](http://127.0.0.1:8000)
# List of vulnerabilities

- web-client
    - others
        - magicform - site on flask with lock html from
    - SQL injection
        - shoppinglist - site on flask with sql injection
    - xss
        - myblog - site on django with xss (low, middle)
    - csrf
        - myblog - site on django with csrf

- web-server
    - eval injection
        - smartcalc - site on flask with eval injection

- pickle-injection
    - sockserver - console python tcp client and server

- tools:
    - cookie - server on flask to intercept coockies
    - csrfserver - server on flask to csrf attack