```python
from rouge import Rouge

# Reference and generated summaries
rouge = Rouge()
reference = "The quick brown fox jumps over the lazy dog"
generated = "The fast brown fox jumps over a lazy dog"

scores = rouge.get_scores(generated, reference)
print("ROUGE Scores:", scores)
```

This code snippet demonstrates how to use the ROUGE metric to compare a generated summary with a reference summary. Here’s a breakdown:

1. **Import and Initialization:**  
   The code starts by importing the `Rouge` class from the `rouge` library and creates an instance of it:
   ```python
   from rouge import Rouge
   rouge = Rouge()
   ```

2. **Defining Summaries:**  
   Two summaries are defined:
   - **Reference Summary:** `"The quick brown fox jumps over the lazy dog"`  
     This is considered the ground truth or the ideal summary.
   - **Generated Summary:** `"The fast brown fox jumps over a lazy dog"`  
     This is the summary produced by a model that we want to evaluate.

3. **Computing ROUGE Scores:**  
   The `get_scores` method is then called with the generated and reference summaries as arguments:
   ```python
   scores = rouge.get_scores(generated, reference)
   ```
   This method calculates various ROUGE metrics, which typically include:
   - **ROUGE-1:** Measures the overlap of unigrams (single words) between the summaries.
   - **ROUGE-2:** Measures the overlap of bigrams (pairs of consecutive words).
   - **ROUGE-L:** Measures the longest common subsequence between the summaries, capturing sentence-level structure.

   Each metric returns scores for precision (p), recall (r), and F1-score (f).

4. **Output:**  
   Finally, the code prints the computed ROUGE scores:
   ```python
   print("ROUGE Scores:", scores)
   ```
   The printed output will be a dictionary (or a list of dictionaries) showing how similar the generated summary is to the reference summary according to these metrics.

In essence, this script evaluates the quality of the generated summary by quantifying how much it overlaps with the reference summary in terms of word and phrase matches. This kind of evaluation is widely used in natural language processing tasks such as text summarization and machine translation.