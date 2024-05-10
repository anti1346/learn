import os
import subprocess
from datetime import datetime
import pexpect
import time

ssl_password = "pw1234"
apache_command = '/usr/local/apache2/sbin/apachectl'

def stop_systemprobe_service():
    subprocess.run(['systemctl', 'stop', 'systemprobe'])

def print_system_status():
    subprocess.run(['clear'])
    subprocess.run(['systemctl', 'status', 'systemprobe'])

def download_extract_ssl_certificates():
    os.chdir("/usr/local/apache2/conf/ssl")
    subprocess.run(['wget', '-q', 'https://pkg.test.com/dl/ssl/apache/www_test_com.tar.gz'])
    subprocess.run(['tar', 'xfz', 'www_test_com.tar.gz'])

def backup_apache_conf():
    current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    config_files = ['httpd.conf', 'extra/httpd-vhosts.conf', 'extra/httpd-ssl.conf']
    original_conf_paths = [f"/usr/local/apache2/conf/original/{file_name}_{current_time}" for file_name in config_files]
    
    for src, dest in zip(config_files, original_conf_paths):
        subprocess.run(['cp', f'/usr/local/apache2/conf/{src}', dest])

def stop_apache_server():
    subprocess.run([apache_command, 'stop'])
    print("\nApache 서버를 종료합니다...")

def wait_for_server_shutdown():
    print("\nApache 서버가 완전히 종료될 때까지 대기합니다.")
    while True:
        apache_status = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if '/usr/local/apache2/sbin/httpd' not in apache_status.stdout:
            break
        time.sleep(1)
        print(".", end="", flush=True)
    print("\nApache 서버가 성공적으로 종료되었습니다.")

def start_apache_server():
    print("\nApache 서버를 시작합니다...")
    proc = pexpect.spawn(f'{apache_command} start')
    proc.expect('Enter pass phrase:')
    proc.sendline(ssl_password)
    proc.interact()
    print("\nApache 서버가 시작되었습니다.\n")

def start_systemprobe_service():
    subprocess.run(['systemctl', 'start', 'systemprobe'])

def print_apache_server_processes():
    subprocess.run(['ps', '-ef', '|', 'grep', '-v', 'grep', '|', 'grep', 'httpd'])

# # systemprobe 서비스 중지
# stop_systemprobe_service()
# # 시스템 상태 출력
# print_system_status()
# # SSL 인증서 다운로드 및 추출
# download_extract_ssl_certificates()
# # Apache 구성 파일 백업
# backup_apache_conf()

# Apache 구성 파일 확인 후 서버 조작
apache_config_check = subprocess.run([f'{apache_command}', '-t'])
if apache_config_check.returncode == 0:
    stop_apache_server()
    wait_for_server_shutdown()
    start_apache_server()
else:
    print("Apache 구성 파일을 확인하는 중 문제가 발생했습니다.")
    exit(1)

# # systemprobe 서비스 시작
# start_systemprobe_service()
# # 시스템 상태 출력
# print_system_status()
# # Apache 서버 프로세스 확인
# print_apache_server_processes()
