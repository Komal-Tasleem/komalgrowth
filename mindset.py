import streamlit as st
import random
import datetime
import pandas as pd

# 🌟 Page Config
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

# 🎉 App Title
st.title("🌱Growth Mindset Challenge:Web App with Streamlit.")
st.subheader("🚀 Welcome to Your Own Growth Journey!")
st.write("Embrace challenges, learn from experiences, and celebrate your wins every day! ✨")

# 💡 Growth Mindset Quotes (Offline)
quotes = [
    "💡 Believe you can and you're halfway there. - Theodore Roosevelt",
    "💡 Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "💡 Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "💡 The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "💡 It does not matter how slowly you go as long as you do not stop. - Confucius",
]
quote_of_the_day = random.choice(quotes)
st.info(f"**Today's Growth Mindset Quote:** {quote_of_the_day}")

# 🎯 Daily Challenge
st.subheader("🎯 What's Your Challenge Today?")
challenges = [
    "🚀 Write down 3 things you learned today!",
    "📖 Read about a famous person who overcame challenges.",
    "✍️ Write a letter to your future self.",
    "🎯 Set a small goal for today and achieve it.",
    "🙏 Practice gratitude by listing 5 things you're grateful for.",
    "💬 Teach someone something new today.",
    "📚 Read 10 pages of a book that inspires you.",
]
today = datetime.date.today()
todays_challenge = challenges[today.day % len(challenges)]
st.success(f"**Today's Challenge:** {todays_challenge}")

# 📝 Reflection Section
st.subheader("📝 Reflect on Your Learning")
st.write("Take a moment to reflect on your progress and insights from today's challenge.")

completed = st.radio("Did you complete today's challenge?", ["Yes", "No"])
lesson = st.text_area("🌱 What did you learn today?")
feeling = st.text_area("😊 How did this challenge make you feel?")
improvement = st.text_area("🔄 What will you improve tomorrow?")

# 🎉 Celebration Section
st.subheader("🎉 Celebrate Your Wins")
st.write("Every step forward is worth celebrating! What progress are you proud of today?")
celebration = st.text_area("🎊 Share your small or big wins!")

# 💾 Save Reflection
if st.button("💾 Save Reflection & Wins"):
    if lesson or feeling or improvement or celebration:
        data = {
            "Date": [str(today)],
            "Completed": [completed],
            "Lesson": [lesson],
            "Feeling": [feeling],
            "Improvement": [improvement],
            "Celebration": [celebration],
        }
        df = pd.DataFrame(data)
        df.to_csv("reflections.csv", mode="a", header=False, index=False)
        st.success("🎯 Reflection & Wins saved successfully!")
    else:
        st.error("⚠️ Please fill at least one section before saving.")

st.write("**Stay consistent & keep growing! 💪**")
