import subprocess
import getpass
import os
import sys
import signal

def print_colored(message, color='default'):
    colors = {
        'default': '\033[0m',
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'orange': '\033[33m',  # ANSI escape code for orange may vary, 33 is one possibility
        'blue': '\033[94m',
    }
    color_code = colors.get(color, colors['default'])
    print(f"{color_code}{message}{colors['default']}")

def custom_message(signal, frame):
    print_colored("\nExit: Ctrl+C pressed. Exiting gracefully.", 'blue')
    sys.exit(0)

signal.signal(signal.SIGINT, custom_message)

def is_root():
    return os.geteuid() == 0

if is_root():
    print_colored("[*] Warning: script is running as root.", "orange")
else:
    print_colored("[*] Permission denied: root privileges required", "red")
    sys.exit(0)

current_working_dir = os.getcwd()
# current_user = getpass.getuser()
current_user = os.getenv('SUDO_USER') or os.getenv('USER')
parent_directory = os.path.abspath(os.path.join(current_working_dir, os.pardir))
project_name = input("[*] Enter project name: ")
domain_name = input("[*] Enter domain name: ")

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        
# List of sudo commands to run sequentially
commands = [
    "sudo apt update",
    "sudo apt install nginx",
    "sudo apt update",
    "sudo ufw allow 'Nginx HTTP'",
    "sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools -y",
    "sudo apt install python3-venv -y",
    f"python3 -m venv {parent_directory}/env",
    f"{parent_directory}/env/bin/python -m pip install --upgrade pip"
    f"{parent_directory}/env/bin/python -m pip install wheel",
    f"{parent_directory}/env/bin/python -m pip install gunicorn flask requests",
    f"sudo chown -R {current_user}:{current_user} {parent_directory}/env",
]

for cmd in commands:
    run_command(cmd)

#################  SERVICES ####################

serviceData = f"""
[Unit] 
Description=Gunicorn instance to serve {project_name}
After=network.target

[Service]
User={current_user}
Group=www-data
WorkingDirectory={current_working_dir}
Environment="PATH={parent_directory}/env/bin"
ExecStart={parent_directory}/env/bin/gunicorn --workers 3 --bind unix:{project_name}.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
"""

sitesAvailableData = f"""
server {{
    listen 80;
    server_name {domain_name} www.{domain_name};

    location / {{
        include proxy_params;
        proxy_pass http://unix:{current_working_dir}/{project_name}.sock;
    }}
}}
"""

service_file_path = f"/etc/systemd/system/{project_name}.service"
with open(service_file_path, 'w') as service_file:
    service_file.write(serviceData)
print_colored(f"[*] created file : {service_file_path}", "blue")
run_command(f"sudo chown root:root {service_file_path}")

sites_available_file_path = f"/etc/nginx/sites-available/{project_name}"
with open(sites_available_file_path, 'w') as sites_available_file:
    sites_available_file.write(sitesAvailableData)

print_colored(f"[*] created file : {sites_available_file_path}", "blue")
run_command(f"sudo chown root:root {sites_available_file_path}")

commands = [
    f"sudo systemctl start {project_name}",
    f"sudo systemctl enable {project_name}",
    f"sudo ln -s /etc/nginx/sites-available/{project_name} /etc/nginx/sites-enabled",
    "sudo nginx -t",
    "sudo systemctl restart nginx",
    "sudo ufw delete allow 5000",
    "sudo ufw allow 'Nginx Full",
    f"sudo systemctl status {project_name}",
]

for cmd in commands:
    run_command(cmd)


print_colored("[*] Script Executed Successfully", "green")