class IncludeAPIRouter:
    def __new__(cls):
        from fastapi import APIRouter

        from src.blueprints.apis import address_router

        router = APIRouter()
        router.include_router(address_router, prefix="/api/v1")
        return router
