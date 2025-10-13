from retico_core.debug import DebugModule
from retico_core.audio import MicrophoneModule, SpeakerModule
from retico_googleasr import GoogleASRModule
from retico_huggingfacelm import HuggingfaceLM
from retico_speechbraintts import SpeechBrainTTSModule
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer


device = "cuda" if torch.cuda.is_available() else "cpu"

checkpoint = "HuggingFaceTB/SmolLM2-135M-Instruct"
tokenizer = AutoTokenizer.from_pretrained(checkpoint, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True).to(device)
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

debug = DebugModule(print_payload_only=True)
mic = MicrophoneModule()
asr = GoogleASRModule(rate=16_000)
lm = HuggingfaceLM(device, tokenizer, model, streamer)
tts = SpeechBrainTTSModule("en")
speaker = SpeakerModule(rate=22050)

mic.subscribe(asr)
asr.subscribe(lm)
lm.subscribe(tts)
lm.subscribe(debug)
tts.subscribe(speaker)

mic.run()
asr.run()
lm.run()
tts.run()
speaker.run()
debug.run()

input()

mic.stop()
asr.stop()
lm.stop()
tts.stop()
speaker.stop()
debug.stop()
