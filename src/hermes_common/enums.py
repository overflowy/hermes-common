from enum import StrEnum, auto


class UnitType(StrEnum):
    INFANT = auto()
    CHILD = auto()
    YOUTH = auto()
    ADULT = auto()


class DataExtractionMode(StrEnum):
    DISABLED = auto()
    DEFAULT = auto()
    DEFAULT_WITH_ID = auto()
