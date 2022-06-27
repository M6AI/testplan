"""TODO."""
import traceback
from typing import Dict

from testplan.common.config import Config, Configurable


class ExporterResult:
    def __init__(self, exporter, type):
        self.exporter = exporter
        self.type = type
        self.traceback = None

    @property
    def success(self):
        return not self.traceback

    @classmethod
    def run_exporter(cls, exporter, source, type):
        result = ExporterResult(exporter=exporter, type=type)

        try:
            exporter.export(source)
        except Exception:
            result.traceback = traceback.format_exc()
        return result


class BaseExporterConfig(Config):
    """
    Configuration object for
    :py:class:`BaseExporter <testplan.common.exporters.BaseExporter>` object.
    """

    @classmethod
    def get_options(cls) -> Dict:
        return {"name": str}


class BaseExporter(Configurable):
    """Base exporter class."""

    CONFIG = BaseExporterConfig

    def __init__(self, name=None, **options):
        if name is None:
            name = self.__class__.__name__
        self._cfg = self.CONFIG(name=name, **options)
        super(BaseExporter, self).__init__()

    @property
    def name(self) -> str:
        return self.cfg.name

    @property
    def cfg(self) -> BaseExporterConfig:
        """Exporter configuration."""
        return self._cfg

    def export(self, report) -> None:
        """

        :param report:
        :return:
        """
        raise NotImplementedError("Exporter must define export().")
