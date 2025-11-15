Email Spam Probability Estimator using Bayes' Theorem

A Streamlit Application

📝 Project Overview

This project demonstrates the use of Bayes’ Theorem by estimating the probability that an email is spam based on keywords.
Unlike large machine-learning models, this project uses a manual Naive Bayes approach with a small word-frequency dataset.

Users can type any email text, and the app calculates:

Probability that the email is SPAM

Probability that the email is NOT SPAM

Final classification result

This makes the project simple, transparent, and perfect for explaining Bayes Theorem.

🎯 Key Features

✔ Manual probability calculation using Bayes’ Theorem

✔ Streamlit-based interactive UI

✔ Keyword-based spam classification

✔ Laplace Smoothing implemented

✔ Clean probability score output

✔ Easy to understand for beginners

✔ No external ML libraries required

📌 How It Works (Bayes Theorem)

For each word in the email text, the app calculates:

𝑃
(
𝑆
𝑝
𝑎
𝑚
∣
𝑊
𝑜
𝑟
𝑑
𝑠
)
=
𝑃
(
𝑊
𝑜
𝑟
𝑑
𝑠
∣
𝑆
𝑝
𝑎
𝑚
)
⋅
𝑃
(
𝑆
𝑝
𝑎
𝑚
)
𝑃
(
𝑊
𝑜
𝑟
𝑑
𝑠
)
P(Spam∣Words)=
P(Words)
P(Words∣Spam)⋅P(Spam)
	​


Multiple words → multiply probabilities (done using log probabilities).

Finally, the app compares:

log(P(Spam | Email)) vs log(P(Ham | Email))


Higher score → Final classification.

🛠️ Tech Stack

Python 3.8+

Streamlit

NumPy
