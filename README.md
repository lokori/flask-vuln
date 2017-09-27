# Vulnerable app

One more target for security practice. Nothing fancy here.

Should you use it, please take note:
*DO NOT RUN THIS ON YOUR OWN LAPTOP FOR OTHER PEOPLE AS A TARGET. RUNNING THIS APPLICATION WILL BE A SECURITY RISK SHOULD YOU DO IT.*

## Run

1. Install Python + Flask (```pip install flask```)
2. ```export FLASK_APP=flask-vuln.py```
3. ```flask run```

Enjoy the puzzles at ```http://localhost:5000```


# About vulnerability scanners

People should try to solve and figure out this manually. Running [OWASP ZAP](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project) will immediately reveal most of the vulnerabilities on this application (as you can expect, given that this is intentionally a soft target for practice) taking all the learning out of the experience.


# License

See [LICENSE](LICENSE)