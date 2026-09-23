# AI Tone Rewriter

Rewrite any text in a chosen tone using a large language model. Paste your text, pick a tone, drag the creativity dial, and get an instantly reworded version.

**Live demo:** 'https://ai-tone-rewriter-52.streamlit.app/'

---

## What it does

- Rewrites text in one of four tones: **Professional, Friendly, Concise, Persuasive**
- A **creativity slider** controls the model's `temperature` (0 = focused and consistent, 1 = more varied and creative)
- Bring-your-own-key: runs on your own OpenAI key, and nothing is stored

## How it works

Built on the standard LLM-app pattern — collect input, send a prompt to the model, show the response:

1. **Input** — a text box, a tone dropdown, and a temperature slider
2. **Prompt** — the app builds an instruction from your text and chosen tone
3. **Model call** — sends the prompt with `.invoke()` and reads the reply from the response message's `.content`
4. **Output** — displays the rewritten text

## Tech stack

- Python
- Streamlit — UI and hosting
- LangChain (`langchain-openai`)
- OpenAI API

## Run it locally

```bash
git clone https://github.com/your-username/ai-tone-rewriter.git
cd ai-tone-rewriter
pip install -r requirements.txt
streamlit run rewriter.py
```

Then paste your OpenAI API key into the sidebar.

## Notes

This is a **bring-your-own-key** demo — enter your own OpenAI API key in the sidebar to use the live app. No keys are collected or stored anywhere.

---

_Built by Aliasgar Dohadwala as a hands-on applied-AI project — my first end-to-end LLM app, from build to deployment._
