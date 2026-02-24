# ultralytics-YOLO-person-counter
## About the project

This project performs person counting in images using an object detection model.

---

## Prerequisites

- Docker installed
- Git Bash
- Example images directory located at:

---

## Build Docker image

To build the project image, run:

```bash
docker build --no-cache -t person-counter .
```

## Run the container

There are 3 example images available in the project:
- t_0.jpg
- t_1.jpg
- t_2.jpg

To run the processing, execute:

```bash
MSYS_NO_PATHCONV=1 docker run --rm -v /c/Dev/Off-Work/person-counter/resources:/app/resources person-counter '/app/resources/t_2.jpg'
```
