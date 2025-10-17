import rclpy
import rclpy.node
import std_msgs.msg


class MinimalPublisher(rclpy.node.Node):
    def __init__(self):
        super().__init__("minimal_publisher")
        self.publisher_ = self.create_publisher(std_msgs.msg.String, "topic", 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        self.publisher_.publish(std_msgs.msg.String(data=f"Hello, world! {self.i}"))
        self.get_logger().info(f'Publishing: "Hello, world! {self.i}"')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()
