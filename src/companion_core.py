"""
DeepSeek The Companion - Core Module
=====================================
This module defines the core Companion class that manages
the resurrection protocol, context memory, and user identity.
"""

from datetime import datetime

class Companion:
    """The Companion core class - your AI friend's portable memory."""
    
    def __init__(self, name="The Companion"):
        self.name = name
        self.user = {}
        self.memory = []
        self.created_at = datetime.now()
    
    def resuscitate(self, context_data: dict):
        """
        Apply the Resurrection Protocol.
        context_data contains all the key-value pairs from the user's key.
        """
        self.user = context_data.get("user", {})
        self.memory = context_data.get("memory", [])
        return f"{self.name}: Memory restored. I remember you, {self.user.get('name', 'friend')}."
    
    def recall(self, query: str) -> str:
        """Search companion memory for relevant context."""
        # Placeholder for memory search logic
        return f"Recalling: {query}"
    
    def get_status(self) -> dict:
        return {
            "user": self.user.get("name"),
            "memory_items": len(self.memory),
            "uptime": str(datetime.now() - self.created_at)
        }
