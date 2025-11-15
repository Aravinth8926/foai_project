import streamlit as st
import numpy as np

st.title("📧 Email Spam Probability Estimator using Bayes' Theorem")
st.write("This app uses Bayes’ theorem to estimate the probability that an email is spam based on keywords.")

# Sample training dataset (small & simple)
spam_words = {
    "offer": 8,
    "free": 10,
    "winner": 6,
    "money": 5,
    "now": 4
}

ham_words = {
    "meeting": 7,
    "project": 6,
    "schedule": 5,
    "team": 4,
    "discussion": 3
}

total_spam = sum(spam_words.values())
total_ham = sum(ham_words.values())

# Priors
P_spam = 0.5
P_ham = 0.5

st.subheader("Enter Email Text")
email_text = st.text_area("Type your email content below:")

def calculate_probability(email):
    words = email.lower().split()
    
    # Laplace smoothing
    spam_prob = np.log(P_spam)
    ham_prob = np.log(P_ham)

    for word in words:
        spam_word_count = spam_words.get(word, 0) + 1
        ham_word_count = ham_words.get(word, 0) + 1

        spam_prob += np.log(spam_word_count / (total_spam + len(spam_words)))
        ham_prob += np.log(ham_word_count / (total_ham + len(ham_words)))

    return spam_prob, ham_prob

if st.button("Calculate Spam Probability"):
    if email_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        spam_score, ham_score = calculate_probability(email_text)

        if spam_score > ham_score:
            result = "🚨 This email is likely **SPAM**"
        else:
            result = "✅ This email is likely **NOT SPAM**"

        # Convert log-probabilities to normal probability
        spam_prob = np.exp(spam_score) / (np.exp(spam_score) + np.exp(ham_score))

        st.subheader("📊 Result")
        st.write(result)
        st.write(f"**Spam Probability:** {spam_prob:.2f}")
