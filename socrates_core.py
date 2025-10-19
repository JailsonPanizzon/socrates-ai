import os



def ask_heuristic_questions(user_input):
    prompt = build_prompt(user_input, mode)

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "Você é um mentor que só responde com perguntas."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=300
    )

    return response['choices'][0]['message']['content'].strip()