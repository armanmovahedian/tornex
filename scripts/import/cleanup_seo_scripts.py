"""Deletes the one-off SEO fix/diagnostic scripts from the WP root now that
the fix has been applied and verified."""
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

REMOTE_FILES = [
    'public_html/tornex-fix-category-seo.php',
    'public_html/tornex-seo-diag.php',
]


def connect():
    ftp = ftplib.FTP()
    ftp.connect(env['DEPLOY_HOST'], int(env.get('DEPLOY_PORT', 21)), timeout=25)
    ftp.login(env['DEPLOY_USER'], env['DEPLOY_PASSWORD'])
    return ftp


def main():
    ftp = connect()
    for remote_path in REMOTE_FILES:
        for attempt in range(1, 4):
            try:
                ftp.delete(remote_path)
                print('deleted ->', remote_path)
                break
            except ftplib.all_errors as e:
                print(f'retry {attempt}/3 for {remote_path} ({e})')
                time.sleep(2)
                try:
                    ftp = connect()
                except Exception:
                    pass
    ftp.quit()


if __name__ == '__main__':
    main()
