import os

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a retroload file"

    def add_arguments(self, parser):
        parser.add_argument(
            '-a', '--app', action='store', dest='app', default='server',
            help="Use this to specify app name for retroloads file(s)."
        )

    def handle(self, **options):
        app_name = options.get('app')
        retroloads_dir = os.path.join(settings.BASE_DIR, app_name, "retroloads")
        if not os.path.exists(retroloads_dir):
            os.makedirs(retroloads_dir)

        counter = 1
        while True:
            file_name = f"{counter:04}.py"
            file_path = os.path.join(retroloads_dir, file_name)

            if not os.path.exists(file_path):
                break

            counter += 1
        with open(file_path, 'w') as f:
            f.write("# This is an empty retroload file created by a custom Django command\n")
        self.stdout.write(self.style.SUCCESS(f"Empty file created: {file_path}"))
