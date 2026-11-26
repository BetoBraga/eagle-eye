"""Run the same CPU inference and rendering path as the Streamlit app."""

from pathlib import Path
import argparse
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import cv2
from app import detect_objects, setup_model

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("input", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()

if args.output.resolve() == args.input.resolve():
    parser.error("output must be a different file")
image = cv2.imread(str(args.input))
if image is None:
    parser.error(f"unreadable image: {args.input}")
predictor, metadata = setup_model()
instances = predictor(image)["instances"].to("cpu")
result = detect_objects(image, lambda _image: {"instances": instances}, metadata)
if not cv2.imwrite(str(args.output), result):
    raise SystemExit(f"could not write: {args.output}")

detections = [
    {"class": metadata.thing_classes[i], "score": round(p, 4)}
    for i, p in zip(instances.pred_classes.tolist(), instances.scores.tolist())
]
print(json.dumps({"detections": detections, "output": str(args.output)}))
