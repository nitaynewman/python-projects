import speech_recognition as sr
import pyttsx3
from langchain_ollama import OllamaLLM

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak2Text(command):
    engine.say(command)
    engine.runAndWait()

# Initialize Ollama with the phi3 model
llm = OllamaLLM(model="phi3")

# Initialize the speech recognizer
r = sr.Recognizer()

# Function to capture voice input
def record_text():
    with sr.Microphone() as src2:
        print('Listening...')
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(src2, duration=0.5)

        # Set pause threshold to detect pauses
        r.pause_threshold = 0.8  # Lower values detect shorter pauses

        try:
            # Set timeout to 5 seconds after silence and limit total phrase time to 10 seconds
            audio2 = r.listen(src2, timeout=1, phrase_time_limit=10)
            
            MyText = r.recognize_google(audio2)
            print(f'You said: {MyText}')
            return MyText
        except sr.UnknownValueError:
            print('Sorry, I did not catch that.')
            return None
        except sr.RequestError as e:
            print(f'Could not request results: {e}')
            return None
        except sr.WaitTimeoutError:
            print('Listening timed out while waiting for speech.')
            return None



# Function to send input to the Ollama phi3 model and get a response
def send_to_ollama(msg):
    prompt = "\n".join([f"{message['role']}: {message['content']}" for message in msg])
    response = llm(prompt)  # Direct interaction with the local Ollama model
    return response

# Main assistant loop
def main():
    msg = []  # To store conversation history
    print("Starting the assistant. Say 'stop' to exit.")
    
    while True:
        # Listen for user command
        text = record_text()
        if text is None:
            continue

        if "stop" in text.lower():
            print("Goodbye!")
            speak2Text("Goodbye!")
            break

        # Append user input to conversation history
        msg.append({'role': 'user', 'content': text})

        # Send the input to the Ollama phi3 model and get a response
        response = send_to_ollama(msg)
        print(f"AI says: {response}")

        # Append the AI's response to the conversation history
        msg.append({'role': 'assistant', 'content': response})

        # Speak the AI's response
        speak2Text(response)

if __name__ == "__main__":
    main()
