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

# import streamlit as st
# import json
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

#     # Summary badge + Source link
#     is_mock = thread.get("is_mock", False)
#     summary_type = "🤖 Simulated Summary" if is_mock else "🔁 Real Summary"
#     summary_color = "#e0e0e0" if is_mock else "#d4edda"
#     source_url = thread.get("source_url", "")
#     source_html = f'<b>📎 Source:</b> <a href="{source_url}" target="_blank">Reddit Thread</a>' if source_url else ""

#     st.markdown(f"""
#         <div style='background-color:{summary_color};padding:10px;border-radius:10px;margin-bottom:10px'>
#             <b>Summary Type:</b> {summary_type}<br>
#             {source_html}
#         </div>
#     """, unsafe_allow_html=True)

#     with st.expander("🗣️ Thread Posts", expanded=False):
#         for post in thread["posts"]:
#             st.markdown(f"- {post}")

#     st.subheader("🧠 Summary")
#     st.markdown(thread["summary"])

#     st.subheader("🔎 Fact Checks")
#     with st.expander("View fact check details", expanded=False):
#         for f in thread["fact_check"]:
#             judgment = f["judgment"]
#             emoji = "🟢" if "Correct" in judgment else "🔴" if "Incorrect" in judgment else "⚪"
#             st.markdown(f"- **Claim:** {f['claim']}  \n  **Judgment:** {emoji} {judgment}")

#     st.subheader("⚡ Latency (s)")
#     latency = thread.get("latency", {})
#     models = thread.get("models_used", {})  # per-agent model

#     if latency:
#         for k, v in latency.items():
#             model_name = models.get(k.lower(), "Unknown")
#             st.markdown(f"- **{k.capitalize()}**: {v} sec  \n  <span style='color:gray;font-size:small'>Model: `{model_name}`</span>", unsafe_allow_html=True)
#     else:
#         st.info("Latency not recorded for this thread.")

#     st.subheader("📊 Evaluation")
#     eval_ = thread["evaluation"]
#     if isinstance(eval_, str):
#         eval_ = json.loads(eval_)

#     if isinstance(eval_, dict):
#         with st.expander("View evaluation details", expanded=False):
#             for k, v in eval_.items():
#                 score = v['score']
#                 reason = v['reason']
#                 emoji = "🟢" if score >= 4 else "🟡" if score == 3 else "🔴"
#                 st.markdown(f"- **{k.capitalize()}**: {emoji} {score} — {reason}")
#     else:
#         st.warning(f"Evaluation skipped: {eval_}")

#     st.caption("✅ Powered by OpenRouter LLMs and modular multi-agent stack.")


# import streamlit as st
# import json
# from utils import load_thread_data, get_thread_by_id

# st.set_page_config(page_title="ThreadNavigatorAI 2.0", layout="wide")
# st.title("🧵 ThreadNavigatorAI 2.0")
# st.markdown("A multi-agent Reddit thread analyzer built by Rajesh 💼")

# # Sidebar controls
# st.sidebar.header("⚙️ Display Options")
# show_latency = st.sidebar.checkbox("Show Latency", value=True)
# show_eval = st.sidebar.checkbox("Show Evaluation", value=True)
# show_download = st.sidebar.checkbox("Enable Download", value=True)

# # Load thread data
# data = load_thread_data()
# thread_ids = [t["thread_id"] for t in data]
# selected_id = st.selectbox("Select a thread to inspect", thread_ids)
# thread = get_thread_by_id(data, selected_id)

# if thread:
#     st.subheader("📌 Title:")
#     st.markdown(f"**{thread['title']}**")

#     # 🪪 Summary Type + Source Link
#     is_mock = thread.get("is_mock", False)
#     summary_type = "🤖 Simulated Summary" if is_mock else "🔁 Real Summary"
#     summary_color = "#e0e0e0" if is_mock else "#d4edda"
#     source_url = thread.get("source_url", "")
#     source_html = f'<b>📎 Source:</b> <a href="{source_url}" target="_blank">Reddit Thread</a>' if source_url else ""

#     st.markdown(f"""
#         <div style='background-color:{summary_color};padding:10px;border-radius:10px;margin-bottom:10px'>
#             <b>Summary Type:</b> {summary_type}<br>
#             {source_html}
#         </div>
#     """, unsafe_allow_html=True)

#     with st.expander("🗣️ Thread Posts", expanded=False):
#         for post in thread["posts"]:
#             st.markdown(f"- {post}")

#     st.subheader("🧠 Summary")
#     st.markdown(thread["summary"])

#     # 📥 Download Button right below summary
#     if show_download:
#         json_str = json.dumps(thread, indent=2)
#         st.download_button(
#             "⬇️ Download JSON Result",
#             data=json_str,
#             file_name=f"{thread['thread_id']}.json",
#             mime="application/json"
#         )

#     st.subheader("🔎 Fact Checks")
#     with st.expander("View fact check details", expanded=False):
#         for f in thread["fact_check"]:
#             judgment = f["judgment"]
#             emoji = "🟢" if "Correct" in judgment else "🔴" if "Incorrect" in judgment else "⚪"
#             st.markdown(f"- **Claim:** {f['claim']}  \n  **Judgment:** {emoji} {judgment}")

#     if show_latency:
#         st.subheader("⚡ Latency (s)")
#         latency = thread.get("latency", {})
#         models = thread.get("models_used", {})
#         if latency:
#             for k, v in latency.items():
#                 model_name = models.get(k.lower(), "Unknown")
#                 st.markdown(f"- **{k.capitalize()}**: {v} sec  \n  <span style='color:gray;font-size:small'>Model: `{model_name}`</span>", unsafe_allow_html=True)
#         else:
#             st.info("Latency not recorded for this thread.")

#     if show_eval:
#         st.subheader("📊 Evaluation")
#         eval_ = thread["evaluation"]
#         if isinstance(eval_, str):
#             eval_ = json.loads(eval_)
#         if isinstance(eval_, dict):
#             with st.expander("View evaluation details", expanded=False):
#                 for k, v in eval_.items():
#                     score = v["score"]
#                     reason = v["reason"]
#                     emoji = "🟢" if score >= 4 else "🟡" if score == 3 else "🔴"
#                     st.markdown(f"- **{k.capitalize()}**: {emoji} {score} — {reason}")
#         else:
#             st.warning(f"Evaluation skipped: {eval_}")

#     # if show_download:
#     #     st.subheader("📥 Export")
#     #     json_str = json.dumps(thread, indent=2)
#     #     st.download_button("⬇️ Download JSON Result", data=json_str, file_name=f"{thread['thread_id']}.json", mime="application/json")

#     st.caption("✅ Powered by OpenRouter LLMs and modular multi-agent stack.")


# import streamlit as st
# import json
# from utils import load_thread_data, get_thread_by_id

# st.set_page_config(page_title="ThreadNavigatorAI 2.0", layout="wide")
# st.title("🧵 ThreadNavigatorAI 2.0")
# st.markdown("A multi-agent Reddit thread analyzer built by Rajesh 💼")

# # Load thread data
# data = load_thread_data()
# thread_ids = [t["thread_id"] for t in data]

# # Sidebar controls
# st.sidebar.header("⚙️ Display Options")
# selected_id = st.sidebar.selectbox("🧵 Select a Thread", thread_ids)
# show_latency = st.sidebar.checkbox("Show Latency", value=True)
# show_eval = st.sidebar.checkbox("Show Evaluation", value=True)
# show_download = st.sidebar.checkbox("Enable Download", value=True)

# thread = get_thread_by_id(data, selected_id)

# if thread:
#     st.subheader("📌 Title")
#     st.markdown(f"**{thread['title']}**")

#     # 🪪 Summary Type + Source
#     is_mock = thread.get("is_mock", False)
#     summary_type = "🤖 Simulated Summary" if is_mock else "🔁 Real Summary"
#     summary_color = "#e0e0e0" if is_mock else "#d4edda"
#     source_url = thread.get("source_url", "")
#     source_html = f'<b>📎 Source:</b> <a href="{source_url}" target="_blank">Reddit Thread</a>' if source_url else ""

#     st.markdown(f"""
#         <div style='background-color:{summary_color};padding:10px;border-radius:10px;margin-bottom:10px'>
#             <b>Summary Type:</b> {summary_type}<br>
#             {source_html}
#         </div>
#     """, unsafe_allow_html=True)

#     # 🧠 Summary with styled box + copy button
#     st.subheader("🧠 Summary")
#     summary_text = thread["summary"]

#     st.markdown(
#         f"""
#         <div style='background-color:#f8f9fa; padding:12px; border-radius:8px;
#                     font-family:monospace;  word-wrap:break-word;
#                     border:1px solid #ddd; margin-bottom:10px'>
#             {summary_text.strip()}
#         </div>
#         """, unsafe_allow_html=True
#     )
#     # st.button("📋 Copy Summary", on_click=lambda: st.session_state.update({"summary_copied": True}))
#     # if st.session_state.get("summary_copied"):
#     #     st.success("✅ Summary copied! (Use Ctrl+C if needed)")

#     # 📥 Download JSON (next to summary)
#     if show_download:
#         json_str = json.dumps(thread, indent=2)
#         st.download_button(
#             label="⬇️ Download JSON Result",
#             data=json_str,
#             file_name=f"{thread['thread_id']}.json",
#             mime="application/json"
#         )

#     # 🧪 Fact Checks
#     st.subheader("🔎 Fact Checks")
#     with st.expander("View fact check details", expanded=False):
#         for f in thread["fact_check"]:
#             judgment = f["judgment"]
#             emoji = "🟢" if "Correct" in judgment else "🔴" if "Incorrect" in judgment else "⚪"
#             st.markdown(f"- **Claim:** {f['claim']}  \n  **Judgment:** {emoji} {judgment}")

#     # ⚡ Latency
#     if show_latency:
#         st.subheader("⚡ Latency (s)")
#         latency = thread.get("latency", {})
#         models = thread.get("models_used", {})
#         if latency:
#             for k, v in latency.items():
#                 model_name = models.get(k.lower(), "Unknown")
#                 st.markdown(f"- **{k.capitalize()}**: {v} sec  \n  <span style='color:gray;font-size:small'>Model: `{model_name}`</span>", unsafe_allow_html=True)
#         else:
#             st.info("Latency not recorded for this thread.")

#     # 📊 Evaluation
#     if show_eval:
#         st.subheader("📊 Evaluation")
#         eval_ = thread["evaluation"]
#         if isinstance(eval_, str):
#             eval_ = json.loads(eval_)

#         if isinstance(eval_, dict):
#             with st.expander("View evaluation details", expanded=False):
#                 for k, v in eval_.items():
#                     score = v["score"]
#                     reason = v["reason"]
#                     emoji = "🟢" if score >= 4 else "🟡" if score == 3 else "🔴"
#                     st.markdown(f"- **{k.capitalize()}**: {emoji} {score} — {reason}")
#         else:
#             st.warning(f"Evaluation skipped: {eval_}")

#     st.caption("✅ Powered by OpenRouter LLMs and a modular multi-agent stack.")


import streamlit as st
import json
import streamlit.components.v1 as components
from utils import load_thread_data, get_thread_by_id

st.set_page_config(page_title="ThreadNavigatorAI 2.0", layout="wide")
st.title("🧵 ThreadNavigatorAI 2.0")
st.markdown("A multi-agent Reddit thread analyzer built by Rajesh 💼")

# Sidebar: Display toggles + App Info
st.sidebar.header("⚙️ Display Options")
show_latency = st.sidebar.checkbox("Show Latency", value=True)
show_eval = st.sidebar.checkbox("Show Evaluation", value=True)
show_download = st.sidebar.checkbox("Enable Download", value=True)

st.sidebar.markdown("---")
st.sidebar.markdown("ℹ️ **About This App**\n\nBuilt with a modular multi-agent stack:\n- Semantic summarization\n- Fact-checking\n- LLM-based evaluation\n\nPowered by OpenRouter APIs, fully local UI, and simulated + real threads.")

# Load data
data = load_thread_data()
thread_ids = [t["thread_id"] for t in data]

# Thread selector
selected_id = st.selectbox("🎯 Select a Reddit Thread", thread_ids)
thread = get_thread_by_id(data, selected_id)

# Reset copy flag when thread changes
if "last_selected_id" not in st.session_state:
    st.session_state.last_selected_id = selected_id
if selected_id != st.session_state.last_selected_id:
    st.session_state.summary_copied = False
    st.session_state.last_selected_id = selected_id

if thread:
    st.subheader("📌 Title:")
    st.markdown(f"**{thread['title']}**")

    # Summary type and source
    is_mock = thread.get("is_mock", False)
    summary_type = "🤖 Simulated Summary" if is_mock else "🔁 Real Summary"
    summary_color = "#e0e0e0" if is_mock else "#d4edda"
    source_url = thread.get("source_url", "")
    source_html = f'<b>📎 Source:</b> <a href="{source_url}" target="_blank">Reddit Thread</a>' if source_url else ""

    st.markdown(f"""
        <div style='background-color:{summary_color};padding:10px;border-radius:10px;margin-bottom:10px'>
            <b>Summary Type:</b> {summary_type}<br>
            {source_html}
        </div>
    """, unsafe_allow_html=True)

    with st.expander("💬 View Original Posts", expanded=False):
        for post in thread["posts"]:
            st.markdown(f"- {post}")

    # Define tab labels dynamically
    tab_labels = ["🧠 Summary", "🔎 Fact Checks"]
    if show_latency:
        tab_labels.append("⚡ Latency")
    if show_eval:
        tab_labels.append("📊 Evaluation")

    tabs = st.tabs(tab_labels)

    tab_index = 0  # keep track of which index corresponds to which tab

    # 🧠 Summary Tab
    with tabs[tab_index]:
        st.markdown("### Summary")
        st.markdown(
        f"""
        <div style='background-color:#f8f9fa; padding:12px; border-radius:8px;
                    font-family:monospace;  word-wrap:break-word;
                    border:1px solid #ddd; margin-bottom:10px'>
            {thread["summary"]}
        </div>
        """, unsafe_allow_html=True)

        if show_download:
            json_str = json.dumps(thread, indent=2)
            st.download_button(
                "⬇️ Download JSON Result",
                data=json_str,
                file_name=f"{thread['thread_id']}.json",
                mime="application/json"
            )

    tab_index += 1

    # 🔎 Fact Checks Tab
    with tabs[tab_index]:
        st.markdown("### Fact Checks")
        for f in thread["fact_check"]:
            judgment = f["judgment"]
            emoji = "🟢" if "Correct" in judgment else "🔴" if "Incorrect" in judgment else "⚪"
            st.markdown(f"- **Claim:** {f['claim']}  \n  **Judgment:** {emoji} {judgment}")

    tab_index += 1

    # ⚡ Latency Tab (conditionally present)
    if show_latency:
        with tabs[tab_index]:
            st.markdown("### Agent Latency")
            latency = thread.get("latency", {})
            models = thread.get("models_used", {})
            if latency:
                for k, v in latency.items():
                    model_name = models.get(k.lower(), "Unknown")
                    st.markdown(f"- **{k.capitalize()}**: {v} sec  \n  <span style='color:gray;font-size:small'>Model: `{model_name}`</span>", unsafe_allow_html=True)
            else:
                st.info("Latency not recorded for this thread.")
        tab_index += 1

    # 📊 Evaluation Tab (conditionally present)
    if show_eval:
        with tabs[tab_index]:
            st.markdown("### Evaluation")
            eval_ = thread["evaluation"]
            if isinstance(eval_, str):
                eval_ = json.loads(eval_)
            if isinstance(eval_, dict):
                for k, v in eval_.items():
                    score = v["score"]
                    reason = v["reason"]
                    emoji = "🟢" if score >= 4 else "🟡" if score == 3 else "🔴"
                    st.markdown(f"- **{k.capitalize()}**: {emoji} {score} — {reason}")
            else:
                st.warning(f"Evaluation skipped: {eval_}")

    st.caption("✅ Powered by OpenRouter LLMs and modular multi-agent stack.")
