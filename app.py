import streamlit as st

st.set_page_config(
    page_title="AI Insurance Claim Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AI Insurance Claim Assistant")
st.caption("AI-powered educational assistance for healthcare insurance claims")

st.info(
    "This application is for informational and educational purposes only. "
    "Always confirm requirements with your insurance provider or hospital."
)

# Built-in knowledge base — no external dataset required
KB = {
    "cashless": {
        "title": "Cashless Hospitalization Claim",
        "answer": """
### Typical documents
- Health insurance card / policy details
- Government ID such as Aadhaar
- Doctor's prescription and admission advice
- Medical reports and investigation reports
- Hospital admission and discharge documents
- Bills and receipts, where applicable

### General process
1. Confirm that the hospital is in the insurer/TPA network.
2. Contact the insurance desk or TPA at the hospital.
3. Submit the pre-authorization request.
4. Provide the requested medical documents.
5. Wait for insurer/TPA approval.
6. At discharge, complete the hospital and insurance formalities.

Requirements can vary by policy and insurer.
"""
    },
    "reimbursement": {
        "title": "Reimbursement Claim",
        "answer": """
### Commonly requested documents
- Claim form
- Insurance policy/card details
- Government ID
- Original medical bills and receipts
- Prescriptions
- Diagnostic reports
- Discharge summary
- Payment proof, where required
- Bank account details/cancelled cheque, where required

### General process
1. Receive treatment and pay the eligible expenses.
2. Collect original bills and medical records.
3. Complete the insurer's reimbursement claim form.
4. Submit the documents within the policy's stated time limit.
5. The insurer reviews the claim.
6. Approved eligible expenses are reimbursed according to the policy.
"""
    },
    "hospitalization": {
        "title": "Hospitalization Claim Guidance",
        "answer": """
For hospitalization, keep your policy details and insurance card ready.
Inform the hospital insurance desk as early as possible and ask whether
cashless treatment is available.

Keep copies of:
- Admission records
- Doctor's prescriptions
- Medical reports
- Bills and receipts
- Discharge summary
- Claim/pre-authorization forms
"""
    },
    "processing": {
        "title": "Claim Processing",
        "answer": """
Claim processing time depends on the insurer, claim type, completeness of
documents, and policy terms.

To reduce delays:
- Submit complete and readable documents.
- Provide accurate policy information.
- Respond quickly to clarification requests.
- Keep claim/reference numbers.
- Contact the insurer/TPA for the current status and expected timeline.
"""
    }
}

def answer_question(q):
    q = q.lower()
    if any(x in q for x in ["cashless", "network hospital", "pre authorization", "pre-authorization"]):
        return KB["cashless"]["answer"]
    if any(x in q for x in ["reimbursement", "refund", "paid hospital"]):
        return KB["reimbursement"]["answer"]
    if any(x in q for x in ["hospital", "admission", "discharge"]):
        return KB["hospitalization"]["answer"]
    if any(x in q for x in ["time", "processing", "how long", "delay", "status"]):
        return KB["processing"]["answer"]
    return """
### General Insurance Guidance
I can help with:
- Cashless claims
- Reimbursement claims
- Hospitalization
- Claim documents
- Claim processing
- General insurance procedures

Try asking: **"What documents are required for a cashless claim?"**
"""

st.sidebar.header("📌 Navigation")
page = st.sidebar.radio(
    "Choose a feature",
    ["AI Chatbot", "Document Checklist", "Claim Guide", "About"]
)

if page == "AI Chatbot":
    st.header("🤖 Insurance AI Chatbot")
    st.write("Ask a question in natural language.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input(
        "Example: What documents are needed for reimbursement?"
    )

    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        response = answer_question(question)
        st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("user"):
            st.markdown(question)
        with st.chat_message("assistant"):
            st.markdown(response)

elif page == "Document Checklist":
    st.header("📋 Claim Document Checklist")
    claim_type = st.selectbox(
        "Select claim type",
        ["Cashless Hospitalization", "Reimbursement", "General Hospitalization"]
    )

    if claim_type == "Cashless Hospitalization":
        docs = [
            "☐ Health insurance card / policy details",
            "☐ Government ID",
            "☐ Doctor's prescription / admission advice",
            "☐ Medical reports",
            "☐ Hospital admission documents",
            "☐ Pre-authorization form",
            "☐ Discharge documents",
            "☐ Bills/receipts as requested"
        ]
    elif claim_type == "Reimbursement":
        docs = [
            "☐ Completed claim form",
            "☐ Health insurance card / policy details",
            "☐ Government ID",
            "☐ Original medical bills",
            "☐ Payment receipts",
            "☐ Doctor's prescriptions",
            "☐ Diagnostic reports",
            "☐ Discharge summary",
            "☐ Bank details/cancelled cheque if required"
        ]
    else:
        docs = [
            "☐ Insurance policy/card",
            "☐ Government ID",
            "☐ Doctor's prescription",
            "☐ Medical reports",
            "☐ Hospital bills",
            "☐ Discharge summary",
            "☐ Claim form"
        ]

    for doc in docs:
        st.write(doc)

elif page == "Claim Guide":
    st.header("📝 Insurance Claim Guide")

    tabs = st.tabs([
        "Cashless",
        "Reimbursement",
        "Hospitalization",
        "Processing"
    ])

    for tab, key in zip(tabs, ["cashless", "reimbursement", "hospitalization", "processing"]):
        with tab:
            st.subheader(KB[key]["title"])
            st.markdown(KB[key]["answer"])

elif page == "About":
    st.header("ℹ️ About the Project")
    st.markdown("""
**AI Insurance Claim Assistant** is a Streamlit-based healthcare insurance
assistance application.

### Features
- AI-style insurance chatbot
- Real-time response generation from a built-in knowledge base
- Document checklist generator
- Cashless claim guidance
- Reimbursement claim guidance
- Hospitalization guidance
- Claim processing information
- Simple and user-friendly dashboard

### Technology
- Python
- Streamlit

### Future enhancements
- Connect to a Generative AI API
- Upload and analyze claim documents
- Claim status tracking
- Chat history management
- Voice-based insurance assistance
- Personalized policy guidance
""")

st.divider()
st.caption("AI Insurance Claim Assistant • Educational use only")
