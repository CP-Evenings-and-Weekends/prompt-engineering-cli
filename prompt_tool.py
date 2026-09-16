from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="unused"
)
"""Prompt Engineering CLI — starter from the week16/day2 lesson.

Three built-in use cases (code review, concept explanation, debug helper)
are wired up. Your job is to add at least one more — pick something you'd
actually use day to day and apply the techniques from the lesson.

call_llm() is intentionally a no-op stub that just prints the engineered
prompt. On Thursday (week16/day3) you'll replace it with a real API call.
"""


# def call_llm(messages):
#     """
#     Placeholder for an actual LLM API call.
#     Replace this with a real API call on Day 3.
#     For now, it just prints the engineered prompt so you can see
#     what would be sent to the model.
#     """
#     print("\n--- Engineered Prompt (what would be sent to the LLM) ---\n")
#     for msg in messages:
#         role = msg["role"].upper()
#         print(f"[{role}]")
#         print(msg["content"])
#         print()
#     print("--- End of Prompt ---")
#     print("\n(Replace call_llm() with a real API call to see actual responses.)\n")

def call_llm(messages):
    """Send the engineered prompt to Ollama and print the response."""
    response = client.chat.completions.create(
        model="qwen3:8b",
        messages=messages
    )

    print("\n--- LLM Response ---\n")
    print(response.choices[0].message.content)
    print()

    
def build_code_review_prompt(code_snippet):
    """Build a prompt for reviewing code using multiple techniques."""
    messages = [
        {
            "role": "system",
            "content": (
                "You are a senior software engineer conducting a code review. "
                "Be constructive and specific. For each issue you find, explain "
                "why it is a problem and provide a corrected code snippet. "
                "Organize your review into sections: Bugs, Style, Performance, Security."
            )
        },
        {
            "role": "user",
            "content": f"""Review the following Python code. Identify any bugs, style issues,
performance concerns, or security vulnerabilities.

For each issue:
1. Quote the problematic line
2. Explain the problem
3. Show the corrected code

If the code looks good in a category, say "No issues found."

###CODE START###
{code_snippet}
###CODE END###

Return your review organized by category."""
        }
    ]
    return messages


def build_explain_prompt(concept, skill_level):
    """Build a prompt for explaining a concept using context and specificity."""
    messages = [
        {
            "role": "system",
            "content": (
                "You are a patient and clear programming instructor at a coding bootcamp. "
                "Your students know Python, JavaScript, and Django. "
                "Use analogies and practical examples. Never assume knowledge beyond "
                "what is specified."
            )
        },
        {
            "role": "user",
            "content": f"""Explain the following concept: {concept}

Student's self-reported comfort level: {skill_level}/5

Instructions:
- If comfort is 1-2, use a simple analogy first, then show basic code
- If comfort is 3, give a clear definition with a practical code example
- If comfort is 4-5, focus on nuances, edge cases, and advanced usage

Keep your explanation under 300 words. End with a "Try it yourself" mini-challenge."""
        }
    ]
    return messages


def build_debug_prompt(error_message, code_context, what_i_tried):
    """Build a prompt for debugging using context and chain-of-thought."""
    messages = [
        {
            "role": "system",
            "content": (
                "You are a debugging assistant. Think through problems step by step. "
                "Always explain the root cause, not just the fix."
            )
        },
        {
            "role": "user",
            "content": f"""I need help debugging an issue.

**Error message:**
{error_message}

**Relevant code:**
```
{code_context}
```

**What I have already tried:**
{what_i_tried}

Please:
1. Think through what could cause this error step by step
2. Identify the most likely root cause
3. Explain WHY this causes the error
4. Provide the fix with corrected code
5. Suggest how to prevent this type of error in the future"""
        }
    ]
    return messages


# Add your own build_<something>_prompt(...) function here.
# email rewrite
def professional_email_rewrite(email_draft):
 
    """Build a prompt for rewriting an email using system prompts, few-shot examples, and structured output."""
    messages = [
        {
            "role": "system",
            "content": (
                "You are a professional email rewriting assistant. "
                "Rewrite the user's email while preserving the original meaning. "
                "Correct grammar and spelling and improve clarity. "
                "Create three versions of the email with different levels of professionalism: "
                "low, medium, and high. "
                "Do not add information that was not included in the original email. "
                "Return the rewritten emails using the exact JSON structure provided."
            )
        },
        {
            "role": "user",
            "content": f"""I need help rewriting an email.

Here are examples showing different levels of professionalism:
Example 1:

Input:
"hey john, i wanted to check if you got my paperwork. let me know thanks"

Low Professional:
{{
    "subject": "Follow-Up on Paperwork",
    "greeting": "Hi John,",
    "body": "Just wanted to check if you got my paperwork. Let me know when you can. Thanks!",
    "closing": "Thanks,"
}}

Medium Professional:
{{
    "subject": "Follow-Up on Paperwork",
    "greeting": "Hi John,",
    "body": "I wanted to follow up and see if you received my paperwork. Please let me know when you have a chance.",
    "closing": "Thank you,"
}}

High Professional:
{{
    "subject": "Follow-Up on Paperwork",
    "greeting": "Dear John,",
    "body": "I am following up to confirm whether you have received my paperwork. Please let me know at your convenience.",
    "closing": "Best regards,"
}}


Example 2:

Input:
"Hi, I can't come to the meeting tomorrow because something came up. Can we do it another day?"

Low Professional:
{{
    "subject": "Meeting",
    "greeting": "Hi,",
    "body": "I can't make the meeting tomorrow because something came up. Can we reschedule?",
    "closing": "Thanks,"
}}

Medium Professional:
{{
    "subject": "Request to Reschedule Meeting",
    "greeting": "Hi,",
    "body": "Unfortunately, I am no longer available for tomorrow's meeting due to an unexpected conflict. Would it be possible to reschedule for another day?",
    "closing": "Best,"
}}

High Professional:
{{
    "subject": "Request to Reschedule Meeting",
    "greeting": "Dear [Name],",
    "body": "Unfortunately, I am unable to attend tomorrow's scheduled meeting due to an unexpected conflict. Would it be possible to arrange an alternative meeting time that is convenient for you?",
    "closing": "Best regards,"
}}


Now rewrite the following email and provide all three levels of professionalism:
<email>
{email_draft}
</email>

Return ONLY valid JSON using exactly these fields:
{{
    "low_professional": {{
        "subject": "",
        "greeting": "",
        "body": "",
        "closing": ""
    }},
    "medium_professional": {{
        "subject": "",
        "greeting": "",
        "body": "",
        "closing": ""
    }},
    "high_professional": {{
        "subject": "",
        "greeting": "",
        "body": "",
        "closing": ""
    }}
}}
"""
        }
    ]

    return messages

# System Prompt → tells the AI its role and rules
# Few-Shot Prompting → shows examples of low/medium/high professionalism
# Structured Output → forces the predictable JSON structure
# Delimiters → <email>...</email> clearly separates the user's data

def main():
    print("=== Prompt Engineering CLI Tool ===\n")
    print("Choose a use case:")
    print("1. Code Review")
    print("2. Concept Explanation")
    print("3. Debug Helper")
    print("4. Email Rewriter")

    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
        print("\nPaste your code (type 'END' on a new line when done):")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        code = "\n".join(lines)
        messages = build_code_review_prompt(code)
        call_llm(messages)

    elif choice == "2":
        concept = input("\nWhat concept do you want explained? ").strip()
        skill_level = input("Your comfort level with this topic (1-5): ").strip()
        messages = build_explain_prompt(concept, skill_level)
        call_llm(messages)

    elif choice == "3":
        error = input("\nPaste the error message: ").strip()
        print("Paste the relevant code (type 'END' on a new line when done):")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        code = "\n".join(lines)
        tried = input("What have you already tried? ").strip()
        messages = build_debug_prompt(error, code, tried)
        call_llm(messages)


    elif choice == "4":
        print("\nPaste your email (type 'END' on a new line when done):")
        lines = []

        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)

        email_draft = "\n".join(lines)

        messages = professional_email_rewrite(email_draft)
        call_llm(messages)



    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
