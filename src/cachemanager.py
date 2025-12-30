#!/usr/bin/env python3
"""
CacheManager - In-memory caching system with TTL support.
"""

from datetime import datetime, timedelta
from typing import Any, Optional

class CacheManager:
    """In-memory cache with TTL."""
    def __init__(self, default_ttl: int = 3600):
        self.cache = {}
        self.default_ttl = default_ttl
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Set cache value with optional TTL."""
        ttl = ttl or self.default_ttl
        expires_at = datetime.now() + timedelta(seconds=ttl)
        self.cache[key] = {
            "value": value,
            "expires_at": expires_at
        }
    
    def get(self, key: str) -> Optional[Any]:
        """Get cache value if not expired."""
        if key not in self.cache:
            return None
        
        item = self.cache[key]
        if datetime.now() > item["expires_at"]:
            del self.cache[key]
            return None
        
        return item["value"]
    
    def delete(self, key: str) -> bool:
        """Delete cache entry."""
        if key in self.cache:
            del self.cache[key]
            return True
        return False
    
    def clear(self) -> None:
        """Clear all cache."""
        self.cache.clear()

if __name__ == "__main__":
    cache = CacheManager(default_ttl=60)
    cache.set("test", "value")
    print(cache.get("test"))
