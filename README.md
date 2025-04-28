# Hack the python

Test bench for testing python applications for penetration

# QuickStart

## Installation and Run

You need 8000-8005 open ports

### from github

#### Install

You need python >= 3.12 and pip

```sh
$ git clone https://github.com/DanteOnline/hack-the-python.git
$ cd hack-the-python
$ pip install -r requirements.txt
```

#### Run

In your virtual environment run

```sh
$ python runall.py
```

Go to main menu on [http://127.0.0.1:8000](http://127.0.0.1:8000)

### from Docker image

```commandline
docker run -ti -p 8000-8005:8000-8005 danteonline/hack-the-python
```

### from Dockerfile

#### Install

```sh
$ git clone https://github.com/DanteOnline/hack-the-python.git
$ cd hack-the-python
$ docker compose up --build
```

Go to main menu on [http://127.0.0.1:8000](http://127.0.0.1:8000)

# List of vulnerabilities

- web-client

  - [MagicForm](magicform/README.md)
  - [shoppinglist](shoppinglist/README.md)
  - [myblog](myblog/README.md)
  - [myblog](myblog/README.md)

- web-server
  - [smartcalc](smartcalc/README.md)

- other
    - [sockserver](sockserver/README.md)

- tools:
    - [cookie, csrfserver](tools/REAMDE.md)

# Settings

in myblog/blog/settings.py
`SHOW_VULNS` - variable (default False)
True - show vulnerabilities names in main menu
False - not show vulnerabilities names (project names only)
