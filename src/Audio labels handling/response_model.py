from dataclasses import dataclass
from typing import List, Any
from dataclass_wizard import JSONWizard, json_field


@dataclass
class Value:
    start: float
    end: float
    channel: int
    labels: List[str]

@dataclass
class Data:
    audio: str

@dataclass
class Result:
    original_length: float
    value: Value
    id: str
    from_name: str
    to_name: str
    type_: str = json_field('type', all=True)
    origin: str

@dataclass
class Annotation:
    id: int
    completed_by: int
    result: List[Result]
    was_cancelled: bool
    ground_truth: bool
    created_at: str
    updated_at: str
    draft_created_at: str
    lead_time: float
    prediction: str
    result_count: int
    unique_id: str
    import_id: str
    last_action: str
    task: int
    project: int
    updated_by: int
    parent_prediction: str
    parent_annotation: str
    last_created_by: str

@dataclass
class Response(JSONWizard):

    class _(JSONWizard.Meta):
        key_transform_with_dump = 'LISP'

    id: int
    annotations: List[Annotation]
    file_upload: str
    drafts: list
    predictions: list
    data: Data
    meta: dict
    created_at: str
    updated_at: str
    inner_id: int
    total_annotations: int
    cancelled_annotations: int
    total_predictions: int
    comment_count: int
    unresolved_comment_count: int
    last_comment_updated_at: Any
    project: int
    updated_by: int
    comment_authors: list