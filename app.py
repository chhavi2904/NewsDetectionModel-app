import streamlit as st
from predict import predict_news

st.set_page_config(page_title="Fake News Detection", layout="centered")

st.title("📰 Fake News Detection App")
st.write("Enter a news article and check whether it's real or fake.")

# Input text box
news_input = st.text_area("📝 Paste the news article here:", height=250)

# Predict button
if st.button("🚀 Predict"):
    if not news_input.strip():
        st.warning("Please enter a news article to analyze.")
    else:
        # Call your prediction function
        with st.spinner("Analyzing the article..."):
            output = predict_news(news_input)

        # Show result
        if output['result'] == "Real News":
            st.success("✅ The article appears to be **REAL NEWS**.")
        else:
            st.error("⚠️ The article appears to be **FAKE NEWS**.")

        # Show confidence
        st.markdown(f"**Model Confidence:** {output['confidence']}")

        # Show related articles if result is Real News
        if output['related_articles']:
            st.markdown("### 🔍 Related Articles")
            for url in output['related_articles']:
                st.markdown(f"- [{url}]({url})")


st.markdown("---")
st.caption("Built with Streamlit · Fake News Detection using XGBoost")
