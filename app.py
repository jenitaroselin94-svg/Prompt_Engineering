import streamlit as st
from llm import generate_response
from prompt_templates import build_prompt
st.set_page_config(
    page_title="Qwen Prompt Engineering",
    page_icon="🔮",
    layout="centered"
)
st.title("🔮 Qwen Prompt Engineering")
st.write(
    "Choose a prompting technique, enter your task, "
    "and generate an answer using the Qwen LLM."
)
technique = st.selectbox(
    "Choose Prompting Technique",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT",
        "ReAct"
    ]
)
task = st.text_area(
    "Enter your task:",
    placeholder="Example: Explain AI and Machine Learning."
)
temperature = st.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.3,
    step=0.1
)
max_tokens = st.slider(
    "Maximum Tokens",
    min_value=100,
    max_value=1000,
    value=500,
    step=100
)
if st.button("Generate Answer"):
    if not task.strip():
        st.warning("Please enter a task.")
    else:
        try:
            final_prompt = build_prompt(technique, task)
            st.subheader("Generated Prompt")
            st.code(final_prompt, language="text")
            with st.spinner("Generating answer using Qwen..."):
                answer = generate_response(
                    final_prompt,
                    temperature,
                    max_tokens
                )
            st.subheader("Generated Answer")
            st.write(answer)
        except Exception as e:
            st.error(f"Unable to generate answer: {e}")

