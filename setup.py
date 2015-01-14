from setuptools import setup
setup(
    name='encoded_commands',
    version='0.3',
    description='',
    packages=['encoded_commands'],
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [console_scripts]
        check-files = encoded_commands.check_files:main
        update-file-status = encoded_commands.update_file_status:main
        ''',
)
