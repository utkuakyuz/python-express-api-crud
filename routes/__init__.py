"""
Routes paketi

Bu paket, API endpoint'lerini içerir.
"""

from .patients import router as patients_router

__all__ = ["patients_router"] 