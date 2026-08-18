"""Uploads scripts/tornex-category-audit.php to the WordPress root on
production (same convention as tornex-import.php etc.)."""
import ftplib
import os
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

env = {}
with open(os.path.join(ROOT, '.env'), encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        env[k] = v

LOCAL_FILE = os.path.join(ROOT, 'scripts', 'tornex-category-audit.php')
REMOTE_PATH = 'public_html/tornex-category-audit.php'


def connect():
    ftp = ftplib.FTP()
    ftp.connect(env['DEPLOY_HOST'], int(env.get('DEPLOY_PORT', 21)), timeout=25)
    ftp.login(env['DEPLOY_USER'], env['DEPLOY_PASSWORD'])
    return ftp


def main():
    for attempt in range(1, 5):
        try:
            ftp = connect()
            with open(LOCAL_FILE, 'rb') as fh:
                ftp.storbinary('STOR ' + REMOTE_PATH, fh)
            ftp.quit()
            print('uploaded ->', REMOTE_PATH)
            return
        except ftplib.all_errors as e:
            print(f'retry {attempt}/4 ({e})')
            time.sleep(3)
    raise RuntimeError('failed to upload ' + REMOTE_PATH)


if __name__ == '__main__':
    main()
