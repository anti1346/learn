import subprocess
import requests
from datetime import datetime, timedelta
import time

# Slack 웹훅 URL
webhook_url = "https://hooks.slack.com/services/webhook_url"
# Slack 채널 이름
slack_channel = "#slack_channel"

# 각 데몬에 대한 마지막 Slack 메시지 발송 시간을 저장하는 딕셔너리
last_notification_times = {}

def send_slack_message(message):
    payload = {
        "channel": slack_channel,
        "text": message
    }
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  # HTTP 요청 오류가 발생하면 예외 발생
        print("Slack 알람 전송 완료")
    except requests.exceptions.RequestException as e:
        print("Slack 알람 전송 실패:", e)

def check_daemon_status(daemon_name):
    # ps 명령어로 데몬 상태 확인
    ps_output = subprocess.run(['ps', 'aux', '|', 'grep', '-v', 'grep'], capture_output=True, text=True)
    if daemon_name not in ps_output.stdout:
        # 현재 시간 저장
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        # 마지막으로 알람을 보낸 시간 가져오기
        last_notification_time = last_notification_times.get(daemon_name)
        if last_notification_time is None:
            # 최초로 다운되었을 때 Slack 메시지 발송
            send_slack_message(f"[{formatted_time}] {daemon_name} 데몬이 다운되었습니다.")
            # 현재 시간으로 업데이트
            last_notification_times[daemon_name] = current_time
        else:
            # 최초로 다운된 시간으로부터 경과한 시간 계산
            elapsed_time = int((current_time - last_notification_time).total_seconds() // 60)
            # 1분, 5분, 10분 경과 후에 메시지 추가 발송
            if elapsed_time in [1, 5, 10]:
                send_slack_message(f"[{formatted_time}] {daemon_name} 데몬이 {elapsed_time}분 동안 다운되었습니다.")
            # 1시간 이상 경과한 경우 마지막 알림 시간 초기화
            if elapsed_time >= 60:
                last_notification_times[daemon_name] = current_time

def monitor_daemons():
    daemons_to_monitor = ['httpd', 'named']
    while True:
        for daemon in daemons_to_monitor:
            check_daemon_status(daemon)
        # 1분 대기
        time.sleep(60)

if __name__ == "__main__":
    monitor_daemons()


### 백그라운드 실행
# nohup python daemon_monitor_slack_alert.py > /dev/null 2>&1 &
