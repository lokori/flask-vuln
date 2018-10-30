# Vulnerable app

One more target for security practice. Nothing fancy here.

Should you use it, please take note:
*DO NOT RUN THIS ON YOUR OWN LAPTOP FOR OTHER PEOPLE AS A TARGET. RUNNING THIS APPLICATION WILL BE A SECURITY RISK SHOULD YOU DO IT.*

## Run

1. Install Python + Flask (```pip install flask```)
2. ```export FLASK_APP=flask-vuln.py```
3. ```flask run```

Or use ```run.sh```.

Or use ```run_docker.sh``` (which builds the image and starts a container). Remember to stop and remove the container after you're done.

Enjoy the puzzles at ```http://localhost:5000```

# Running properly for other people

If you run this for other people, somewhere, you should add ```--host=0.0.0.0``` to flask command parameters to listen for all IP addresses. Please understand that doing so puts the machine at risk where you run this application and take appropriate measures.

## "Professional" setting

Flask is a single-threaded development server. Which means it hangs and sucks in a workshop setting. 
As a remedy, do something like this:

1. Setup Ubuntu server on EC2, proper firewalls etc.
2. Configure host ip for Ansible
3. ```ansible-playbook playbook.yml -i hosts```
4. ```run-gunicorn.sh```

This runs it through [Gunicorn](http://gunicorn.org/) which is a better implementation for multi-threaded web server.

# About vulnerability scanners

People should try to solve and figure out this manually. Running [OWASP ZAP](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project) will immediately reveal most of the vulnerabilities on this application (as you can expect, given that this is intentionally a soft target for practice) taking all the learning out of the experience.


# License

See [LICENSE](LICENSE)
