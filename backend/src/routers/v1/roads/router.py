from collections.abc import Sequence

from fastapi import APIRouter

from src.repositories.cruds.road_crud import RoadCRUD
from src.repositories.mongo_context import MongoDatabaseContext
from src.schemas.road import AddRoadRequest, GetGeometriesResponse

router = APIRouter()

@router.post('/road')
async def add_road_info(road_info: AddRoadRequest | Sequence[AddRoadRequest]):
    """Эндпоинт добавления информации о дороге"""
    db_context = MongoDatabaseContext[RoadCRUD]()
    db_context.crud = RoadCRUD(collection=db_context.db['roads'])
    if isinstance(road_info, AddRoadRequest):
        await db_context.crud.add_object(road_info)
    else:
        await db_context.crud.add_objects(road_info)

@router.get('/get-geometries')
async def get_geometries() -> Sequence[GetGeometriesResponse]:
    """Эндпоинт для получения информации о объектах"""
    db_context = MongoDatabaseContext[RoadCRUD]()
    db_context.crud = RoadCRUD(collection=db_context.db['roads'])
    return await db_context.crud.get_geometries(out_schema=GetGeometriesResponse)
