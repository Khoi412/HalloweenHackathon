# Analytics/streamlit_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import plotly.express as px
import plotly.io as pio

# --- Halloween Plotly Theme ---
halloween_theme = {
    "layout": {
        "paper_bgcolor": "#0d0d0d",      # dark background
        "plot_bgcolor": "#0d0d0d",
        "font": {"color": "#FFA500"},    # pumpkin orange text
        "title": {"x": 0.5, "font": {"size": 22, "color": "#FF7518"}},
        "xaxis": {
            "gridcolor": "#333333",
            "linecolor": "#666666",
            "tickfont": {"color": "#FFA500"}
        },
        "yaxis": {
            "gridcolor": "#333333",
            "linecolor": "#666666",
            "tickfont": {"color": "#FFA500"}
        },
        "legend": {"bgcolor": "rgba(0,0,0,0)", "font": {"color": "#FF7518"}},
        "colorway": ["#FF7518", "#9400D3", "#FF4500", "#DA70D6"],  # orange, violet, red, pink
        "hoverlabel": {"bgcolor": "#222222", "font": {"color": "#FFA500"}},
    }
}

# Apply theme globally
pio.templates["halloween"] = halloween_theme
pio.templates.default = "halloween"

from analytics import (
    load_data,
    summary,
    plot_events_per_city,
    plot_price_per_event,
    plot_event_timeline,
    plot_attendance_per_event,
    plot_average_attendance_per_city,
    plot_price_vs_attendance,
    OUT_DIR,
)

# --- Streamlit Config ---
st.set_page_config(page_title="HauntHub Analytics", layout="wide")
st.title("🎃 HauntHub Halloween Events Analytics Dashboard")

# --- Load Data ---
df = load_data()

# --- Raw data section ---
st.header("🧾 Raw Data Preview")

with st.expander("View Full Dataset"):
    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )
# Optional: let users download the raw dataset

csv_data = df.to_csv(index=False).encode("utf-8")
st.download_button(
        label="⬇️ Download Full Dataset as CSV",
        data=csv_data,
        file_name="haunthub_raw_data.csv",
        mime="text/csv"
    )

# --- Sidebar Filter ---
city_filter = st.sidebar.multiselect(
    "Filter by City:",
    options=sorted(df['city'].unique()),
    default=sorted(df['city'].unique())
)
filtered_df = df[df['city'].isin(city_filter)]

# --- Summary Section ---
st.header("📊 Event Summary")
s = summary(filtered_df)
st.write(pd.DataFrame([s]))

# --- Charts Section ---
st.header("📈 Event Insights")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Events per City")
    plot_events_per_city(filtered_df)
    st.image(str(OUT_DIR / "events_per_city.png"))

    st.subheader("Average Attendance per City")
    plot_average_attendance_per_city(filtered_df)
    st.image(str(OUT_DIR / "average_attendance_per_city.png"))

with col2:
    st.subheader("Price per Event (GBP)")
    plot_price_per_event(filtered_df)
    st.image(str(OUT_DIR / "price_per_event.png"))

    st.subheader("Attendance per Event")
    plot_attendance_per_event(filtered_df)
    st.image(str(OUT_DIR / "attendance_per_event.png"))

# --- Timeline and Correlation ---
st.header("⏰ Timeline & Correlation")

st.subheader("Event Dates Timeline")
plot_event_timeline(filtered_df)
st.image(str(OUT_DIR / "events_timeline.png"))

st.subheader("Price vs Attendance")
plot_price_vs_attendance(filtered_df)
st.image(str(OUT_DIR / "price_vs_attendance.png"))

# --- Footer ---
st.markdown("---")
st.caption("Mock analytics generated for HauntHub — 2025 🎃")


# --- New Plotly Chart Section ---
st.header("✨ Interactive Plotly Chart")

# Interactive Attendance per Event chart
fig = px.bar(
    filtered_df,
    x="title",
    y="attendance",
    color="city",
    title="Interactive Attendance per Event (Plotly)",
    hover_data=["price_gbp"],
    template="halloween"
)

fig.update_traces(
    marker=dict(line=dict(width=1, color="#FF7518")),
    hovertemplate="<b>%{x}</b><br>Attendance: %{y}<br>Price: £%{customdata[0]}<extra></extra>",
    opacity=0.85
)
st.plotly_chart(fig, use_container_width=True)


fig2 = px.scatter(
    filtered_df,
    x="date",
    y="attendance",
    color="city",
    size="price_gbp",
    title="Event Timeline and Attendance (Plotly)",
    template="halloween",
    hover_name="title"
)


fig2.update_traces(
    marker=dict(line=dict(width=1, color="#FF7518")),
    opacity=0.85
)

st.plotly_chart(fig2, use_container_width=True)

