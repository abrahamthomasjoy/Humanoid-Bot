import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import os

class TTSNode(Node):
    def __init__(self):
        super().__init__('tts_node')
        self.subscription = self.create_subscription(String, 'system/response', self.callback, 10)
        self.get_logger().info('TTS Node (espeak) has started.')

    def callback(self, msg):
        text = msg.data
        self.get_logger().info(f'Speaking: "{text}"')
        os.system(f'espeak "{text}"')

def main(args=None):
    rclpy.init(args=args)
    node = TTSNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
