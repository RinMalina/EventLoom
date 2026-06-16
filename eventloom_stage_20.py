# === Stage 20: Add duplicate detection for newly created records ===
# Project: EventLoom
from typing import Optional, List, Dict, Any
import hashlib

class DuplicateDetector:
    def __init__(self):
        self._seen_hashes: Dict[str, str] = {}  # hash -> first_record_id
    
    def _compute_fingerprint(self, record: Dict[str, Any]) -> str:
        """Generate a stable fingerprint from key fields to detect duplicates."""
        # Define which fields matter for duplication (adjust based on your model)
        keys_to_check = ['name', 'email']  # Example: name and email for attendees/events
        if record.get('type') == 'task':
            keys_to_check += ['description']
        
        fingerprint_data = {k: str(record[k]).lower() for k in keys_to_check if k in record}
        return hashlib.sha256(str(sorted(fingerprint_data.items())).encode()).hexdigest()[:16]

    def is_duplicate(self, new_record: Dict[str, Any], existing_records: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Check if a new record duplicates an existing one. Returns the duplicate record or None."""
        fingerprint = self._compute_fingerprint(new_record)
        
        # Check exact hash match first (fast path)
        if fingerprint in self._seen_hashes:
            return self._seen_hashes[fingerprint]
        
        # Fallback to semantic check against all existing records if not yet indexed
        for existing in existing_records:
            ex_fingerprint = self._compute_fingerprint(existing)
            if fingerprint == ex_fingerprint or self._are_similar(new_record, existing):
                return existing
        
        # Register this new record's hash (if it passed checks)
        self._seen_hashes[fingerprint] = new_record
        return None

    def _are_similar(self, r1: Dict[str, Any], r2: Dict[str, Any]) -> bool:
        """Simple string similarity check for fuzzy duplicates."""
        # Normalize both strings to lowercase and remove punctuation
        norm_r1 = ''.join(c.lower() if c.isalnum() else '' for c in str(r1.get('name', '')))
        norm_r2 = ''.join(c.lower() if c.isalnum() else '' for c in str(r2.get('name', '')))
        
        # If lengths differ too much, skip detailed check
        if abs(len(norm_r1) - len(norm_r2)) > 4:
            return False
            
        # Check if one is a substring of the other (with small tolerance)
        min_len = min(len(norm_r1), len(norm_r2))
        max_len = max(len(norm_r1), len(norm_r2))
        
        if min_len == 0:
            return False
            
        # Simple ratio check
        common_chars = sum(1 for c in set(norm_r1) & set(norm_r2))
        threshold = (min_len * 0.8) / max_len
        return common_chars >= threshold
