
# Sample Chainlit application demonstrating core features (no LLMs involved)

import chainlit as cl
from chainlit.input_widget import Select, Slider, Switch, Tags, TextInput
import asyncio

# on_chat_start is called when a new chat session begins
@cl.on_chat_start
async def on_chat_start():
    # Initialize a counter in session memory to track number of messages
    cl.user_session.set("counter", 0)

    # Send a welcome message with instructions
    await cl.Message(
        content="**Welcome to the Chainlit Demo!** 🎉\n\n"
                "Try the following commands to explore features:\n"
                "- **button**: display an action button and handle callback\n"
                "- **ask user**: ask a question (text input)\n"
                "- **ask action**: prompt for picking an action\n"
                "- **upload file**: ask to upload a file and read it\n"
                "- **file**: show a downloadable file element\n"
                "- **image**, **video**, **audio**: display media elements\n"
                "- **stream**: show streaming response token by token\n"
    ).send()

    # Configure sidebar settings that the user can adjust
    settings = await cl.ChatSettings(
        [
            TextInput(id="AgentName", label="Your Name", initial="User"),
            Select(id="Mode", label="Mode", values=["Basic", "Advanced"], initial_index=0),
            Slider(id="Volume", label="Volume", min=0, max=10, initial=5, step=1),
            Tags(id="Interests", label="Your Interests", initial=["Chatting"], tooltip="Add tags you like"),
            Switch(id="Notifications", label="Enable Notifications", initial=True),
        ]
    ).send()

    # Use the settings to greet the user
    if settings:
        name = settings.get("AgentName", "User")
        mode = settings.get("Mode")
        volume = settings.get("Volume")
        interests = settings.get("Interests")
        notifications = settings.get("Notifications")
        await cl.Message(
            content=f"Nice to meet you, **{name}**! 🎈\n"
                    f"- Mode: {mode}\n"
                    f"- Volume: {volume}\n"
                    f"- Interests: {interests}\n"
                    f"- Notifications Enabled: {notifications}"
        ).send()

    # Ask how to proceed
    await cl.Message(content="How can I assist you today?").send()

# on_message is called whenever the user sends a message
@cl.on_message
async def on_message(message: cl.Message):
    # Update and store the message count in session memory
    counter = cl.user_session.get("counter") or 0
    counter += 1
    cl.user_session.set("counter", counter)

    # Normalize user input to lowercase for command matching
    user_text = message.content.strip().lower()

    if user_text == "button":
        # Send a message with an action button
        actions = [
            cl.Action(name="hello_button", label="Say Hello", icon="hand", payload={"info": "👋"})
        ]
        await cl.Message(
            content="Click the button below to trigger an action:",
            actions=actions
        ).send()

    elif user_text == "ask user":
        # Prompt the user for text input
        res = await cl.AskUserMessage(content="What is your favorite color?").send()
        if res:
            color = res.get("output")
            await cl.Message(content=f"Your favorite color is **{color}**! 🌈").send()

    elif user_text == "ask action":
        # Prompt the user to pick one of the given actions
        actions = [
            cl.Action(name="continue", payload={"value": "continue"}, label="✅ Continue"),
            cl.Action(name="cancel", payload={"value": "cancel"}, label="❌ Cancel")
        ]
        res = await cl.AskActionMessage(content="Pick an option:", actions=actions).send()
        if res and res.get("payload"):
            choice = res["payload"].get("value")
            if choice == "continue":
                await cl.Message(content="You chose to continue. 🎉").send()
            elif choice == "cancel":
                await cl.Message(content="You chose to cancel. ❌").send()

    elif user_text == "upload file":
        # Ask the user to upload a file
        files = await cl.AskFileMessage(content="Please upload a text file.", accept=["text/plain"]).send()
        if files:
            text_file = files[0]
            try:
                with open(text_file.path, "r", encoding="utf-8") as f:
                    content = f.read()
                await cl.Message(
                    content=f"Uploaded **{text_file.name}** with {len(content)} characters! 📄"
                ).send()
            except Exception as e:
                await cl.Message(content=f"Failed to read file: {e}").send()

    elif user_text == "file":
        # Send a message with a downloadable file element
        file_elem = cl.File(
            name="Python.gitignore",
            url="https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
        )
        await cl.Message(content="Here is a file you can download:", elements=[file_elem]).send()

    elif user_text == "image":
        # Send a message with an image element
        image = cl.Image(
            url="https://via.placeholder.com/300.png?text=Chainlit+Image",
            name="demo_image",
            display="inline"
        )
        await cl.Message(content="Here is an image for you:", elements=[image]).send()

    elif user_text == "video":
        # Send a message with a video element
        video = cl.Video(
            name="sample_video.mp4",
            url="https://file-examples.com/wp-content/storage/2017/04/file_example_MP4_480_1_5MG.mp4",
            display="inline"
        )
        await cl.Message(content="Enjoy this video sample:", elements=[video]).send()

    elif user_text == "audio":
        # Send a message with an audio element
        audio = cl.Audio(
            name="sample_audio.mp3",
            url="https://file-examples.com/wp-content/storage/2017/11/file_example_MP3_700KB.mp3",
            display="inline"
        )
        await cl.Message(content="Listen to this audio clip:", elements=[audio]).send()

    elif user_text == "stream":
        # Demonstrate streaming a message token by token
        msg = cl.Message(content="")
        await msg.send()
        for token in ["Streaming ", "text ", "token ", "by ", "token", "."]:
            await asyncio.sleep(0.5)
            await msg.stream_token(token)
        await msg.update()

    else:
        # Default: echo the message and show message count
        await cl.Message(
            content=f"You said: *{message.content}* 💬\n"
                    f"Message count: {counter}"
        ).send()

# Define a callback function for the action button
@cl.action_callback("hello_button")
async def on_action(action: cl.Action):
    info = action.payload.get("info")
    await cl.Message(content=f"Hello! You clicked the button {info}").send()

# on_stop is called when the user stops the current task
@cl.on_stop
def on_stop():
    print("🔴 The user has stopped the task.")  # Logs to the backend console
