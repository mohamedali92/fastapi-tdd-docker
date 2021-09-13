from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from typing import Optional, List


async def post(paylaod: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=paylaod.url,
        summary="dummy summary"
    )

    await summary.save()
    return summary.id


async def get(id: int) -> Optional[dict]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    return None


async def get_all() -> List[TextSummary]:
    summaries = await TextSummary.all().values()
    return summaries
