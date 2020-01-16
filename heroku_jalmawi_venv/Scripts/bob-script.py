#!D:\PyProject\GitRespo\Django_Portfolio\jonathan_almawi_site\heroku_jalmawi_venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bob-builder==0.0.17','console_scripts','bob'
__requires__ = 'bob-builder==0.0.17'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bob-builder==0.0.17', 'console_scripts', 'bob')()
    )
