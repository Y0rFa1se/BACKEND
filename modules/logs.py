def log(module, content):
    with open(f"web/fastapi/logs/{module}.log", "a") as f:
        f.write(content)