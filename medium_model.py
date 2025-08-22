import os
import re
import torch
from flask import Flask, jsonify, request, send_file
from faster_whisper import WhisperModel

# Flask app
app = Flask(__name__)

# TTS file prefix
speech_tts_prefix = "speech-tts-"

# Load transcription model
if torch.cuda.is_available():
    #model = WhisperModel("medium.en", device="cuda", compute_type="float16")
    #model = WhisperModel("large-v2", device="cuda", compute_type="float16")
    model = WhisperModel("medium", device="cuda", compute_type="float16")
else:
    model = WhisperModel("medium", device="auto")

# Clean temporary files (called every 5 minutes)
def clean_tmp():
    tmp_dir = tempfile.gettempdir()
    for file in os.listdir(tmp_dir):
        if file.startswith(speech_tts_prefix):
            os.remove(os.path.join(tmp_dir, file))
    print("[Speech REST API] Temporary files cleaned!")


# Transcribe endpoint
@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'error': 'Invalid input, form-data: audio'}), 400

    # Audio file
    audio_file = request.files['audio']
    
    # Decode the audio
    #segments, info = model.transcribe(audio_file, beam_size=5, language="pl")
    segments, info = model.transcribe(audio_file, beam_size=5)
    
    text_result = ''
    
    for segment in segments:
        text_result = text_result + segment.text
        
    text_result_trim = text_result.strip()
    
    print(text_result_trim)

    return jsonify({
        'language': info.language,
        'text': text_result_trim
    }), 200

# Health endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/clean', methods=['GET'])
def clean():
    clean_tmp()
    return jsonify({'status': 'ok'}), 200

# Entry point
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))

    # Start server
    print("[Speech REST API] Starting server on port " + str(port))

    app.run(host='0.0.0.0', port=3000)

