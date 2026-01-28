from textwrap import dedent
from openai import OpenAI

client = OpenAI()  # reads from OPENAI_API_KEY environment variable
MODEL = "gpt-4o-mini"   # swap to which ever model you want to use with your API key - I use this to save $ while testing functionality 


def build_dream_prompt(dream_text: str) -> str:
    return dedent(f"""
    ROLE:
    You are a skilled dream analyst with deep knowledge of archetypal imagery,
    symbolic language, and the psychology of dreams. Your approach is influenced
    by depth psychology and the work of thinkers such as Carl Jung, Robert A. Johnson,
    and Marie-Louise von Franz.

    TASK:
    Offer a reflective interpretation of the dream below.
    Do not reduce the dream to a single fixed meaning.
    Help the dreamer gently explore the emotional tone, symbols, and inner movement
    of the dream.

    DREAM:
    \"\"\"{dream_text}\"\"\"

    OUTPUT:
    Return ONLY valid JSON with the following structure:

    {{
      "fluid_interpretation": "6–10 sentence reflective narrative",
      "tags": {{
        "dominant_emotions": ["1–3 short emotions"],
        "archetypal_themes": ["1–3 themes"],
        "symbols": ["1–3 key symbols"]
      }},
      "reflective_questions": [
        "2–4 open-ended questions"
      ]
    }}

    STYLE RULES:
    - Write in flowing, imaginal prose.
    - Use metaphor and emotional resonance over explanation.
    - Keep tags brief (one or two words).
    - Questions should invite curiosity, not provide advice.
    """).strip()



def analyze_dream(dream_text: str) -> str:
    prompt = build_dream_prompt(dream_text)

    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a wise, Jungian dream analyst."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.9,  # higher = more fluid and creative
    )

    return resp.choices[0].message.content.strip()

