from japronto import Application

app = Application()


def hello(request):
    return request.Response(json={"text": "Hello python!"})


def hello_query(request):
    ids = request.query.get("id")
    return request.Response(json={"text": f"Hello python, {ids}!"})


app.router.add_route("/", hello)
app.router.add_route("/query", hello_query)


if __name__ == "__main__":
    app.run()
