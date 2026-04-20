from __future__ import annotations

import os
from contextlib import nullcontext
from typing import Any

try:
    from langfuse import get_client, observe, propagate_attributes
except Exception:  # pragma: no cover
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    def get_client() -> Any:
        class _DummyClient:
            def update_current_generation(self, **kwargs: Any) -> None:
                return None
        return _DummyClient()

    def propagate_attributes(**kwargs: Any):
        return nullcontext()


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))
