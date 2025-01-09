import csv
import shutil
import tempfile
from typing import List

from src.core.models.domains import DomainConfig
from src.core.models.enums import DateFormat, DecimalFormat, Specie
from src.core.models.models import Account, Client, Consumer, File, FilePackage
from src.core.services.storage_service import StorageService
from src.core.services.reader_service import CsvReader, ExcelReader


class FileService:
    def __init__(self, file):
        self.file = file

    def process(
        self,
    ) -> str:  # pragma: no cover
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                consumer, _ = Consumer.objects.get_or_create(
                    name=row['consumer name'],
                    address=row['consumer address'],
                    ssn=row['ssn']
                )

                client, _ = Client.objects.get_or_create(
                    reference=row['client reference no']
                )
                Account.objects.create(
                    client=client,
                    consumer=consumer,
                    balance=row['balance'],
                    status=row['status']
                )

        return "success"
