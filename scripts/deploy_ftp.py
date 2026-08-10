import ftplib
import os
import time
import socket

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = {}
with open(os.path.join(ROOT, '.env'), encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        env[k] = v

EXCLUDE_DIRS = {'.git', 'node_modules', '.claude', 'design', 'docs', 'scripts'}
EXCLUDE_FILES = {'.env', '.wp-env.json', 'package.json', 'package-lock.json', 'tornex-prod.sql', '.gitignore', 'CLAUDE.md', 'tornex-theme.zip'}

made_dirs = set()
ftp = None


def connect():
    global ftp
    ftp = ftplib.FTP()
    ftp.connect(env['DEPLOY_HOST'], int(env.get('DEPLOY_PORT', 21)), timeout=25)
    ftp.login(env['DEPLOY_USER'], env['DEPLOY_PASSWORD'])
    ftp.cwd('public_html/wp-content/themes/tornex')


def ensure_remote_dir(rel_dir_posix):
    if not rel_dir_posix or rel_dir_posix in made_dirs:
        return
    parts = rel_dir_posix.split('/')
    cur = ''
    for part in parts:
        cur = cur + '/' + part if cur else part
        if cur in made_dirs:
            continue
        try:
            ftp.mkd(cur)
        except ftplib.error_perm:
            pass
        made_dirs.add(cur)


def upload_file(local_path, remote_path, attempts=4):
    for attempt in range(1, attempts + 1):
        try:
            with open(local_path, 'rb') as fh:
                ftp.storbinary('STOR ' + remote_path, fh)
            return
        except ftplib.all_errors as e:
            print('  retry {}/{} for {} ({})'.format(attempt, attempts, remote_path, e))
            time.sleep(3)
            try:
                connect()
            except Exception as reconnect_err:
                print('  reconnect failed:', reconnect_err)
    raise RuntimeError('failed to upload ' + remote_path + ' after ' + str(attempts) + ' attempts')


connect()

uploaded = 0
for root, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    rel_root = os.path.relpath(root, ROOT)
    rel_root_posix = '' if rel_root == '.' else rel_root.replace(os.sep, '/')

    for f in files:
        if f in EXCLUDE_FILES:
            continue
        local_path = os.path.join(root, f)
        remote_path = f if not rel_root_posix else rel_root_posix + '/' + f

        if rel_root_posix:
            ensure_remote_dir(rel_root_posix)

        upload_file(local_path, remote_path)
        uploaded += 1
        print('uploaded:', remote_path)

print('TOTAL UPLOADED:', uploaded)
ftp.quit()
