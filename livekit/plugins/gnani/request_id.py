"""Request ID generation for Gnani API correlation."""

from __future__ import annotations

import uuid


def _generate_request_id() -> str:
    """Generate a unique request ID for outbound Gnani API calls."""
    return f"lk_req_{uuid.uuid4().hex[:12]}"
