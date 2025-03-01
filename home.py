import streamlit as st

st.set_page_config(
    page_title="OPIOD Dashboard",
    page_icon="👋",
)

st.title("OPIOID Modeling")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "Overview",
        "Medical Uses",
        "Risk and Concern",
        "Historical Context",
        "Conclusion",
        "Challenges"
    ]
)

# Add content to each tab
with tab1:
    st.header("Overview")
    st.write(
        "Opioids are a class of drugs that include natural, semi-synthetic, and synthetic substances. They interact with opioid receptors in the brain and nervous system to reduce the perception of pain. \
         Common prescription opioids include oxycodone, hydrocodone, morphine, and codeine, while heroin is an example of an illegal opioid. "
    )

with tab2:
    st.header("Medical Uses of Opioids")
    st.write(
        "Medically, opioids are primarily prescribed for pain management, \
         especially in cases of severe or chronic pain. They are also utilized in \
         treating cough and diarrhea under specific circumstances. "
    )

with tab3:
    st.header("Risks and Concerns")
    st.write(
        "While effective for pain relief, opioids carry significant risks, \
            including the potential for dependence and addiction. \
            Their use can lead to tolerance, requiring higher doses to achieve the same effect, \
            and withdrawal symptoms upon cessation. Misuse of opioids has contributed to a widespread public health crisis, \
            with increasing rates of overdose and death. "
    )

with tab4:
    st.header("Historical Context")
    st.write(
        "The use of opioids dates back thousands of years, primarily for pain relief. \
            In modern medicine, their role expanded significantly after the development of inhalational anesthesia \
            in the 19th century, integrating opioids as adjuncts in anesthetic practices."
    )

with tab5:
    st.header("Conclusion")
    st.write(
        "Opioids play a crucial role in managing pain and \
            certain medical conditions. However, due to their high potential \
            for addiction and misuse, it is essential to use them under strict medical supervision, \
            adhering to prescribed dosages and durations. Awareness and education about the benefits \
            and risks of opioids are vital in addressing the ongoing public health challenges associated with their use."
    )

with tab6:
    st.header("Challenges")
    st.write("Inadequate Data")


st.title("Data Sources")

tab1, tab2 = st.tabs(["Population", "Opioid"])

with tab1:
    st.write("Population from 1900-2024")
    st.markdown(
        "[Population](https://www.macrotrends.net/global-metrics/states/nevada/population)"
    )

with tab2:
    st.write(
        "Opioid Overdose Deaths and Opioid Overdose Deaths as a Percent of All Drug Overdose Deaths"
    )
    st.markdown(
        "[Opioid Data](https://www.kff.org/other/state-indicator/opioid-overdose-deaths/?activeTab=graph&currentTimeframe=0&startTimeframe=23&selectedDistributions=opioid-overdose-deaths&selectedRows=%7B%22states%22:%7B%22nevada%22:%7B%7D,%22alabama%22:%7B%7D,%22alaska%22:%7B%7D,%22arizona%22:%7B%7D%7D%7D&sortModel=%7B%22colId%22:%22Location%22,%22sort%22:%22asc%22%7D)"
    )
