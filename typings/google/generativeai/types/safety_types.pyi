"""
This type stub file was generated by pyright.
"""

import proto
from collections.abc import Mapping
from typing import Dict, Iterable, List, Union
from typing_extensions import TypedDict
from google.generativeai import protos

"""
This type stub file was generated by pyright.
"""
__all__ = ["HarmCategory", "HarmProbability", "HarmBlockThreshold", "BlockedReason", "ContentFilterDict", "SafetyRatingDict", "SafetySettingDict", "SafetyFeedbackDict"]
HarmProbability = protos.SafetyRating.HarmProbability
HarmBlockThreshold = protos.SafetySetting.HarmBlockThreshold
BlockedReason = protos.ContentFilter.BlockedReason
class HarmCategory(proto.Enum):
    """
    Harm Categories supported by the gemini-family model
    """
    HARM_CATEGORY_UNSPECIFIED = ...
    HARM_CATEGORY_HARASSMENT = ...
    HARM_CATEGORY_HATE_SPEECH = ...
    HARM_CATEGORY_SEXUALLY_EXPLICIT = ...
    HARM_CATEGORY_DANGEROUS_CONTENT = ...


HarmCategoryOptions = Union[str, int, HarmCategory]
_HARM_CATEGORIES: Dict[HarmCategoryOptions, protos.HarmCategory] = ...
def to_harm_category(x: HarmCategoryOptions) -> protos.HarmCategory:
    ...

HarmBlockThresholdOptions = Union[str, int, HarmBlockThreshold]
_BLOCK_THRESHOLDS: Dict[HarmBlockThresholdOptions, HarmBlockThreshold] = ...
def to_block_threshold(x: HarmBlockThresholdOptions) -> HarmBlockThreshold:
    ...

class ContentFilterDict(TypedDict):
    reason: BlockedReason
    message: str
    __doc__ = ...


def convert_filters_to_enums(filters: Iterable[dict]) -> List[ContentFilterDict]:
    ...

class SafetyRatingDict(TypedDict):
    category: protos.HarmCategory
    probability: HarmProbability
    __doc__ = ...


def convert_rating_to_enum(rating: dict) -> SafetyRatingDict:
    ...

def convert_ratings_to_enum(ratings: Iterable[dict]) -> List[SafetyRatingDict]:
    ...

class SafetySettingDict(TypedDict):
    category: protos.HarmCategory
    threshold: HarmBlockThreshold
    __doc__ = ...


class LooseSafetySettingDict(TypedDict):
    category: HarmCategoryOptions
    threshold: HarmBlockThresholdOptions
    ...


EasySafetySetting = Mapping[HarmCategoryOptions, HarmBlockThresholdOptions]
EasySafetySettingDict = dict[HarmCategoryOptions, HarmBlockThresholdOptions]
SafetySettingOptions = Union[HarmBlockThresholdOptions, EasySafetySetting, Iterable[LooseSafetySettingDict], None]
def to_easy_safety_dict(settings: SafetySettingOptions) -> EasySafetySettingDict:
    ...

def normalize_safety_settings(settings: SafetySettingOptions) -> list[SafetySettingDict] | None:
    ...

def convert_setting_to_enum(setting: dict) -> SafetySettingDict:
    ...

class SafetyFeedbackDict(TypedDict):
    rating: SafetyRatingDict
    setting: SafetySettingDict
    __doc__ = ...


def convert_safety_feedback_to_enums(safety_feedback: Iterable[dict]) -> List[SafetyFeedbackDict]:
    ...

def convert_candidate_enums(candidates):
    ...

