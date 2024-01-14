from dataclasses import dataclass
from typing import List
from dataclass_wizard import JSONWizard, json_field

@dataclass
class Sono:
    small: str
    med: str
    large: str
    full: str

@dataclass
class Osci:
    small: str
    med: str
    large: str

@dataclass
class Recording:
    id: int
    gen: str
    sp: str
    ssp: str
    group: str
    en: str
    rec: str
    cnt: str
    loc: str
    lat: str
    lng: str
    alt: str
    type_: str = json_field('type', all=True)
    sex: str
    stage: str
    method: str
    url: str
    file: str
    file_name: str
    sono: Sono
    osci: Osci
    lic: str
    q: str
    length: str
    time: str
    date_: str = json_field('date', all=True) 
    uploaded: str
    also: List[str]
    rmk: str
    bird_seen: str
    animal_seen: str
    playback_used: str
    temp: str
    regnr: str
    auto: str
    dvc: str
    mic: str
    smp: int

@dataclass
class Response(JSONWizard):

    class _(JSONWizard.Meta):
        key_transform_with_dump = 'LISP'

    numRecordings: int
    numSpecies: int
    page: int
    numPages: int
    recordings: List[Recording]