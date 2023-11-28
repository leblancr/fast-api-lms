import fastapi 

router = fastapi.APIRouter()


@router.get("/sections/{id}")
async def read_section():
    return {"courses": []}


@router.post("/sections/{id}/content-blocks")
async def read_section_content_blocks():
    return {"courses": []}


@router.get("/content-blocks/{id}")
async def get_user(id: int):
    return {"courses": []}
