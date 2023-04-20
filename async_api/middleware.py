import asyncio
import json
import time

from django.http import JsonResponse
from django.utils.decorators import sync_and_async_middleware


@sync_and_async_middleware
def timing_middleware(get_response):
    if asyncio.iscoroutinefunction(get_response):
        async def middleware(request):
            start = time.perf_counter()
            response = await get_response(request)
            data = json.loads(response.content)
            data["elapsed"] = time.perf_counter() - start
            return JsonResponse(data)
    else:
        def middleware(request):
            start = time.perf_counter()
            response = get_response(request)
            data = json.loads(response.content)
            data["elapsed"] = time.perf_counter() - start
            return JsonResponse(data)
    return middleware
