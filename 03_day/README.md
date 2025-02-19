Sure! I'll provide Python code examples for each evaluation metric, categorized by Machine Learning (Classification & Regression), Deep Learning, and Generative AI.

---

# **1. Machine Learning Model Evaluation Metrics**
## **1.1 Classification Metrics**
Let's use `scikit-learn` to demonstrate common classification metrics.

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score, roc_curve
import numpy as np

# Simulated true labels and predicted labels
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
y_pred = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

# Accuracy
accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Precision
precision = precision_score(y_true, y_pred)
print(f"Precision: {precision:.2f}")

# Recall
recall = recall_score(y_true, y_pred)
print(f"Recall: {recall:.2f}")

# F1 Score
f1 = f1_score(y_true, y_pred)
print(f"F1 Score: {f1:.2f}")

# Confusion Matrix
conf_matrix = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", conf_matrix)

# ROC AUC Score
auc = roc_auc_score(y_true, y_pred)
print(f"AUC Score: {auc:.2f}")
```

---

## **1.2 Regression Metrics**
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Simulated true and predicted values
y_true = np.array([3.5, 2.8, 4.0, 5.2, 3.3])
y_pred = np.array([3.7, 2.9, 3.8, 5.1, 3.1])

# Mean Absolute Error (MAE)
mae = mean_absolute_error(y_true, y_pred)
print(f"Mean Absolute Error: {mae:.2f}")

# Mean Squared Error (MSE)
mse = mean_squared_error(y_true, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse:.2f}")

# R-Squared (R²)
r2 = r2_score(y_true, y_pred)
print(f"R-Squared: {r2:.2f}")
```

---

## **1.3 Clustering Metrics**
```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

# Generating dummy data
X = np.random.rand(10, 2)

# Applying KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

# Silhouette Score
silhouette = silhouette_score(X, labels)
print(f"Silhouette Score: {silhouette:.2f}")
```

---

# **2. Deep Learning Model Evaluation Metrics**
## **2.1 BLEU Score (For Text Generation)**
```python
from nltk.translate.bleu_score import sentence_bleu

# Reference and generated text
reference = [['the', 'cat', 'is', 'on', 'the', 'mat']]
candidate = ['the', 'cat', 'is', 'on', 'the', 'mat']

# BLEU Score
bleu = sentence_bleu(reference, candidate)
print(f"BLEU Score: {bleu:.2f}")
```

---

## **2.2 Perplexity (For Language Models)**
```python
import numpy as np

# Probability of a test sentence under the model
probabilities = np.array([0.2, 0.3, 0.1, 0.4])
perplexity = np.exp(-np.sum(np.log(probabilities)) / len(probabilities))
print(f"Perplexity: {perplexity:.2f}")
```

---

## **2.3 ROUGE Score (For Text Summarization)**
```python
from rouge import Rouge

# Reference and generated summaries
rouge = Rouge()
reference = "The quick brown fox jumps over the lazy dog"
generated = "The fast brown fox jumps over a lazy dog"

scores = rouge.get_scores(generated, reference)
print("ROUGE Scores:", scores)
```

---

# **3. Generative AI Model Evaluation Metrics**
## **3.1 Inception Score (For Image Generation)**
```python
import numpy as np
from scipy.stats import entropy

# Simulated predictions from an Inception model
p_yx = np.array([[0.1, 0.9], [0.2, 0.8], [0.7, 0.3], [0.5, 0.5]])
p_y = np.mean(p_yx, axis=0)

# Compute KL divergence for each sample
kl_divergences = [entropy(p, p_y) for p in p_yx]

# Compute Inception Score
inception_score = np.exp(np.mean(kl_divergences))
print(f"Inception Score: {inception_score:.2f}")
```

---

## **3.2 Fréchet Inception Distance (FID)**
```python
from scipy.linalg import sqrtm
import numpy as np

# Simulated feature representations from a real and generated image set
mu1, sigma1 = np.array([1, 2]), np.array([[1, 0.5], [0.5, 1]])
mu2, sigma2 = np.array([1.5, 2.5]), np.array([[1, 0.3], [0.3, 1]])

# Compute FID
diff = mu1 - mu2
covmean = sqrtm(sigma1.dot(sigma2))

fid = np.sum(diff**2) + np.trace(sigma1 + sigma2 - 2 * covmean)
print(f"FID Score: {fid:.2f}")
```

---

## **3.3 Structural Similarity Index (SSIM)**
```python
from skimage.metrics import structural_similarity as ssim
import numpy as np

# Simulated images (2D numpy arrays)
image1 = np.random.rand(100, 100)
image2 = np.random.rand(100, 100)

# Compute SSIM
ssim_value = ssim(image1, image2)
print(f"SSIM Score: {ssim_value:.2f}")
```

---

# **Conclusion**
These Python examples cover:
- **Classification**: Accuracy, Precision, Recall, F1, Confusion Matrix, AUC.
- **Regression**: MAE, MSE, RMSE, R².
- **Clustering**: Silhouette Score.
- **Deep Learning**: BLEU, Perplexity, ROUGE.
- **Generative AI**: Inception Score, FID, SSIM.

Would you like me to generate a dataset for testing these metrics with actual ML/DL models? 🚀