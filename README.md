# 🧠 AI Assistant for PDFs  
> Ask anything from your PDF — no more scrolling or searching!



## 🚀 What It Does

Tired of manually reading long PDFs?  
This app removes all your hassle.  
✅ Upload your PDF  
✅ Ask questions about it  
✅ Get instant answers — the AI does all the reading for you.

No registration, no setup — just drag, drop, and ask.


## 🛠 Technologies Used

1. **Python**
2. **Streamlit** – for interactive UI
3. **PyPDF2** – to extract text from PDF files
4. **Transformers (Flan-T5)** – for answering questions using AI



## ✅ Best Part

- **No API key required**  
- Runs on a **fully open-source model (Flan-T5)**  
- Completely **free to use** and deploy  
- Can be run locally or on Streamlit Cloud



## ⚙️ How It Works

- The PDF is uploaded by the user
- `PyPDF2` extracts the text from the file (with a page limit for performance)
- The extracted text is passed to a **Flan-T5 transformer model** using Hugging Face pipelines
- When a user asks a question, the AI processes the context + question and returns an answer in real time



## 📦 Future Improvements

- Add support for long documents using chunking + summarization
- Switch to Gemini/GPT APIs for faster responses 
- Add branding, analytics, and multi-file support



## 🧪 Try It Live

👉 [Click here to use the app](https://ai-assistant-pdf-to-text.streamlit.app)  


## 🧑‍💻 Author

Made with ❤️ by [Yash Khetan]  
