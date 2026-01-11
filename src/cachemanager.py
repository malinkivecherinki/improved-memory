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


"""
Improved Memory - Feature Enhancement
"""

def process_data(data):
    """Process and validate input data"""
    if not data:
        raise ValueError("Data cannot be empty")
    
    processed = []
    for item in data:
        if isinstance(item, dict):
            processed.append(validate_item(item))
        else:
            processed.append(str(item).strip())
    
    return processed

def validate_item(item):
    """Validate individual item structure"""
    required_fields = ['id', 'name']
    for field in required_fields:
        if field not in item:
            raise ValueError(f"Missing required field: {field}")
    return item

class DataProcessor:
    """Main data processing class"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.cache = {}
    
    def process(self, data):
        """Main processing method"""
        cache_key = hash(str(data))
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        result = process_data(data)
        self.cache[cache_key] = result
        return result


"""
Improved Memory - Feature Enhancement
"""

def process_data(data):
    """Process and validate input data"""
    if not data:
        raise ValueError("Data cannot be empty")
    
    processed = []
    for item in data:
        if isinstance(item, dict):
            processed.append(validate_item(item))
        else:
            processed.append(str(item).strip())
    
    return processed

def validate_item(item):
    """Validate individual item structure"""
    required_fields = ['id', 'name']
    for field in required_fields:
        if field not in item:
            raise ValueError(f"Missing required field: {field}")
    return item

class DataProcessor:
    """Main data processing class"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.cache = {}
    
    def process(self, data):
        """Main processing method"""
        cache_key = hash(str(data))
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        result = process_data(data)
        self.cache[cache_key] = result
        return result
