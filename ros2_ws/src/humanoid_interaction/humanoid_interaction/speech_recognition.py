import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import vosk
import sounddevice as sd
import queue
import json
import numpy as np
from scipy.signal import resample

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(f"Audio input status: {status}")
    try:
        q.put(bytes(indata))
    except Exception as e:
        print(f"Error adding audio data to queue: {e}")

class SpeechRecognizer(Node):
    def __init__(self):
        super().__init__('speech_recognition')
        self.publisher_ = self.create_publisher(String, 'speech/detected', 10)
        self.get_logger().info('Speech Recognizer Node started.')
        self.hw_samplerate = 48000
        self.target_samplerate = 16000
        model = vosk.Model(lang='en-us')
        self.rec = vosk.KaldiRecognizer(model, self.target_samplerate)
        self.stream = sd.RawInputStream(samplerate=self.hw_samplerate, dtype='int16', channels=1, device=0, callback=callback)
        self.stream.start()
        self.timer = self.create_timer(0.5, self.process_audio)

    def process_audio(self):
        while not q.empty():
            audio = q.get()
            samples = np.frombuffer(audio, dtype=np.int16)
            if self.hw_samplerate != self.target_samplerate:
                num = int(len(samples) * self.target_samplerate / self.hw_samplerate)
                samples = resample(samples, num).astype(np.int16)
            if self.rec.AcceptWaveform(samples.tobytes()):
                text = json.loads(self.rec.Result()).get('text', '')
                if text:
                    self.get_logger().info(f"Speech recognized: '{text}'")
                    self.publisher_.publish(String(data=text))

def main(args=None):
    rclpy.init(args=args)
    node = SpeechRecognizer()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
