import time

from services.backup_service import BackupService


def main() -> None:
    BackupService().make_backup()


while True:
    main()
    time.sleep(24 * 60 * 60)
