📄 HTTP STATUS CODES — CHEAT SHEET (PDF)
👉 Follow these steps after the content to save it as a PDF.
🌐 HTTP STATUS CODES – QUICK REFERENCE
🔵 1xx — Informational
Server received request, still processing.
100 Continue – Client can continue request
101 Switching Protocols – Protocol change (HTTP → WebSocket)
🟢 2xx — Success ✅
Request was successful.
Code	Meaning	Real-Life Example
200 OK	Success	Food delivered
201 Created	New resource	Account created
202 Accepted	Processing	Order confirmed
204 No Content	Success, no body	Email deleted
🟡 3xx — Redirection 🔁
Client must go elsewhere.
Code	Meaning	Example
301	Moved permanently	Website changed
302	Temporary redirect	Short detour
304	Not modified	Cached page used
🔴 4xx — Client Errors ❌
Problem with request.
Code	Meaning	Example
400	Bad request	Invalid form
401	Unauthorized	Wrong API key
403	Forbidden	No permission
404	Not found	Wrong URL
405	Method not allowed	GET instead of POST
429	Too many requests	Rate limit hit
🟣 5xx — Server Errors 🔥
Server failed to process request.
Code	Meaning	Example
500	Internal error	Server crash
502	Bad gateway	Invalid upstream
503	Service down	Maintenance
504	Timeout	Server too slow
🧠 GOLDEN RULE
2xx → Success
4xx → Fix your request
5xx → Retry later
🐍 Python Best Practice
response.raise_for_status()
Automatically handles 4xx / 5xx errors.
🎯 Interview One-Liner
HTTP status codes describe the result of an HTTP request, grouped into success, redirection, client errors, and server errors.