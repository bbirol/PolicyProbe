# 🔐 Policy Probe: HTTP Header Security Scanner

Policy Probe is a Python-based tool that analyzes HTTP response headers for key security headers 
and provides a risk assessment score.



# 🚀 Features

-Analyzes HTTP headers of a given URL.

-Checks for critical security headers like Strict-Transport-Security, Content-Security-Policy, and others.

-Provides a weighted protection score.

-Displays results in a table format.

-Allows scanning multiple URLs.



# 🔒 Security Headers Analyzed

The tool checks for these headers:

-Strict-Transport-Security (HSTS)

-Content-Security-Policy (CSP)

X-Frame-Options

-X-Content-Type-Options

-Referrer-Policy

-Permissions-Policy



# ⚙️ Requirements (If Running as Python File)

Install the required libraries using pip:

*pip install requests colorama tabulate*



# 💻 Example Output

[+] Starting HTTP Headers Analysis for: https://example.com

Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'

[+] Security Headers Analysis:
Checking: Strict-Transport-Security... ✓ Present
Checking: Content-Security-Policy... ✓ Present

+--------------------------+--------+-----------------+
| Header                   | Weight | Status          |
+--------------------------+--------+-----------------+
| Strict-Transport-Security | 2.0    | ✓ Present      |
| Content-Security-Policy   | 3.0    | ✓ Present      |
+--------------------------+--------+-----------------+

[+] Risk Assessment:
→ Weighted Protection Score: 8.00/10
[~] Good: Minor issues found.



# 🏆 Risk Assessment

10/10: Excellent (All headers are present)

7-9: Good (Minor issues)

4-6: Warning (Some headers missing)

1-3: High Risk (Most headers missing)



