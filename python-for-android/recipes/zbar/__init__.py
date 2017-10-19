import os
from pythonforandroid.recipe import PythonRecipe


class ZBarRecipe(PythonRecipe):

    version = '0.10'

    # For some reason the version 0.10 on PyPI is not the same as the ones
    # in sourceforge and GitHub. The one in PyPI has a setup.py.
    # url = 'https://github.com/ZBar/ZBar/archive/{version}.zip'
    url = 'https://pypi.python.org/packages/e0/5c/' + \
        'bd2a96a9f2adacffceb4482cdd56831735ab5a67ea6a60c0a8757c17b62e' + \
        '/zbar-{version}.tar.gz'

    call_hostpython_via_targetpython = False

    depends = ['hostpython2', 'python2', 'setuptools', 'libzbar']

    def get_recipe_env(self, arch=None, with_flags_in_cc=True):
        env = super(ZBarRecipe, self).get_recipe_env(arch, with_flags_in_cc)
        libzbar = self.get_recipe('libzbar', self.ctx)
        libzbar_dir = libzbar.get_build_dir(arch.arch)
        env['PYTHON_ROOT'] = self.ctx.get_python_install_dir()
        env['CFLAGS'] += ' -I' + os.path.join(libzbar_dir, 'include')
        env['CFLAGS'] += ' -I' + env['PYTHON_ROOT'] + '/include/python2.7'
        # TODO
        env['LDSHARED'] = env['CC'] + \
            ' -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions'
        # TODO: hardcoded Python version
        env['LDFLAGS'] += " -landroid -lpython2.7 -lzbar"
        return env


recipe = ZBarRecipe()
