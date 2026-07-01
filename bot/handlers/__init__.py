from aiogram import Router

from .start import router as start_router
from .booking import router as booking_router
from .schedule import router as schedule_router
from .subjects import router  as subjects_router
from .admin import router as admin_router

router = Router()

router.include_router(start_router)
router.include_router(booking_router)
router.include_router(schedule_router)
router.include_router(subjects_router)
router.include_router(admin_router)
