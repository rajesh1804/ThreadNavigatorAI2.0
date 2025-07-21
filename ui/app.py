# import streamlit as st
# from utils import load_thread_data, get_thread_by_id

# st.set_page_config(page_title="ThreadNavigatorAI 2.0", layout="wide")
# st.title("🧵 ThreadNavigatorAI 2.0")
# st.markdown("A multi-agent Reddit thread analyzer built by Rajesh 💼")

# data = load_thread_data()
# thread_ids = [t["thread_id"] for t in data]
# selected_id = st.selectbox("Select a thread to inspect", thread_ids)

# thread = get_thread_by_id(data, selected_id)

# if thread:
#     st.subheader(f"📌 Title: **{thread['title']}**")
#     # st.markdown(f"**{thread['title']}**")

#     # 🧾 Summary Type and Source
#     is_mock = thread.get("is_mock", False)
#     summary_type = "🤖 Simulated Summary" if is_mock else "🔁 Real Summary"
#     source_url = thread.get("source_url")

#     st.markdown(f"- **Summary Type**: {summary_type}")
#     if source_url:
#         st.markdown(f"- 📎 [Source Link]({source_url})")

#     with st.expander("🗣️ Thread Posts"):
#         for post in thread["posts"]:
#             st.markdown(f"- {post}")

#     st.subheader("🧠 Summary")
#     st.markdown(thread["summary"])

#     st.subheader("🔎 Fact Checks")
#     for f in thread["fact_check"]:
#         st.markdown(f"- **Claim:** {f['claim']}\n  \t**Judgment:** {f['judgment']}")

#     st.subheader("⚡ Latency (s)")
#     latency = thread.get("latency", {})
#     if latency:
#         for k, v in latency.items():
#             st.markdown(f"- **{k.capitalize()}**: {v} sec")
#     else:
#         st.info("Latency not recorded for this thread.")

#     st.subheader("📊 Evaluation")
#     eval_ = thread["evaluation"]
#     if isinstance(eval_, dict):
#         for k, v in eval_.items():
#             st.markdown(f"- **{k.capitalize()}**: {v['score']} — {v['reason']}")
#     elif isinstance(eval_, str):
#         import json
#         for k, v in json.loads(eval_).items():
#             st.markdown(f"- **{k.capitalize()}**: {v['score']} — {v['reason']}")
#     else:
#         st.warning(f"Evaluation skipped: {eval_}")

#     st.caption("✅ Powered by OpenRouter LLMs and modular multi-agent stack.")


# import streamlit as st
# import plotly.graph_objects as go
# from utils import load_thread_data, get_thread_by_id

# st.set_page_config(page_title="ThreadNavigatorAI 2.0", layout="wide")
# st.title("🧵 ThreadNavigatorAI 2.0")
# st.markdown("A multi-agent Reddit thread analyzer built by Rajesh 💼")

# # Load data
# data = load_thread_data()
# thread_ids = [t["thread_id"] for t in data]
# selected_id = st.selectbox("Select a thread to inspect", thread_ids)

# thread = get_thread_by_id(data, selected_id)

# if thread:
#     st.subheader("📌 Title:")
#     st.markdown(f"**{thread['title']}**")

#     # Summary type note
#     is_mock = thread.get("is_mock", False)
#     summary_type = "🤖 Simulated Summary" if is_mock else "🔁 Real Summary"
#     summary_color = "#e0e0e0" if is_mock else "#d4edda"
#     source_url = thread.get("source_url")

#     with st.container():
#         st.markdown(f"""
#             <div style='background-color:{summary_color};padding:10px;border-radius:10px'>
#             <b>Summary Type:</b> {summary_type}<br>
#             {'<b>📌 Source:</b> <a href="' + source_url + '" target="_blank">Reddit Thread</a>' if source_url else ''}
#             </div>
#         """, unsafe_allow_html=True)

#     with st.expander("🗣️ Thread Posts"):
#         for post in thread["posts"]:
#             st.markdown(f"- {post}")

#     st.subheader("🧠 Summary")
#     st.markdown(thread["summary"])

#     st.subheader("🔎 Fact Checks")
#     for f in thread["fact_check"]:
#         st.markdown(f"- **Claim:** {f['claim']}\n  \t**Judgment:** {f['judgment']}")

#     st.subheader("⚡ Latency (s)")
#     latency = thread.get("latency", {})
#     if latency:
#         for k, v in latency.items():
#             tooltip = f"LLM Model: {k}"  # Placeholder: Replace with actual per-agent model later
#             st.markdown(f"- **{k.capitalize()}**: {v} sec  \n  <span style='color:gray;font-size:small'>{tooltip}</span>", unsafe_allow_html=True)
#     else:
#         st.info("Latency not recorded for this thread.")

#     st.subheader("📊 Evaluation")
#     eval_ = thread["evaluation"]
#     if isinstance(eval_, str):
#         import json
#         eval_ = json.loads(eval_)

#     if isinstance(eval_, dict):
#         scores = []
#         for k, v in eval_.items():
#             st.markdown(f"- **{k.capitalize()}**: {v['score']} — {v['reason']}")
#             scores.append(v['score'])

#         # Bar Chart
#         fig = go.Figure(go.Bar(
#             x=list(eval_.keys()),
#             y=scores,
#             text=scores,
#             textposition='auto',
#             marker_color='lightskyblue'
#         ))
#         fig.update_layout(
#             title_text='Evaluation Metrics',
#             yaxis=dict(range=[0, 5], title='Score'),
#             xaxis=dict(title='Metric'),
#             margin=dict(l=20, r=20, t=30, b=20)
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning(f"Evaluation skipped: {eval_}")

#     st.caption("✅ Powered by OpenRouter LLMs and modular multi-agent stack.")


import streamlit as st
import plotly.graph_objects as go
import json
from utils import load_thread_data, get_thread_by_id

st.set_page_config(page_title="ThreadNavigatorAI 2.0", layout="wide")
st.title("🧵 ThreadNavigatorAI 2.0")
st.markdown("A multi-agent Reddit thread analyzer built by Rajesh 💼")

# Load data
data = load_thread_data()
thread_ids = [t["thread_id"] for t in data]

# 🔍 Search bar
search_query = st.text_input("🔍 Search threads by title", "")
filtered_ids = [t["thread_id"] for t in data if search_query.lower() in t["title"].lower()]

selected_id = st.selectbox("Select a thread to inspect", filtered_ids if search_query else thread_ids)
thread = get_thread_by_id(data, selected_id)

if thread:
    st.subheader("📌 Title:")
    st.markdown(f"**{thread['title']}**")

    # ✅ Summary type badge and source link
    is_mock = thread.get("is_mock", False)
    summary_type = "🤖 Simulated Summary" if is_mock else "🔁 Real Summary"
    summary_color = "#e0e0e0" if is_mock else "#d4edda"
    source_url = thread.get("source_url", "")
    source_html = f'<b>📎 Source:</b> <a href="{source_url}" target="_blank">Reddit Thread</a>' if source_url else ""

    st.markdown(f"""
        <div style='background-color:{summary_color};padding:10px;border-radius:10px'>
            <b>Summary Type:</b> {summary_type}<br>
            {source_html}
        </div>
    """, unsafe_allow_html=True)

    with st.expander("🗣️ Thread Posts"):
        for post in thread["posts"]:
            st.markdown(f"- {post}")

    st.subheader("🧠 Summary")
    st.markdown(thread["summary"])

    st.subheader("🔎 Fact Checks")
    for f in thread["fact_check"]:
        judgment = f['judgment']
        if "Correct" in judgment:
            emoji = "🟢"
        elif "Incorrect" in judgment:
            emoji = "🔴"
        else:
            emoji = "⚪"
        st.markdown(f"- **Claim:** {f['claim']}  \n  **Judgment:** {emoji} {judgment}")

    st.subheader("⚡ Latency (s)")
    latency = thread.get("latency", {})
    models = thread.get("models_used", {})  # ✅ actual models used per agent

    if latency:
        for k, v in latency.items():
            model_name = models.get(k.lower(), "Unknown")
            st.markdown(f"- **{k.capitalize()}**: {v} sec  \n  <span style='color:gray;font-size:small'>Model: `{model_name}`</span>", unsafe_allow_html=True)
    else:
        st.info("Latency not recorded for this thread.")

    st.subheader("📊 Evaluation")
    eval_ = thread["evaluation"]
    if isinstance(eval_, str):
        eval_ = json.loads(eval_)

    if isinstance(eval_, dict):
        scores = []
        for k, v in eval_.items():
            st.markdown(f"- **{k.capitalize()}**: {v['score']} — {v['reason']}")
            scores.append(v['score'])

        fig = go.Figure(go.Bar(
            x=list(eval_.keys()),
            y=scores,
            text=scores,
            textposition='auto',
            marker_color='lightskyblue'
        ))
        fig.update_layout(
            title_text='Evaluation Metrics',
            yaxis=dict(range=[0, 5], title='Score'),
            xaxis=dict(title='Metric'),
            margin=dict(l=20, r=20, t=30, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(f"Evaluation skipped: {eval_}")

    st.caption("✅ Powered by OpenRouter LLMs and modular multi-agent stack.")
