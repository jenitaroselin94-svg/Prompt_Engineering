# Qwen Prompting Techniques

## Project Overview

Qwen Prompting Techniques is an AI-based web application built using Streamlit and the Qwen Large Language Model (LLM). It allows users to explore different prompting techniques and generate responses for their tasks.

The application demonstrates how different prompt structures can influence AI-generated responses.

## Objectives

* To understand different prompt engineering techniques.
* To generate responses using the Qwen LLM.
* To compare different prompting approaches.
* To provide a simple and interactive user interface.

## Prompting Techniques

1. **Zero-shot Prompting:** Generates an answer without providing examples.
2. **One-shot Prompting:** Uses one example to guide the response.
3. **Few-shot Prompting:** Provides multiple examples to guide the model.
4. **Chain of Thought (CoT):** Encourages a structured approach to solving tasks.
5. **Manual CoT:** Uses predefined steps to organize the solution.
6. **Tree of Thoughts (ToT):** Encourages consideration of multiple possible approaches.
7. **ReAct:** Combines reasoning and action-oriented steps to approach a task.

## Technologies Used

* Python
* Streamlit
* Hugging Face Hub
* Qwen2.5-72B-Instruct
* python-dotenv

## Project Structure

```text
prompt Engineering/
│
├── app.py
├── llm.py
├── prompt_templates.py
├── .env
└── README.md
```

## Installation

Install the required Python packages:

```bash
pip install streamlit huggingface_hub python-dotenv
```

## Configuration

Create a `.env` file in the project directory and add your Hugging Face access token:

```text
HF_TOKEN=your_hugging_face_token
```

Keep the `.env` file private. Do not upload your token to GitHub or share it publicly.

## Run the Application

Open the terminal in the project directory and execute:

```bash
streamlit run app.py
```

The application opens in your web browser.

## How to Use

1. Open the application.
2. Select a prompting technique.
3. Enter a task or question.
4. Adjust the temperature and maximum token settings.
5. Click the Generate Answer button.
6. View the generated prompt and AI response.

## Key Features

* Interactive Streamlit interface.
* Seven prompting techniques.
* Customizable temperature and maximum tokens.
* Displays the generated prompt.
* Generates responses using the Qwen model.
* Error handling for missing tokens and API failures.

## Future Enhancements

* Compare outputs from multiple prompting techniques.
* Add response history.
* Integrate external tools for ReAct.
* Support additional language models.
* Improve response evaluation and visualization.

## Conclusion

Qwen Prompting Techniques provides a practical way to learn and experiment with prompt engineering. It demonstrates how structured prompts can help guide language models to produce useful responses for different tasks.

## Author

Developed as an educational project to explore Large Language Models and Prompt Engineering.
