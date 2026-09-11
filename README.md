# Humanoid Robot – Voice & Gesture Interaction System

An educational humanoid robot platform built around an **NVIDIA Jetson Nano**, running **ROS 2 Humble** on Ubuntu, with 3D-printed arm/hand assemblies and LiDAR-based sensing. This repo currently hosts the **interaction stack** — offline speech recognition, a rule-based dialogue manager, and text-to-speech — that lets the robot listen, understand simple commands, and respond out loud.

🏆 **Awarded "Best Project of the Year"** at the 48th KSCST Student Project Programme (SPP), Poster Presentation & Exhibition, JNNCE, Shivamogga — Aug 2025. Supported by DST-GoI, ART-Park (IISc), and Karnataka State Bioenergy Development Board. See [`docs/KSCST_WIN_Certificate.pdf`](docs/KSCST_WIN_Certificate.pdf).

## What it does

- **Speech input:** microphone audio is captured and transcribed offline using [Vosk](https://alphacephei.com/vosk/), with resampling from the mic's native rate to 16kHz for the recognizer.
- **Interaction logic:** a ROS 2 node listens on both speech and gesture topics and maps recognized phrases/gestures (wave, thumbs-up, fist, peace, etc.) to canned responses.
- **Speech output:** responses are spoken aloud via `espeak`.
- **Hardware:** Jetson Nano as the onboard compute; peripherals for actuation and a LiDAR unit for the mobile base; arms and hands are 3D-printed (some parts built by senior students).

```
[ Camera/Mic ] → speech_recognition node → /speech/detected ─┐
[ Gesture cam]  → (gesture node, WIP)     → /gesture/detected ┼→ interaction_manager → /system/response → tts_node → speaker
```

## Repo structure

```
humanoid-robot/
├── ros2_ws/src/humanoid_interaction/   # ROS 2 package (this is the buildable code)
│   ├── humanoid_interaction/
│   │   ├── speech_recognition.py       # Vosk-based STT node
│   │   ├── interaction_manager.py      # command → response logic
│   │   └── tts_node.py                 # espeak-based TTS node
│   ├── package.xml
│   └── setup.py
├── docs/                               # certificate, project report
├── media/                              # photos/demo (add your own)
└── requirements.txt
```

## Setup

Requires Ubuntu 22.04 + ROS 2 Humble already installed on the Jetson (or dev machine).

```bash
sudo apt install espeak
pip install -r requirements.txt --break-system-packages   # or use a venv

# Download a Vosk speech model (small English model is enough for command-style speech)
# from https://alphacephei.com/vosk/models and place it where vosk.Model(lang='en-us')
# can find it, or pass an explicit model path.

cd ros2_ws
colcon build --packages-select humanoid_interaction
source install/setup.bash

ros2 run humanoid_interaction speech_recognition
ros2 run humanoid_interaction interaction_manager
ros2 run humanoid_interaction tts_node
```

## Status / Roadmap

- [x] Offline speech recognition (Vosk)
- [x] Rule-based command → response mapping
- [x] Text-to-speech output
- [ ] Gesture recognition node (camera-based) — publishes to `gesture/detected`
- [ ] Swap rule-based responses for a small LLM/intent classifier
- [ ] LiDAR navigation integration
- [ ] Arm/gripper control nodes

## Team

Built by the humanoid robotics team at CHRIST (Deemed to be University), Kengeri Campus, Bengaluru.

## License

MIT — see [LICENSE](LICENSE).
