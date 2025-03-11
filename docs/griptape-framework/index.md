Griptape is a python framework for building generative AI applications.
Griptape provides simple, flexible abstractions for working with many areas of genAI, including LLMs, RAG, Evals, and more.

## Why Do I Need a Framework?

You might not! If you're just getting started with generative AI, we encourage you to explore what it's like to build applications from scratch.
As the complexity of your project grows, however, you might find a framework like Griptape helpful for providing structure and best practices.

Griptape tries to be as transparent as possible about the underlying technologies, but having a basic understanding of the underlying technologies can be helpful when building complex applications.

## Quick Start

Generative AI is a broad field, and Griptape is designed to cover a wide range of use cases in this space.
For getting started, we're going to focus on the most common generative AI use case: large language models (LLMs).

### Prerequisites

#### OpenAI API Key

By default, Griptape uses [OpenAi](https://openai.com/) as the underlying model for LLM interactions.
We'll see later how this can be changed through the use of [Prompt Drivers](./drivers/prompt-drivers.md).
For now, grab an [OpenAI API key](https://platform.openai.com/api-keys) and set it as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key"
```

!!! info
    The name Prompt Drivers comes from the act of "prompting" the model with some input.

!!! tip
    Though it is out of scope for this tutorial, you can also check out tools like [python-dotenv](https://pypi.org/project/python-dotenv/) or [mise](https://mise.jdx.dev/environments/) to securely and easily manage your environment variables.

#### Install Griptape

##### Using Uv

[uv](https://docs.astral.sh/uv/) is a dependency manager that makes it easy to install and manage dependencies for your project.
If you're familiar with [poetry](https://python-poetry.org/), `uv` is similar but with a focus on simplicity and speed.

After [installing](https://docs.astral.sh/uv/getting-started/installation/) `uv`, initialize a new project:

```bash
uv init griptape-quickstart
```

Change your working directory to the new `griptape-quickstart` directory created by `uv` and add the the `griptape` dependency:

```bash
uv add griptape
```

`uv` should automatically create [virtual environment](https://docs.astral.sh/uv/pip/environments/#python-environments) to isolate your project's dependencies.
You can "activate" this virtual environment by running:

```bash
source .venv/bin/activate
```

!!! note
    If you use another shell like `fish`, you may need to update this command to match your shell's syntax.

!!! tip
    If you set up `mise` earlier for managing environment variables, you can also use it to [automatically activate](https://mise.jdx.dev/lang/python.html#automatic-virtualenv-activation) your virtual environment.

##### Using Pip

If you don't have access (or don't want to use) `uv`, you can install `griptape` using the more traditional `pip`:

```bash
pip install "griptape" -U
```

## Prompt Task

Now that we're all set up, we can start building with Griptape! One of the most basic building blocks in Griptape is concept of a [Task](./structures/tasks.md).
For getting started, we're going to use the [Prompt Task](./structures/tasks.md#prompt-task) to prompt the LLM with some input.

Create a file called `app.py` and add the following code:

=== "Code"

    ```python
    --8<-- "docs/griptape-framework/src/index_1.py"
    ```

=== "Logs"

    ```text
    --8<-- "docs/griptape-framework/logs/index_1.txt"
    ```

Now run the script like so:
    
```bash
python app.py
```

!!! tip
    Any time you see a "Logs" tab, you can click it to see the output of the example, assuming it produces logs.


If you received a response from the model, congratulations! You've just built your first generative AI application with Griptape.

## Changing Models

!!! info
    This section is a brief aside to show how to change the underlying model implementation.
    The remainder of the tutorial content will continue to use the OpenAI model, so feel free to skip this section if you're not interested in changing the model provider.

Griptape makes it easy to swap out implementations through the use of "Drivers".
Drivers let you change the underlying implementation without needing to change your application code.

Let's adapt our Task to use a different model provider, [Anthropic](https://www.anthropic.com/).
Start by following similar steps to how we set up our OpenAI API key, but this time with an [Anthropic API key](https://console.anthropic.com/settings/keys).

```bash
export ANTHROPIC_API_KEY="your-api-key"
```

Now, import [Anthropic Prompt Driver](/docs/griptape-framework/drivers/prompt-drivers.md#anthropic) and pass it to the Task:

```python
--8<-- "docs/griptape-framework/src/index_2.py"
```

Running the script again, we should get a very similar output as before.
Note that you needed to change no application code to switch between the two models as it was all handled by the Prompt Driver.

The remainder of the tutorial content will use the [Open Ai Chat Prompt Driver](https://docs.griptape.ai/stable/griptape-framework/drivers/prompt-drivers/#openai-chat).
Feel free to use the Anthropic driver if you prefer, just take care to adapt the code accordingly.

```python
--8<-- "docs/griptape-framework/src/index_3.py"
```

## Templating

Griptape uses the popular templating engine, [Jinja](https://jinja.palletsprojects.com/en/stable/), to make it easy to create dynamic prompts.

Let's modify our Task to use a template:

```python
--8<-- "docs/griptape-framework/src/index_4.py"
```

Here, we are referencing `args` with `jinja`'s double curley braces to render the runtime arguments to the template.

!!! info
    `args` is a special attribute that added to the Task's context at runtime.
    Depending on the Task and where it is run, the Task may have access to additional attributes.

For static, key/value data, we can add `context` to the Task:

```python
--8<-- "docs/griptape-framework/src/index_5.py"
```

Using these two methods, you can create dynamic prompts that can be used in a variety of contexts.
Next, let's explore explore getting the LLM to answer how we want it to.


## Rules

## Multimodal Prompt Task

Some LLMs are "multimodal," meaning they can accept both text and image inputs. Let's try downloading an image and prompting the model with it.


## Conversation Memory

## Structured Output

## Tools

## Structures

## Outside this tutorial, Engines Overview and Drivers Overview
## Restructure Navigation
