import yaml
from agents.summarizer_agent import SummarizerAgent

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

sample_input = """
Reddit user: I recently switched from Android to iPhone and I’m really enjoying the camera and battery life. But I do miss the flexibility of Android and some custom apps.

Comment 1: Same here. iOS is smooth but lacks some niche features.

Comment 2: I use both. Android for customization, iPhone for camera and updates.

Comment 3: Try using shortcuts and widgets to bridge the gap.

Comment 4: Totally agree. The battery on iPhone 13 is insane compared to Pixel.
"""

agent = SummarizerAgent("SummarizerAgent", config)
result = agent.run(sample_input)

print("\n🔍 Summary:\n")
print(result)
