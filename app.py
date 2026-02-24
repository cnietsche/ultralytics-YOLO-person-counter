import sys
import cv2
from ultralytics import YOLO


def count_people(image_path):
    model = YOLO("yolov8n.pt")  # Modelo leve

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Não foi possível carregar a imagem.")

    results = model(image)

    person_count = 0

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            # Classe 0 = person (COCO dataset)
            if class_id == 0 and confidence > 0.5:
                person_count += 1

    return person_count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python app.py imagem.png")
        sys.exit(1)

    image_path = sys.argv[1]

    total = count_people(image_path)
    print(total)