import chainlit as cl
from chainlit.input_widget import Slider, Select


@cl.on_chat_start
async def on_chat_start():

    cl.user_session.set("message_count", 0)
    cl.user_session.set("user_name", None)
    cl.user_session.set("temperature", 0.5)

    settings = cl.ChatSettings(
        [
            Slider(
                id="temperature",
                label="Simulation Temperature",
                min=0.0,
                max=1.0,
                step=0.1,
                initial=0.5,
                description="Adjust the 'temperature' for response variation (higher = more random)."
            ),
            Select(
                id="response_style",
                label="Response Style",
                values=["Echo", "Uppercase", "Reversed"],
                initial_index=0,
                description="Choose how responses are formatted."
            )
        ]
    )
    await settings.send()


    elements = [
        cl.Text(name="welcome_text", content="This is a sample text element.", display="inline"),
        cl.Image(name="sample_image", path="image.png", display="side"),  
    ]
    actions = [
        cl.Action(name="greet_button", label="Greet Me", payload={"action": "greet"}),
        cl.Action(name="count_button", label="Show Count", payload={"action": "count"})
    ]
    init_msg = cl.Message(content="Welcome to the Chainlit demo! Click a button or send a message.", elements=elements, actions=actions)
    await init_msg.send()


    res = await cl.AskUserMessage(content="What is your name? (Timeout: 30s)", timeout=30).send()
    if res:
        user_output = res.get("output")
        cl.user_session.set("user_name", user_output)
        await cl.Message(content=f"Nice to meet you, {user_output}!").send()
    else:
        await cl.Message(content="No name provided, proceeding anonymously.").send()


@cl.on_settings_update
async def on_settings_update(settings):
    cl.user_session.set("temperature", settings["temperature"])
    cl.user_session.set("response_style", settings["response_style"])
    await cl.Message(content="Settings updated! Try sending a message to see the effect.").send()


@cl.on_message
async def on_message(message: cl.Message):
    prev_count = cl.user_session.get("message_count")
    if prev_count is None:
        prev_count = 0
    count = prev_count + 1
    cl.user_session.set("message_count", count)
    user_name = cl.user_session.get("user_name") or "User"
    temp = cl.user_session.get("temperature")
    style = cl.user_session.get("response_style")


    if temp is None:
        temp = 0.5


    response_content = message.content
    if style == "Uppercase":
        response_content = response_content.upper()
    elif style == "Reversed":
        response_content = response_content[::-1]


    prefix = "Response: " if temp < 0.5 else "Randomized Response: " * int(temp * 5)

   
    stream_msg = cl.Message(content="")
    tokens = (prefix + response_content).split()
    for token in tokens:
        await stream_msg.stream_token(token + " ")
    await stream_msg.send()

    # Demonstrate updating a message
    update_msg = cl.Message(content=f"{user_name}, this is message #{count}.")
    await update_msg.send()
    await cl.sleep(2)  # Simulate delay
    update_msg.content = f"Updated: {user_name}, this is now edited message #{count}."
    await update_msg.update()

    # Demonstrate removing a message (after a delay)
    remove_msg = cl.Message(content="This message will be removed in 3 seconds.")
    await remove_msg.send()
    await cl.sleep(3)
    await remove_msg.remove()

# Handle action callbacks
@cl.action_callback("greet_button")
async def on_greet(action: cl.Action):
    user_name = cl.user_session.get("user_name") or "User"
    await cl.Message(content=f"Hello, {user_name}! Action executed.").send()
    await action.remove()  # Remove the button after click

@cl.action_callback("count_button")
async def on_count(action: cl.Action):
    count = cl.user_session.get("message_count")
    await cl.Message(content=f"Current message count: {count}").send()
    await action.remove()