import subprocess
import time
import pexpect

ssl_password = "pw1234"
apache_command = '/usr/local/apache2/sbin/apachectl'

def stop_apache_server():
    subprocess.run([apache_command, 'stop'])
    print("\nApache 서버를 종료합니다...")

def wait_for_server_shutdown():
    print("\nApache 서버가 완전히 종료될 때까지 대기합니다...")
    start_time = time.time() - 1
    while True:
        apache_status = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if '/usr/local/apache2/sbin/httpd' not in apache_status.stdout:
            break
        elapsed_time = int(time.time() - start_time)
        print(f"{elapsed_time}초 대기 중... 아파치 서버를 종료 중입니다.")
        time.sleep(1)
    print("Apache 서버가 성공적으로 종료되었습니다.\n")

def start_apache_server():
    print("Apache 서버를 시작합니다...")
    proc = pexpect.spawn(f'{apache_command} start')
    proc.expect('Enter pass phrase:')
    proc.sendline(ssl_password)
    proc.interact()
    print("\nApache 서버가 시작되었습니다.\n")

# Apache 구성 파일 확인
apache_config_check = subprocess.run([f'{apache_command}', '-t'])
if apache_config_check.returncode == 0:
    stop_apache_server()
    wait_for_server_shutdown()
    start_apache_server()
else:
    print("Apache 구성 파일을 확인하는 중 문제가 발생했습니다.")
    exit(1)
