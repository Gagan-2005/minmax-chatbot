# 🤖 MiniMax Chatbot

A simple conversational AI chatbot built using [Streamlit](https://streamlit.io/) and the [MiniMaxAI model](https://huggingface.co/MiniMaxAI/MiniMax-M1-80k) via Hugging Face Inference API.

---

## 🧠 Features

- Real-time chat interface (user vs bot)
- Styled UI with colored message bubbles
- Uses Hugging Face `InferenceClient` with MiniMax M1 model
- Chat history retained during the session

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Hugging Face Hub
- dotenv

---

## 🚀 Getting Started

### 1. **Clone the Repository**

```bash
git clone https://github.com/Gagan-2005/minmax-chatbot.git
cd minmax-chatbot

2. (Optional) Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux
3. Install Requirements
bash
Copy
Edit
pip install -r requirement.txt
4. 🔐 Create a .env File
Create a file named .env in the root folder of your project and paste your Hugging Face token like this:

ini
Copy
Edit
HF_TOKEN=your_huggingface_api_token_here
⚠️ Never share your real token or push .env to GitHub. It is ignored using .gitignore.

If you're collaborating, you can use .env.example as a template.

5. Run the App
bash
Copy
Edit
streamlit run app.py
Open your browser to http://localhost:8501 to start chatting!
