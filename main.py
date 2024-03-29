import streamlit as st
import anthropic
from PIL import Image
import io

# Set your Anthropic API key
API_KEY = "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"

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=API_KEY)

def main():
    st.set_page_config(page_title="Claude-3 Question Answering", layout="wide")

    # Add some CSS styles for responsiveness
    desktop_column, mobile_column = st.columns([0.6, 0.4])

    with desktop_column:
        st.title("Claude-3 Question Answering")

        # Chat interface
        chat_container = st.container()
        user_input = st.text_input("Enter your message:", key="user_input")
        upload_image = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])

        if st.button("Send"):
            if user_input or upload_image:
                try:
                    messages = [
                        {"role": "user", "content": [{"type": "text", "text": user_input}]}
                    ]

                    if upload_image:
                        image = Image.open(upload_image)
                        image_bytes = io.BytesIO()
                        image.save(image_bytes, format="PNG")
                        image_bytes = image_bytes.getvalue()
                        messages[0]["content"].append({"type": "image", "data": image_bytes})

                    # Create a message request
                    message = client.messages.create(
                        model="claude-3-opus-20240229",
                        max_tokens=1000,
                        temperature=0,
                        system="Today is March 4, 2024.",
                        messages=messages
                    )

                    # Display the response in the chat
                    chat_container.write(f"**User:** {user_input}")
                    chat_container.write(f"**Claude:** {message.content}")

                    # Clear user input
                    user_input = ""
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("Please enter a message or upload an image.")

    with mobile_column:
        st.write("")  # Placeholder for responsiveness

if __name__ == "__main__":
    main()
