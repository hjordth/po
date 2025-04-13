
import streamlit as st

st.set_page_config(page_title="Mælaborð – Flokkað eftir vídd", layout="wide")
st.title("📂 Velferðarmælaborð – Flokkað eftir vídd")

viddir = {
    "Líðan": {
        "þreyta": {"nafn": "Eru þreytt flesta daga í skólanum", "gildi": 0.20, "markmið": 15},
        "höfuðverkur": {"nafn": "Finna reglulega fyrir höfuðverkur", "gildi": 0.11, "markmið": 10},
        "magaverkur": {"nafn": "Finna reglulega fyrir magaverk", "gildi": 0.09, "markmið": 8}
    },
    "Tengsl": {
        "gagnsemi": {"nafn": "Upplifa sig gagnleg", "gildi": 0.49, "markmið": 60}
    },
    "Heilsa": {
        "heilsa_góð": {"nafn": "Upplifa heilsu sína góða", "gildi": 0.85, "markmið": 90}
    }
}

selected_vidd = st.sidebar.radio("Veldu vídd", list(viddir.keys()))
metrics = viddir[selected_vidd]

st.subheader(f"📌 {selected_vidd}")

for key, info in metrics.items():
    with st.container():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown(f"**{info['nafn']}**")
            st.progress(info['gildi'])
            st.write(f"Núverandi staða: {info['gildi']*100:.0f}%")
        with col2:
            st.metric("🎯 Markmið", f"{info['markmið']}%")
            if key in ["þreyta", "höfuðverkur", "magaverkur"]:
                if info['gildi']*100 <= info['markmið']:
                    st.success("✅ Markmiði náð")
                else:
                    st.warning("❌ Markmiði ekki náð")
            else:
                if info['gildi']*100 >= info['markmið']:
                    st.success("✅ Markmiði náð")
                else:
                    st.warning("❌ Markmiði ekki náð")
