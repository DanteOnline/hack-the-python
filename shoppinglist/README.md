# Classic SQL Injection (Flask App)

## Description

This exercise demonstrates a **classic SQL Injection vulnerability**.

The Flask web application dynamically builds SQL queries using user input directly in an **f-string**
(without proper sanitization or parameterization).  
This allows attackers to inject arbitrary SQL code into the query and interact directly with the database.

---

## Exploitation Steps

1. Open the vulnerable page (e.g., search form or login form).
2. Enter a crafted payload into the input field. For example:

```sql
' OR 1=1 --
```

## Example payloads

Bypass authentication:
```sql
' OR 1=1 --
```

Get database structure:
```sql
leo' union all select sql, 1, 1 FROM sqlite_master where '1'='1
```

## Why This is Dangerous

- Attackers can read, modify, or delete sensitive data.
- They can gain unauthorized access to accounts or the entire application.
- In worst cases, full remote code execution on the server is possible.

## Objective for Participants

- ✅ Identify the vulnerable input field.
- ✅ Successfully inject SQL payloads.
- ✅ Bypass authentication or retrieve sensitive database information.

## Tip

Look for any form or input that interacts with the database (login forms, search boxes, etc.).
Try injecting ' OR 1=1 -- and observe the response.

Remember:
Always use parameterized queries or ORM methods that prevent SQL Injection!

## Run

```commandline
python craete_db.py
python main.py
```