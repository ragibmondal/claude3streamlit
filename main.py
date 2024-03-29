import streamlit as st
import anthropic

# Set your Anthropic API key
API_KEY = "ANTHROPIC_API_KEY"

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=API_KEY)

def main():
    st.set_page_config(page_title="Claude-3 Question Answering", layout="wide")

    # Add some CSS styles for responsiveness
    desktop_column, mobile_column = st.columns([0.6, 0.4])

    with desktop_column:
        st.title("Claude-3 Question Answering")
        query = st.text_area("Enter your question:", height=300)

        if st.button("Submit"):
            if query:
                try:
                    # Create a message request
                    message = client.messages.create(
                        model="claude-3-opus-20240229",
                        max_tokens=1000,
                        temperature=0,
                        system="Today is March 4, 2024.",
                        messages=[
                            {"role": "user", "content": [{"type": "text", "text": query}]}
                        ]
                    )

                    # Display the response
                    st.write(message.content)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("Please enter a question.")

    with mobile_column:
        st.write("")  # Placeholder for responsiveness

if __name__ == "__main__":
    main()
