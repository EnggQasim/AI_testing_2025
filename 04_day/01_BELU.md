### Example Setup

Suppose you have:

- **Reference translation:**  
  *"there is a cat on the mat"*

- **Candidate translation:**  
  *"the cat is on the mat"*

Notice that the candidate is almost the same as the reference, except for the missing word "there". We want to show how BLEU evaluates this difference.

---

### Step 1. Tokenization

Both sentences are split into words (unigrams):

- **Reference tokens:**  
  `['there', 'is', 'a', 'cat', 'on', 'the', 'mat']`

- **Candidate tokens:**  
  `['the', 'cat', 'is', 'on', 'the', 'mat']`

---

### Step 2. Modified n-gram Precision

BLEU evaluates modified precision for different n-grams (commonly 1-gram through 4-gram). Let’s focus on unigrams for this example:

1. **Count each word’s occurrences in the candidate:**  
   - "the": appears 2 times  
   - "cat": 1  
   - "is": 1  
   - "on": 1  
   - "mat": 1  

2. **For each candidate word, find the maximum count in the reference (clipping):**  
   - "the": In the reference, "the" appears 1 time → clip candidate count from 2 to 1  
   - "cat": appears 1 time (clip remains 1)  
   - "is": appears 1 time (1)  
   - "on": appears 1 time (1)  
   - "mat": appears 1 time (1)

3. **Sum of clipped counts:**  
   \(1 ("the") + 1 ("cat") + 1 ("is") + 1 ("on") + 1 ("mat") = 5\)

4. **Total number of candidate unigrams:**  
   \(6\)

5. **Unigram precision:**  
   \(P_1 = \frac{5}{6} \approx 0.833\)

For higher-order n-grams (bigrams, trigrams, etc.), similar counts are computed; typically the more words you require to match in order, the lower the precision.

---

### Step 3. Brevity Penalty

BLEU includes a brevity penalty (BP) to discourage very short candidate translations. It is defined as:

\[
\text{BP} = 
\begin{cases}
1 & \text{if } c > r \\
\exp\left(1 - \frac{r}{c}\right) & \text{if } c \le r
\end{cases}
\]

Here,  
- \(c\) is the candidate length (6), and  
- \(r\) is the reference length (7).

Since \(6 < 7\), we have:

\[
\text{BP} = \exp\left(1 - \frac{7}{6}\right) = \exp\left(-\frac{1}{6}\right) \approx 0.846
\]

---

### Step 4. Final BLEU Score

In the standard BLEU-4 setup, the geometric mean of the modified precisions for 1-gram through 4-gram is computed and then multiplied by the brevity penalty. In our simple example we only computed the unigram precision (for teaching purposes). Thus, an approximate BLEU score (using only 1-gram) would be:

\[
\text{BLEU} \approx \text{BP} \times P_1 \approx 0.846 \times 0.833 \approx 0.705
\]

(When using full BLEU-4, you would compute similar scores for bigrams, trigrams, and 4-grams and then take the weighted geometric mean.)

---

### Python Code Example

You can illustrate this with Python using NLTK:

```python
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk import word_tokenize

# Define the reference and candidate sentences
reference = "there is a cat on the mat"
candidate = "the cat is on the mat"

# Tokenize the sentences
reference_tokens = [word_tokenize(reference)]  # Note: list of one reference sentence
candidate_tokens = word_tokenize(candidate)

# Use a smoothing function to avoid zero scores on higher n-grams (if needed)
smooth_fn = SmoothingFunction().method1

# Calculate BLEU score (default BLEU-4)
bleu_score = sentence_bleu(reference_tokens, candidate_tokens, smoothing_function=smooth_fn)

print("BLEU score:", bleu_score)
```

When you run this code, you should see a BLEU score roughly in the same range as our manual calculation—keeping in mind that the full BLEU-4 score combines multiple n-gram precisions.

---

### Summary for Teaching

- **Tokenization:** Break both candidate and reference into words.
- **Modified Precision:** Count how many words (and n-grams) in the candidate also appear in the reference, but “clip” counts so that repeated words aren’t over-rewarded.
- **Brevity Penalty:** Penalize candidates shorter than the reference.
- **Final BLEU:** Multiply the brevity penalty by the geometric mean of modified n-gram precisions.

This example provides a concrete walkthrough of BLEU’s components and shows how even a small change (omitting “there”) impacts the final score. It’s a great starting point for teaching how machine translation quality is evaluated.

---

*According to Papineni et al. (2002) citeturn0search10, BLEU remains one of the most widely used metrics because it is simple to compute and correlates reasonably well with human judgment at the corpus level.*