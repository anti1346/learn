import subprocess

# # Apache 서버 프로세스 확인
# subprocess.run(['clear'])
# subprocess.run(['ps', '-ef', '|', 'grep', '-v', 'grep', '|', 'grep', 'httpd'])

def print_apache_server_processes():
    subprocess.run(['clear'])
    ps_output = subprocess.run(['ps', '-ef'], capture_output=True, text=True)
    apache_processes = [line for line in ps_output.stdout.split('\n') if 'httpd' in line and 'grep' not in line]
    for process in apache_processes:
        print(process)

# Apache 서버 프로세스 확인
print_apache_server_processes()
