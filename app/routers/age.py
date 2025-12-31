from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter(prefix="/age", tags=["External API"])

@router.get("/predict")
async def predict_age(name: str):
    # basic validation
    if not name:
        raise HTTPException(status_code=400, detail="Name is required")

    url = f"https://api.agify.io/?name={name}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="External API failed")

        data = response.json()

        # clean & structured response
        return {
            "input_name": data.get("name"),
            "predicted_age": data.get("age"),
            "data_source": "agify.io"
        }

    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Unable to reach external API")
