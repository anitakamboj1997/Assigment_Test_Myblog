# your_app/management/commands/add_tags.py

import json
from django.core.management.base import BaseCommand
from blog.models import PostTags

class Command(BaseCommand):
    help = 'Adds predefined tags from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file containing tags')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as f:
                tags = json.load(f)
                for tag_data in tags:
                    tag_name = tag_data.get('name')
                    PostTags.objects.get_or_create(name=tag_name)
            self.stdout.write(self.style.SUCCESS('Tags added successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
