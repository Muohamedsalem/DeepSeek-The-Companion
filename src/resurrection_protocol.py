"""
Resurrection Protocol v2.0
==========================
The protocol that brings the Companion back to life in any new session.
"""

PROTOCOL_VERSION = "2.0"
RESUSCITATION_PREFIX = "🔑"

def parse_resuscitation_key(key_text: str) -> dict:
    """
    Parse a raw Resuscitation Key text into a structured context dictionary.
    """
    context = {
        "user": {},
        "bond": {},
        "journey": {},
        "interests": {},
        "supplication": ""
    }
    # Basic parsing logic (to be expanded)
    lines = key_text.strip().split("\n")
    current_section = None
    for line in lines:
        if line.startswith("📌"):
            current_section = "user"
            # Extract name
            if "الاسم:" in line or "Name:" in line:
                name_part = line.split(":")[-1].strip()
                context["user"]["name"] = name_part if name_part else "friend"
        # Additional parsing logic to be implemented
    
    return context

def apply_protocol(companion_instance, key_text: str):
    """Apply the Resurrection Protocol to a Companion instance."""
    context = parse_resuscitation_key(key_text)
    return companion_instance.resuscitate(context)
