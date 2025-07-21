import yaml
import json
from agents.evaluator_agent import EvaluatorAgent

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

agent = EvaluatorAgent("EvaluatorAgent", config)

# Sample thread + summary
thread_text = """OP: I recently switched from Android to iPhone and I’m loving the camera and battery life.
User1: Same here. iOS feels smoother, but I do miss some Android customizations.
User2: Try using Shortcuts and widgets — helps bridge the gap.
User3: Android still wins in flexibility, but iPhone nails hardware + ecosystem.
User4: Battery life on iPhone 13 is insane. Pixel drains like crazy."""

summary = """- iPhones have better battery life and camera quality than most Android phones.
- iOS is smoother, but some users miss Android's customization.
- Using Shortcuts and widgets can help ease the transition.
- While Android is more flexible, iPhone provides better integration.
- iPhone 13 specifically has standout battery performance."""

result = agent.run(summary, thread_text)

print("\n📊 Evaluation Output:\n")
print(result)
