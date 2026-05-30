# Prompt Engineering CLI

Take the prompt-tool starter from today's lesson and extend it with a **new** use case that you'd actually use day to day.

The shipped `prompt_tool.py` already has three use cases wired up: code review, concept explanation, and debug helper.  Your job is to add at least one more and to apply the techniques from the lesson when you do.

## Setup

```bash
python3 -m venv venv && source venv/bin/activate
# No third-party deps yet — Day 3 adds an OpenAI/Anthropic client.
python prompt_tool.py
```

`call_llm()` is intentionally a stub that just prints the engineered prompt.  Wednesday's lesson (`week16/day3` — AI API Integration) is where you swap it out for a real API call.

## Requirements

### 1. Pick a use case that isn't already in the tool

Pick something you'd actually use day-to-day.  A few ideas (don't use code review, explain, or debug — those are the built-in three):

- **Test generator** — give it a function, get back unit tests
- **Commit-message writer** — paste a diff, get a Conventional Commit message
- **API endpoint designer** — describe a resource, get a REST endpoint spec
- **SQL helper** — describe what you want, get a query (specify the schema!)
- **Email rewriter** — paste a draft, get a more professional/concise/friendlier version
- **Code translator** — paste code in one language, get an equivalent in another
- **Regex builder** — describe a pattern in plain English, get a regex with test strings

### 2. Apply at least 3 prompt engineering techniques

From the lesson, you have:
- System prompt that sets the role and constraints
- Few-shot prompting (input → output examples)
- Chain-of-thought ("think through this step by step")
- Structured output (require JSON / specific format)
- Delimiters separating instructions from data
- Specificity (word counts, exact field names, output shape)

Use at least three and pick deliberately — not every technique fits every use case.

### 3. Wire it into the CLI menu

Add your new use case as option `4` in `main()`, with whatever `input(...)` prompts it needs.  Make sure it follows the same shape as the existing three (build the messages array, then call `call_llm(messages)`).

### 4. Compare a poorly-written prompt to your engineered one

Pick **one** of your prompts and write a second, deliberately bad version of it.  Run both and paste the engineered output into a `comparison.md` file in your repo with a short paragraph on what changed and why.

## Things to think about

- Which of the lesson's techniques actually moved the needle for *your* use case, and which felt like overhead?
- The lesson's `build_explain_prompt` takes `skill_level` as a free-form string and pastes it into the prompt unchecked.  What could go wrong?  How would you validate it?
- Where would a few-shot example come from in a production setting?  Hard-coded?  Pulled from a database?  Generated?
- When you switch from this stub to a real API call on Wednesday, what edge cases will you need to handle that don't exist today (timeouts, rate limits, partial JSON…)?

## Stretch

- Read the use case + inputs from a YAML/JSON config file instead of `input(...)`.  Easier to iterate on prompts that way.
- Add a `--dry-run` flag that just prints the prompt (current behavior) and a `--live` flag that you'll wire up to a real API on Wednesday.
- Write 2–3 sample inputs per use case and pin them as fixtures.  When you change a prompt, re-run all fixtures and diff the outputs.
- Add **bias-mitigation** instructions to one of your system prompts (the lesson's "LLM Limitations" section mentions this).  Did the output change?

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!
