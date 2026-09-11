from setuptools import find_packages, setup

package_name = 'humanoid_interaction'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'vosk', 'sounddevice', 'numpy', 'scipy'],
    zip_safe=True,
    maintainer='Humanoid Robot Project',
    maintainer_email='noreply@example.com',
    description='Speech recognition, dialogue management, and TTS nodes for the humanoid robot.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'speech_recognition = humanoid_interaction.speech_recognition:main',
            'interaction_manager = humanoid_interaction.interaction_manager:main',
            'tts_node = humanoid_interaction.tts_node:main',
        ],
    },
)
