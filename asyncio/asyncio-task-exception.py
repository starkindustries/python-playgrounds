import sys
import asyncio
import aiohttp


async def get(url):
    try:
        print('GET %s' % url)
        resp = await aiohttp.request('GET', url)
    except Exception as e:
        raise Exception("%s has error '%s'" % (url, e))
    else:
        if resp.status >= 400:
            raise Exception("ERROR get(): %s has error '%s: %s'" % (url, resp.status, resp.reason))

    return await resp.text()

async def fill_data(run):
    url = 'http://www.google.com/%s' % run['name']
    run['data'] = await get(url)

# def get_runs():
#     runs = [ {'name': 'one'}, {'name': 'two'} ]
#     loop = asyncio.get_event_loop()
#     task = asyncio.wait([fill_data(r) for r in runs])
#     loop.run_until_complete(task)   
#     return runs

def get_runs():
    runs = [ {'name': 'one'}, {'name': 'two'} ]
    loop = asyncio.get_event_loop()
    tasks = asyncio.gather(*[fill_data(r) for r in runs])
    loop.run_until_complete(tasks)
    return runs

try:
    get_runs()
except Exception as e:
    print("ERROR:", repr(e))
    sys.exit(1)