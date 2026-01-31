import subprocess
import pickle

def run_command(cmd):
    subprocess.Popen(cmd, shell=True)

password = "admin123"
run_command("ls")
