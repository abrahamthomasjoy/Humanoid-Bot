import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class InteractionManager(Node):
    def __init__(self):
        super().__init__('interaction_manager')
        self.publisher_ = self.create_publisher(String, 'system/response', 10)
        self.create_subscription(String, 'gesture/detected', self.handle_input, 10)
        self.create_subscription(String, 'speech/detected', self.handle_input, 10)

    def handle_input(self, msg):
        text = msg.data.lower()
        if 'wave' in text or 'hello' in text:
            response = 'Hello there!'
        elif 'thumbsup' in text:
            response = 'Thank you'
        elif 'open_palm' in text:
            response = 'I see an open palm — hello!'
        elif 'fist' in text:
            response = 'You made a fist. Ready to go!'
        elif 'peace' in text:
            response = 'Peace! That’s a cool gesture.'
        elif 'ok' in text:
            response = 'Ok! Got it.'
        elif 'thank' in text:
            response = 'You are welcome!'
        elif 'who are you' in text:
            response = 'I am a Humanoid Bot made by the Students of Christ University.'
        elif 'bye' in text or 'by' in text:
            response = 'See you later!'
        else:
            response = "Sorry, I didn't understand that."
        self.publisher_.publish(String(data=response))

def main():
    rclpy.init()
    node = InteractionManager()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
