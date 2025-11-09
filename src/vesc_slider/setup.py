from setuptools import find_packages, setup

package_name = 'vesc_slider'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
  ('share/ament_index/resource_index/packages', ['resource/vesc_slider']),
    ('share/vesc_slider', ['package.xml']),
    ('share/vesc_slider/launch', ['launch/vesc_slider.launch.py']),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chrono',
    maintainer_email='chrono@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
 'vesc_slider = vesc_slider.vesc_slider_node:main',
        ],
    },
)
