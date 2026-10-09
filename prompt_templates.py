def build_prompt(technique, task):
    if technique == "Zero-shot":
        return f"""
Answer the given task without examples.

Task:
{task}

Provide a clear and accurate answer.
""".strip()

    if technique == "One-shot":
        return f"""
Follow the style of the example below.

Example:
Task: What is Python?
Answer: Python is a programming language used
for software development and automation.

Now answer this task:
{task}
""".strip()

    if technique == "Few-shot":
        return f"""
Learn from the following examples and answer similarly.

Example 1:
Task: What is AI?
Answer: AI helps computers perform intelligent tasks.

Example 2:
Task: What is ML?
Answer: ML allows computers to learn patterns from data.

Example 3:
Task: What is NLP?
Answer: NLP helps computers understand human language.

Now answer the following task:
{task}
""".strip()

    if technique == "CoT":
        return f"""
Analyze the task carefully and solve it step by step.
Provide a brief explanation of the key steps
and a clear final answer.

Task:
{task}
""".strip()

    if technique == "Manual CoT":
        return f"""
Follow these steps to answer the task.

Step 1: Understand the question.
Step 2: Identify the important information.
Step 3: Apply the appropriate method.
Step 4: Check the result.
Step 5: Give the final answer.

Task:
{task}
""".strip()

    if technique == "ToT":
        return f"""
Explore different possible approaches to solve the task.

Approach A:
Suggest and evaluate the first solution.

Approach B:
Suggest and evaluate another solution.

Approach C:
Consider an alternative solution if useful.

Compare the approaches and choose the most suitable one.
Give a concise explanation and final answer.

Task:
{task}
""".strip()

    if technique == "ReAct":
        return f"""
Use the ReAct (Reasoning and Acting) approach
to solve the task.

Thought:
Identify what the task requires.

Action:
Describe a suitable action or method to solve it.

Observation:
State what information or result would be obtained.
Do not invent observations from tools that were not used.

Final Answer:
Provide the answer based on the available information.

Task:
{task}
""".strip()

    raise ValueError("Unknown prompting technique")
