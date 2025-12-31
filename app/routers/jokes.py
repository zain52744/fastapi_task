from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter(prefix="/jokes", tags=["Jokes"])

@router.get("/random")
async def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="External API failed")

        data = response.json()

        return {
            "setup": data["setup"],
            "punchline": data["punchline"]
        }

    except httpx.RequestError:
        raise HTTPException(status_code=500, detail="Unable to reach joke service")
