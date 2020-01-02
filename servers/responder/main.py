import responder

api = responder.API()


@api.route("/")
async def hello_world(req, resp):
    resp.media = {"text": "hello world!"}


@api.route("/query")
async def hello_world_query(req, resp, *args, **kwargs):
    ids = req.params.get("id")
    resp.media = {"text": f"hello world, {ids}!"}


if __name__ == "__main__":
    api.run(debug=False, access_log=False)
