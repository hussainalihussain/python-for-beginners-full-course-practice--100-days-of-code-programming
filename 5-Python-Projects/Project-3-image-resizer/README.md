# Project 3 - Image Resizer

A small OpenCV project to open, preview and resize images.

## Setup

```bash
pip install opencv-python
```

## Files

| File | What it does |
| --- | --- |
| `open-image.py` | Opens `tree.jpg` and shows it in a preview window. |
| `resize-image.py` | Resizes `tree.jpg` to 70% and saves it as `tree-resized.jpg`. |
| `resize-image-tool.py` | Interactive tool - asks for the image and resizes it the way you choose. |
| `tree.jpg` | Sample image to play with. |

## Run it

```bash
python open-image.py
python resize-image.py
python resize-image-tool.py
```

Press any key while the preview window is focused to close it.

## Using the tool

`resize-image-tool.py` asks for an image path, prints its current size, then offers:

- `1` - just preview the image
- `2` - resize by entering a new width and height
- `21` - resize by a scale percentage (e.g. `50` for half size)

Then it asks for the output file name. Type `r` to overwrite the original image.

```
Path of the image to resize (with extension):
tree.jpg
The current size: 1920x1280

Enter an action (1-2):
21
Scale in percentag (only number):
50
New Resize Image Name (with extension, 'r' to replace):
tree-small.jpg

Resizing to 960x640
```

## Notes

- OpenCV uses `image.shape` as `(height, width, channels)` - so `shape[1]` is the width and `shape[0]` is the height.
- `cv2.imread()` returns `None` if the path is wrong, so double-check the file name and extension.

## Learn more

- [OpenCV Python tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [`cv2.resize()` docs](https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d)
- [OpenCV image basics (read, show, write)](https://docs.opencv.org/4.x/db/deb/tutorial_display_image.html)
- [Pillow - another popular image library](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
