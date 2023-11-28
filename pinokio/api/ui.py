import gradio as gr
from insanely_fast_whisper import transcribe

def transcribe_audio(file):
    # Transcribe the audio file using insanely-fast-whisper
    transcription = transcribe(file.name)
    return transcription

# Define Gradio interface
iface = gr.Interface(
    fn=transcribe_audio, 
    inputs=gr.inputs.Audio(source="upload", type="file"), 
    outputs="text"
)

# Launch the interface
iface.launch()