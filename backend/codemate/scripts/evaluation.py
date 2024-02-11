# Code is not used in the final version of the project.
# Keeping it for future reference.
# This code helps to compare two code snippets and decide which one is better
# automatically using the GPT-4 model from OpenAI.

from collections import Counter

import langchain
import numpy as np
import openai
from langchain.callbacks import get_openai_callback
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

COMPARISON_PROMPT = """
You are helping a person writing the current code in the excerpt below. You can suggest them to use one of the snippets below. 
Your goal is to suggest the snippet that does what the current code does in the best way possible.

Current code:
```python
{snippet}
```

Suggested snippet 1: 
```python
{example_1}
```

Suggested snippet 2:
```python
{example_2}
```

Which snippet is the best one? Print only 1 or 2. 
""".strip()


prompt = PromptTemplate(template=COMPARISON_PROMPT, input_variables=["snippet", "example_1", "example_2"])
llm = ChatOpenAI(model_name="gpt-4", temperature=0)
chain = prompt | llm


def run_pair_comparison(snippet, example_1, example_2):
    # Swap in 50% of the cases
    swap = np.random.choice([True, False])
    if swap:
        example_1, example_2 = example_2, example_1

    # Run the chain
    result = chain.invoke(dict(snippet=snippet, example_1=example_1, example_2=example_2))
    result = result.content
    result = result.strip()
    result = int(result)

    if swap:
        result = 2 if result == 1 else 1

    result = result - 1
    return result, swap


def run_pair_comparison_multiple(snippet, example_1, example_2, n=5):
    results = []
    for i in range(n):
        result, swap = run_pair_comparison(snippet, example_1, example_2)
        results.append(result)
        print(f"Iteration {i}: {result} (swapped: {swap})")

    counter = Counter(results)
    if counter[0] > counter[1]:
        print("Example 1 is better")
        return 1
    else:
        print("Example 2 is better")
        return 2
