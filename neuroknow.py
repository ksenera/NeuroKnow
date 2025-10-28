# neuroknow.py

from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
from enum import Enum
import numpy as np
from datetime import datetime
import json

class LearningModality(Enum):
    VISUAL = "visual"
    KINESTHETIC = "kinesthetic" 
    AUDITORY = "auditory"
    LOGICAL = "logical"

class ErrorType(Enum):
    CONCEPTUAL_GAP = "conceptual_gap"
    PROCEDURAL_ERROR = "procedural_error" 
    ATTENTION_LAPSE = "attention_lapse"
    TRANSFER_FAILURE = "transfer_failure"

@dataclass
class CognitiveProfile:
    """each students unique learning type"""
    user_id: str
    attention_pattern: str  # 'sprinter', 'marathon', 'cyclical'
    abstraction_preference: str  # 'concrete_first', 'abstract_first'
    modality_strengths: Dict[LearningModality, float]  # 0-1 scores
    error_recovery_speed: float  # How quickly they learn from mistakes
    transfer_capacity: float  # Ability to apply learning across contexts