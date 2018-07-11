"""
py2app build script for Electrum XPM
Usage (Mac OS X):
     python setup.py py2app
"""

from setuptools import setup
from plistlib import Plist
import requests
import os
import shutil

from lib.version import ELECTRUM_VERSION as version

CERT_PATH = requests.certs.where()

name = "Electrum XPM"
mainscript = 'electrum-xpm'

plist = Plist.fromFile('Info.plist')
plist.update(dict(CFBundleIconFile='icons/electrum.icns'))


os.environ["REQUESTS_CA_BUNDLE"] = "cacert.pem"
shutil.copy(mainscript, mainscript + '.py')
mainscript += '.py'
extra_options = dict(
    setup_requires=['py2app'],
    app=[mainscript],
    packages=[
        'electrum-xpm',
        'electrum-xpm_gui',
        'electrum-xpm_gui.qt',
        'electrum-xpm_plugins',
        'electrum-xpm_plugins.audio_modem',
        'electrum-xpm_plugins.cosigner_pool',
        'electrum-xpm_plugins.email_requests',
        'electrum-xpm_plugins.greenaddress_instant',
        'electrum-xpm_plugins.hw_wallet',
        'electrum-xpm_plugins.keepkey',
        'electrum-xpm_plugins.labels',
        'electrum-xpm_plugins.ledger',
        'electrum-xpm_plugins.trezor',
        'electrum-xpm_plugins.digitalbitbox',
        'electrum-xpm_plugins.trustedcoin',
        'electrum-xpm_plugins.virtualkeyboard',

    ],
    package_dir={
        'electrum-xpm': 'lib',
        'electrum-xpm_gui': 'gui',
        'electrum-xpm_plugins': 'plugins'
    },
    data_files=[CERT_PATH],
    options=dict(py2app=dict(argv_emulation=False,
                             includes=['sip'],
                             packages=['lib', 'gui', 'plugins'],
                             iconfile='icons/electrum.icns',
                             plist=plist,
                             resources=["icons"])),
)

setup(
    name=name,
    version=version,
    **extra_options
)

# Remove the copied py file
os.remove(mainscript)