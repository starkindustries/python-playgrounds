from aiohttp import web

async def handle_request(request):
    if not is_authenticated(request):
        # Generate a redirect response with status code 302 and the Location header set to the redirect URL
        headers = {"Location": "https://example.com/"}
        return web.Response(status=302, headers=headers)
    return web.Response(text="Hello, world!")

def is_authenticated(request):
    # implement your authentication logic here
    return False # return True if authenticated, False otherwise

if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.get('/', handle_request)])
    web.run_app(app)
