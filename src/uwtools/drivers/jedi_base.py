"""
A base class for jedi-based drivers.
"""

from abc import abstractmethod
from pathlib import Path

from iotaa import asset, task, tasks

from uwtools.config.formats.yaml import YAMLConfig
from uwtools.drivers.driver import DriverCycleBased
from uwtools.utils.tasks import file, filecopy, symlink


class JEDIBase(DriverCycleBased):
    """
    A base class for the JEDI-like drivers.
    """

    # Workflow tasks

    @task
    def configuration_file(self):
        """
        The executable's YAML configuration file.
        """
        fn = self._config_fn
        yield self._taskname(fn)
        path = self._rundir / fn
        yield asset(path, path.is_file)
        base_file = self._driver_config["configuration_file"].get("base_file")
        yield file(Path(base_file)) if base_file else None
        self._create_user_updated_config(
            config_class=YAMLConfig,
            config_values=self._driver_config["configuration_file"],
            path=path,
        )

    @tasks
    def files_copied(self):
        """
        Files copied for run.
        """
        yield self._taskname("files copied")
        yield [
            filecopy(src=Path(src), dst=self._rundir / dst)
            for dst, src in self._driver_config.get("files_to_copy", {}).items()
        ]

    @tasks
    def files_linked(self):
        """
        Files linked for run.
        """
        yield self._taskname("files linked")
        yield [
            symlink(target=Path(target), linkname=self._rundir / linkname)
            for linkname, target in self._driver_config.get("files_to_link", {}).items()
        ]

    @tasks
    @abstractmethod
    def provisioned_rundir(self):
        """
        Run directory provisioned with all required content.
        """

    # Private helper methods

    @property
    @abstractmethod
    def _config_fn(self) -> str:
        """
        Returns the name of the config file used in execution.
        """
