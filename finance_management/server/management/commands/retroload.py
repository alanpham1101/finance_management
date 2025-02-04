import os
import importlib.util

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "Applies retroload files"

    def add_arguments(self, parser):
        parser.add_argument(
            '-a', '--app', action='store', dest='app', default='server',
            help="Use this to specify app name for retroloads file(s)."
        )

    def handle(self, **options):
        app_name = options.get('app')
        retroloads_dir = os.path.join(settings.BASE_DIR, app_name, "retroloads")
        applied_files_log = os.path.join(retroloads_dir, ".applied_files.log")

        if not os.path.exists(retroloads_dir):
            self.stdout.write(self.style.ERROR(f"Directory {retroloads_dir} does not exist!"))
            return

        applied_files = set()
        if os.path.exists(applied_files_log):
            with open(applied_files_log, "r") as log_file:
                applied_files = set(log_file.read().splitlines())

        all_files = set([
            file for file in os.listdir(retroloads_dir)
            if file.endswith(".py") and file != '__init__.py'
        ])
        unapplied_files = sorted(all_files - applied_files)
        if not unapplied_files:
            self.stdout.write(self.style.SUCCESS("No retroload file to run!"))
            return

        for unapplied_file in unapplied_files:
            file_path = os.path.join(retroloads_dir, unapplied_file)
            self.stdout.write(self.style.NOTICE(f"Applying {unapplied_file}..."))

            try:
                spec = importlib.util.spec_from_file_location("retro_script", file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                with open(applied_files_log, "a") as log_file:
                    log_file.write(unapplied_file + "\n")

                self.stdout.write(self.style.SUCCESS(f"Successfully applied {unapplied_file}"))
            except Exception:
                self.stdout.write(self.style.ERROR(f"Error applying {unapplied_file}"))
