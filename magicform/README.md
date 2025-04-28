# Client-Side Validation Bypass (Form Manipulation)

## Description

This exercise demonstrates a common web vulnerability: **relying solely on client-side validation**.

The form in this task uses HTML attributes like `disabled`, `readonly`, or hidden fields to prevent the user from modifying certain input values. However, these restrictions can be easily bypassed using browser developer tools.

**Important:**  
Server-side validation is missing or insufficient — allowing an attacker to tamper with form fields and submit unauthorized or malicious data.

---

## Exploitation Steps

1. Open the page and inspect the form using browser Developer Tools (`F12`).
2. Locate the input field(s) that are `disabled`, `readonly`, or `hidden`.
3. Remove the restrictive attributes or modify the values directly in the DOM.
4. Submit the form with the modified values.
5. Observe that the server accepts the manipulated input.

---

## Why This is Dangerous

- Attackers can modify hidden values, disabled fields, or restricted options.
- It can lead to unauthorized actions, such as:
  - Changing user roles.
  - Altering product prices.
  - Performing actions normally not allowed via the UI.

---

## Objective for Participants

✅ Find the form with restricted fields.  
✅ Bypass client-side validation using DevTools.  
✅ Successfully submit modified data to the server.

---

## Tip

If a field is `disabled` or `readonly`, simply remove the attribute in the DOM and change its value.  
Remember: **Never trust client-side validation! Always validate on the server.**

---

## Run example

```commandline
python create_db.py
python main.py
```