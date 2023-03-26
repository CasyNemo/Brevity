from setuptools import setup, find_packages

setup(
    name='your-app-name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'certifi==2022.12.7',
        'charset-normalizer==3.1.0',
        'click==8.1.3',
        'filelock==3.10.0',
        'Flask==2.2.3',
        'gunicorn==20.1.0',
        'huggingface-hub==0.13.2',
        'idna==3.4',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.2',
        'mpmath==1.3.0',
        'networkx==3.0',
        'numpy==1.24.2',
        'packaging==23.0',
        'Pillow==9.4.0',
        'PyYAML==6.0',
        'regex==2022.10.31',
        'requests==2.28.2',
        'sympy==1.11.1',
        'tokenizers==0.13.2',
        'torch==2.0.0',
        'torchvision==0.15.1',
        'tqdm==4.65.0',
        'transformers==4.27.1',
        'typing_extensions==4.5.0',
        'urllib3==1.26.15',
        'Werkzeug==2.2.3',
    ],
)