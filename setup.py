from setuptools import setup


setup(
    name='Hashmal',
    version = '0.1',
    description='Bitcoin transaction script IDE.',
    install_requires=[
        'python-bitcoinlib'
    ],
    author='Tyler Willis, mazaclub',
    author_email='kefkius@maza.club',
    keywords=[
        'bitcoin',
        'transaction'
    ],
    scripts=['hashmal'],
    py_modules=[
        'hashmal_lib.__init__',
        'hashmal_lib.dock_handler',
        'hashmal_lib.gui_utils',
        'hashmal_lib.help_widgets',
        'hashmal_lib.main_window',
        'hashmal_lib.scriptedit',
        'hashmal_lib.settings_dialog',
        'hashmal_lib.core.__init__',
        'hashmal_lib.core.script',
        'hashmal_lib.core.stack',
        'hashmal_lib.core.utils',
        'hashmal_lib.docks.__init__',
        'hashmal_lib.docks.addr_encoder',
        'hashmal_lib.docks.base',
        'hashmal_lib.docks.script_gen',
        'hashmal_lib.docks.stack',
        'hashmal_lib.docks.variables'
    ]
)
