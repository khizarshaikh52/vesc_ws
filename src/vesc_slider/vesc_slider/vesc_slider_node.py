import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import tkinter as tk

class VESCSlider(Node):
    def __init__(self):
        super().__init__('vesc_slider')
        self.publisher_ = self.create_publisher(Float64, '/commands/motor/duty_cycle', 10)

        self.root = tk.Tk()
        self.root.title("VESC Throttle Control")

        self.slider = tk.Scale(
            self.root,
            from_=-100,
            to=100,
            orient='horizontal',
            length=400,
            label='Throttle (%)',
            command=self.publish_throttle
        )
        self.slider.pack(padx=20, pady=20)

    def publish_throttle(self, value):
        duty = float(value) / 100.0   # scale to -1.0 ... +1.0
        msg = Float64()
        msg.data = duty
        self.publisher_.publish(msg)
        self.get_logger().info(f"Throttle: {duty:.2f}")

    def run(self):
        while rclpy.ok():
            self.root.update_idletasks()
            self.root.update()

def main(args=None):
    rclpy.init(args=args)
    node = VESCSlider()
    node.run()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
