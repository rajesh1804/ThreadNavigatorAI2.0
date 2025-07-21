import streamlit as st
from utils import load_thread_data, get_thread_by_id

st.set_page_config(page_title="ThreadNavigatorAI 2.0", layout="wide")
st.title("🧵 ThreadNavigatorAI 2.0")
st.markdown("A multi-agent Reddit thread analyzer built by Rajesh 💼")

# Load data
data = load_thread_data()
thread_ids = [t["thread_id"] for t in data]
selected_id = st.selectbox("Select a thread to inspect", thread_ids)

thread = get_thread_by_id(data, selected_id)

if thread:
    st.subheader("📌 Title:")
    st.markdown(f"**{thread['title']}**")

    with st.expander("🗣️ Thread Posts"):
        for post in thread["summary"].split("\n"):
            st.markdown(f"- {post}")

    st.subheader("🧠 Summary")
    st.markdown(thread["summary"])

    st.subheader("🔎 Fact Checks")
    for f in thread["fact_check"]:
        st.markdown(f"- **Claim:** {f['claim']}\n  \t**Judgment:** {f['judgment']}")

    st.subheader("📊 Evaluation")
    eval_ = thread["evaluation"]
    if isinstance(eval_, dict):
        for k, v in eval_.items():
            st.markdown(f"- **{k.capitalize()}**: {v['score']} — {v['reason']}")
    elif isinstance(eval_, str):
        import json
        for k, v in json.loads(eval_).items():
            st.markdown(f"- **{k.capitalize()}**: {v['score']} — {v['reason']}")
    else:
        st.warning(f"Evaluation skipped: {eval_}")

    st.caption("✅ Powered by OpenRouter LLMs and modular multi-agent stack.")
