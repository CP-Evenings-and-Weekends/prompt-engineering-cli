"""Prompt Engineering CLI — starter from the week16/day2 lesson.

Three built-in use cases (code review, concept explanation, debug helper)
are wired up. Your job is to add at least one more — pick something you'd
actually use day to day and apply the techniques from the lesson.

call_llm() is intentionally a no-op stub that just prints the engineered
prompt. On Thursday (week16/day3) you'll replace it with a real API call.
"""


def call_llm(messages):
    """
    Placeholder for an actual LLM API call.
    Replace this with a real API call on Day 3.
    For now, it just prints the engineered prompt so you can see
    what would be sent to the model.
    """
    print("\n--- Engineered Prompt (what would be sent to the LLM) ---\n")
    for msg in messages:
        role = msg["role"].upper()
        print(f"[{role}]")
        print(msg["content"])
        print()
    print("--- End of Prompt ---")
    print("\n(Replace call_llm() with a real API call to see actual responses.)\n")


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


def build_api_designer_prompt(resource, fields, operations):
    """Build a prompt for designing REST API endpoints."""
    messages = [
        {
            "role": "system",
            "content": (
                "You are an API designer specializing in RESTful APIs. "
                "Design clear and conventional endpoints using standard HTTP methods."
            )
        },
        {
            "role": "user",
            "content": f"""Design REST API endpoints for the resource below.

Use this exact format for each endpoint:

Method:
Path:
Purpose:

Example:

Resource: Student
Fields: name, email
Operations: CRUD

Output:
Method: GET
Path: /api/students/
Purpose: Return all students

Method: POST
Path: /api/students/
Purpose: Create a new student

### RESOURCE START ###
Resource: {resource}
Fields: {fields}
Operations: {operations}
### RESOURCE END ###

Only return the endpoint specification."""
        }
    ]
    return messages

def build_bad_api_prompt(resource):
    """A deliberately poorly written prompt for comparison."""
    messages = [
        {
            "role": "user",
            "content": f"Make API endpoints for {resource}."
        }
    ]
    return messages

def main():
    print("=== Prompt Engineering CLI Tool ===\n")
    print("Choose a use case:")
    print("1. Code Review")
    print("2. Concept Explanation")
    print("3. Debug Helper")
    print("4. API Endpoint Designer")

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
        resource = input("\nWhat resource are you designing an API for? ").strip()
        fields = input("What fields does the resource have? ").strip()
        operations = input("What operations do you need (e.g. CRUD)? ").strip()
        messages = build_api_designer_prompt(resource, fields, operations)
        call_llm(messages)

    else:
        print("Invalid choice.")

    

if __name__ == "__main__":
    main()
