# YouTube Video to GIF Converter

[GifCreator](https://github.com/Dheovani/GifCreator/assets/79609196/715488e5-b329-4190-b067-5a4dc7533ba0)

## Description

This is a simple Python script that allows you to convert YouTube videos into animated GIFs. It uses the PyTube library to download YouTube videos, extracts frames from the video, and then creates a GIF from those frames. The script also includes improvements to ensure that frames are processed and organized correctly.

## Prerequisites

Before using this script, make sure you have the following Python libraries installed:

- [PyTube](https://python-pytube.readthedocs.io/en/latest/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)

You can install them using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. Run the youtube_to_gif.py script:

```bash
python youtube_to_gif.py
```

3. Follow the prompts to enter the video URL, the directory to save videos, the directory to save frames, and the GIF name.

4. The generated GIF will be saved in the specified directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.
