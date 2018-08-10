from distutils.core import setup

INSTALL_REQUIRES = ['numpy', 'keras', 'keras-rl']

setup(
    name='bj_bot',
    version='0.1dev',
    packages=['black_jack'],
    requires=INSTALL_REQUIRES
)
