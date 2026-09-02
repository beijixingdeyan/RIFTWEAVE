# Security

Report vulnerabilities via GitHub Security Advisories (private). No credentials in repo.

- Do not commit `.env`, `*.pem`, or `Saved/Config/*.ini`
- CI checks for secret patterns (`AKIA`, `ghp_`)
