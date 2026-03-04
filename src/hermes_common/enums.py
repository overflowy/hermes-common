from enum import StrEnum, auto


class UnitType(StrEnum):
    INFANT = auto()
    CHILD = auto()
    YOUTH = auto()
    ADULT = auto()
    PERSON = auto()


class DataExtractionMode(StrEnum):
    DISABLED = auto()
    COLOSSEUM = auto()
    SEVILLE = auto()


class ParticipantExtractionStatus(StrEnum):
    INCOMPLETE_DATA = auto()
    UNIT_TYPE_MISMATCH = auto()
    OK = auto()
