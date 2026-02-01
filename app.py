import subprocess
import json

def run_command(cmd):
    subprocess.run(cmd, shell=False, check=True)

def load_data(data):
    return json.loads(data)
