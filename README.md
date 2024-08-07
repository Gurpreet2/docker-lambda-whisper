# docker-lambda-whisper
Contains sample collection of files to get started with a local instance of whisper that can also be deployed as an AWS lambda function (lambda hosted version not yet tested).

This project is mainly about experimenting with making it into a local API.

## Prereqs

1. Docker Desktop (if building locally)
1. Python 3.10 or 3.11
1. AWS Lambda Rie
    1. Download from https://github.com/aws/aws-lambda-runtime-interface-emulator/releases
    1. Simply download the latest version named "aws-lambda-rie" (at the time of writing this, latest was 1.21)
    1. Place the downloaded file in the docker/ directory
    1. Alternatively, you can modify the Dockerfile to use an aws lambda base image, but ffmpeg is also inhumanly difficult to get working on RHEL-based images
1. Git Bash is preferred (on windows, otherwise you may need to modify the commands a bit to work in cmd or powershell)
1. Your favorite IDE that can work with python notebooks (VSCode is recommended)
1. A GPU, preferrably minimum of 4GB

## Getting Started

1. Initialize a virtual environment, activate it, and install dependencies

    ```bash
    python -m venv .venv

    source .venv/Scripts/activate

    pip install -r requirements-local.txt
    ```

1. Start up the container

    ```bash
    docker compose up
    ```

1. Open the whisper.ipynb file, and run each cell, start to finish. Voila, it should convert the speech to text. You can start experimenting from here!

## FAQ

1. I'm having some trouble, any additional docs?

    https://github.com/openai/whisper/discussions/1463

1. I modified function.py, but the container isn't picking up the updates!

    Remember to tear down the old container with the old file first, simply run
    ```bash
    docker compose down && docker compose up --build
    ```
    It'll tear the old container down and start up a new one with the updates

1. Why make a dockerized version of whisper?

    Because for the love of god I almost became a broken man trying to get ffmpeg to work with whisper and its dependencies on windows. It can work with pydub/pyaudio, but it has some sort of vendetta against whisper on windows.

## Comments

Please note that some parts of this project were developed with the assistance of Github Copilot and ChatGPT.
