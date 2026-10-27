from setuptools import setup
from setuptools.command.build_py import build_py


class PackageBuildPy(build_py):
    package_modules = {
        "geOrchestra": {"__init__", "geOrchestra"},
        "geOrchestra.console": {"__init__", "console"},
        "geOrchestra.meta_apis": {
            "__init__",
            "gn_api",
            "meta_manipulation",
            "metadata",
        },
    }

    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        allowed = self.package_modules.get(package, set())
        return [module for module in modules if module[1] in allowed]


setup(cmdclass={"build_py": PackageBuildPy})