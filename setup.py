from distutils.core import setup

INSTALL_REQUIRES = ['numpy', 'matplotlib']
TRAINING_REQUIRES = ['keras']

# TODO: fix extras require with keras

setup(
    name='bj_bot',
    version='0.1dev',
    packages=['black_jack'],
    requires=INSTALL_REQUIRES
)
