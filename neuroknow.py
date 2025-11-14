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

    def get_optimal_modality_mix(self) -> List[LearningModality]:
        """Returns modalities sorted by strength"""
        return sorted(self.modality_strengths.keys(), 
                     key=lambda m: self.modality_strengths[m], reverse=True)
    

@dataclass 
class LearningState:
    """Current snapshot of student's progress"""
    mastered_concepts: List[str]
    active_struggles: List[str]
    cognitive_load: float  # 0-1 scale
    engagement_level: float  # 0-1 scale
    recent_errors: List['ErrorLog']
    
    def get_primary_struggle(self) -> Optional[str]:
        return self.active_struggles[0] if self.active_struggles else None
    
@dataclass
class ErrorLog:
    """Detailed error tracking for metacognition"""
    timestamp: datetime
    concept: str
    error_type: ErrorType
    student_approach: str


class CognitiveFingerprinter:
    """Figures out how this specific brain works"""
    
    def __init__(self):
        self.profiles: Dict[str, CognitiveProfile] = {}
    
    def analyze_initial_interaction(self, user_id: str, diagnostic_data: Dict) -> CognitiveProfile:
        """Creates initial cognitive profile from diagnostic"""
        profile = CognitiveProfile(
            user_id=user_id,
            attention_pattern=self._assess_attention_pattern(diagnostic_data),
            abstraction_preference=self._assess_abstraction_pref(diagnostic_data),
            modality_strengths=self._assess_modality_strengths(diagnostic_data),
            error_recovery_speed=0.5,  
            transfer_capacity=0.5   
        )
        self.profiles[user_id] = profile
        return profile
    
    def update_from_errors(self, user_id: str, error_logs: List[ErrorLog]):
        """Refines profile based on actual learning data"""
        profile = self.profiles[user_id]

        # error recovery speed based on pattern
        recovery_data = self._analyze_error_recovery(error_logs)
        profile.error_recovery_speed = recovery_data['recovery_speed']

        # update learning mod effectiveness based on error log data 
        success_patterns = self._extract_success_patterns(error_logs)
        for modality, effectiveness in success_patterns.items():
            profile.modality_strengths[modality] = effectiveness

    def assess_attention_pattern(self, data: Dict) -> str:
        focus_durations = data.get('focus_durations', [])
        avg_focus = np.mean(focus_durations) if focus_durations else 25
        if avg_focus < 15: return 'sprinter'
        elif avg_focus > 40: return 'marathon' 
        else: return 'cyclical'

    def assess_modality_strengths(self, data: Dict) -> Dict[LearningModality, float]:
        # something here to use diagnostic results 
        return {
            LearningModality.VISUAL: 0.8,
            LearningModality.KINESTHETIC: 0.6,
            LearningModality.AUDITORY: 0.4,
            LearningModality.LOGICAL: 0.9
        }

class KnowledgeGraph:
    """Maps concepts and their cognitive relationships"""
    
    def __init__(self):
        self.concepts: Dict[str, Dict] = {
            'fraction_basics': {
            'prerequisites': [],
            'related_concepts': ['fraction_division', 'decimal_conversion'],
            'transfer_domains': ['pizza_slicing', 'music_rhythms', 'sports_statistics'],