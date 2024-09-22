import os
import subprocess

from services.storage_service import StorageService


class BackupService:
    def __init__(self):
        env = os.environ
        self.storage: StorageService = StorageService()
        self.db_host = env.get("PGHOST", "localhost")
        self.db_name = env.get("DBNAME", "postgres")
        self.db_user = env.get("PGUSER", "postgres")
        self.db_password = env.get("PGPASSWORD", "postgres")
        self.db_port = env.get("PGPORT", "5432")
        self.file_name = "dump.dump"

    def __remove_file(self):
        os.remove(self.file_name)

    def make_backup(self) -> None:
        command = [
            "pg_dump",
            "-h", self.db_host,
            "-U", self.db_user,
            "-d", self.db_name,
            "-p", self.db_port,
            "-f", self.file_name
        ]
        try:
            subprocess.run(command, check=True)
            print(f"Dump successfully created: {self.file_name}")
            self.storage.upload_backup()
            self.__remove_file()
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while creating dump: {e}")


