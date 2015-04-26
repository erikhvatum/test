import distutils.core

test = distutils.core.Extension('test._test', sources = ['test/_test.c', 'Source/test.c'], include_dirs = ['Source'])

distutils.core.setup(name = 'test',
        version = '1.0',
        description = 'test package',
        ext_modules = [test],
        packages = ['test'])
