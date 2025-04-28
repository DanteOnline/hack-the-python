# Remote Code Execution via Untrusted Pickle Deserialization

## Description

This exercise demonstrates a **Remote Code Execution (RCE)** vulnerability caused by **unsafe deserialization** 
of untrusted data using Python's `pickle` module.

The server application listens on a TCP socket, accepts a client connection, and sends a serialized (`pickle`d) malicious Python object.  
When the client **unsafely deserializes** this object using `pickle.loads()`, arbitrary code execution occurs.

---

## Exploitation Steps

1. Connect to the vulnerable server (localhost:9999).
2. Receive the malicious payload (a pickled object).
3. Deserialize the received data using `pickle.loads()`.
4. Observe that arbitrary system commands are executed as part of the payload.

---

## Example Malicious Payload

The `EvilPayload` class uses Python's special method `__reduce__` to:

- Write a message `"You've been hacked by Evil Pickle!!!"` into a file `evil_msg.txt`.
- Launch `notepad.exe` to display the file (on Windows).

**Sample payload behavior:**

```python
import pickle
pickle.loads(received_data)
```

## Why This is Dangerous

- Deserialization of untrusted data is highly dangerous, especially with formats like pickle that can execute arbitrary code.
- Attackers can perform any action the server process has permission for — file manipulation, shell access, data exfiltration, and more.
- Vulnerabilities of this type have led to critical breaches in real-world applications.

## Objective for Participants

- ✅ Recognize that untrusted pickle data should never be deserialized directly.
- ✅ Successfully demonstrate code execution upon deserialization.

## Tip

Always use safer alternatives for serialization of untrusted input, like:

- json (for plain data)
- Specialized safe deserialization libraries
- Or strictly validate/trust data sources before deserialization.

Never trust data coming from network sockets or external clients if using pickle!