from griptape.drivers.prompt.anthropic import AnthropicPromptDriver
from griptape.tasks import PromptTask

task = PromptTask(prompt_driver=AnthropicPromptDriver(model="anthropic.claude-3-7"))

task.run("Hello there!")
