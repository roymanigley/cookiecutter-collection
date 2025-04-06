import os


model_related_templates = [
    'apps/core/models/__cookiecutter__.py',
    'apps/core/serializers/__cookiecutter__.py',
    'apps/core/views/__cookiecutter__.py',
]

for path in model_related_templates:
    content = ''
    file_path = None
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith('### NEEDLE: '):
                file_path = line.replace('### NEEDLE: ', '').strip()
                with open(file_path, 'w') as f:
                    f.write(content)
                content = ''
            else:
                content += line
    os.remove(path)
