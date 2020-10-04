# Docker task

This project uses a regular docker file. Docker-compose can be added later if needed.

## How to use this image
``cd`` in ``./docker`` directory.

Build image.
```
docker build -t docker_task
```

Run container.
```
docker run docker_task -dp 80:80
```

Open browser at ``http://localhost``.

## Functional

``http://localhost/pic`` - shows a picture.

``http://localhost/hello`` - shows hello_world.html.

``http://localhost/search$SEARCH_REQUEST`` - redirects `SEARCH_REQUEST` to google.com.
