import base64
import whisper


model = whisper.load_model("base")


def lambda_handler(event, context):
    audio_data = base64.b64decode(event["audio_data"].encode("utf-8"))

    with open("/tmp/received_audio.mp3", "wb") as audio_file:
        audio_file.write(audio_data)

    result = model.transcribe("/tmp/received_audio.mp3", word_timestamps=True)

    return {"statusCode": 200, "body": result}
