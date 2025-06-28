import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(page_title="EcoLens: Pollution & Heritage Trends", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
        .insight-box {
            background-color: #f9f9f9;
            border-left: 5px solid #3f51b5;
            padding: 1em;
            border-radius: 8px;
            margin-bottom: 1em;
            color: black;  /* 👈 This sets the text color */
        }
    </style>
""", unsafe_allow_html=True)


def render():
    st.title("🌿 EcoLens: Unveiling the Link Between Air Quality & Heritage Tourism")

    # Load data
    df = pd.read_csv("data/airQualityindex.csv")
    df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')
    df = df.dropna(subset=["pollutant_avg"])
    
    # Extract year and month for filtering
    df["year"] = df["last_update"].dt.year
    df["month"] = df["last_update"].dt.month_name()

    # --- Sidebar Filters ---
    st.sidebar.header("🔎 Filter Data")
    selected_year = st.sidebar.selectbox("Select Year", sorted(df["year"].dropna().unique()), index=0)
    selected_month = st.sidebar.selectbox("Select Month", sorted(df["month"].dropna().unique()), index=0)
    selected_pollutant = st.sidebar.selectbox("Select Pollutant Type", sorted(df["pollutant_id"].unique()), index=0)

    # Filtered DataFrame
    filtered_df = df[
        (df["year"] == selected_year) &
        (df["month"] == selected_month) &
        (df["pollutant_id"] == selected_pollutant)
    ]

    # --- 📌 Key Observations ---
    st.markdown("## 📌 Heritage Airwatch Highlights")
    most_polluted_city = filtered_df.groupby("city")["pollutant_avg"].mean().idxmax()
    highest_pollution = filtered_df.groupby("city")["pollutant_avg"].mean().max()
    least_polluted_city = filtered_df.groupby("city")["pollutant_avg"].mean().idxmin()
    lowest_pollution = filtered_df.groupby("city")["pollutant_avg"].mean().min()

    st.markdown(f"""
        <div class='insight-box'>
            🌆 <b>Highest AQI Cultural Hub:</b> {most_polluted_city} — <b>{highest_pollution:.2f}</b><br>
            🏕️ <b>Cleanest Heritage Site:</b> {least_polluted_city} — <b>{lowest_pollution:.2f}</b><br><br>
            📈 <b>Trend:</b> Popular tourist cities tend to record higher AQI values.<br>
            🍃 <b>Insight:</b> Underrated places offer cleaner air & sustainable exploration.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    # --- 📊 Avg AQI by City ---
    with col1:
        st.subheader("📊 Mean AQI by City")
        grouped = filtered_df.groupby('city')['pollutant_avg'].mean().reset_index()
        fig1 = px.bar(
            grouped.sort_values(by="pollutant_avg", ascending=False),
            x='pollutant_avg', y='city',
            color='pollutant_avg', orientation='h',
            color_continuous_scale='Reds',
            labels={'pollutant_avg': 'Average AQI', 'city': 'City'}
        )
        st.plotly_chart(fig1, use_container_width=True)

    # --- 🌬 Pollutant Spread ---
    with col2:
        st.subheader("🌬 Pollution Type Distribution")
        pollutant_summary = filtered_df.groupby(['city', 'pollutant_id'])['pollutant_avg'].mean().reset_index()
        fig2 = px.bar(
            pollutant_summary, x='pollutant_avg', y='city',
            color='pollutant_id', barmode='group',
            title='Pollutant Types Across Cities',
            orientation='h',
            labels={'pollutant_avg': 'AQI', 'city': 'City', 'pollutant_id': 'Pollutant'}
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # --- ⬇️ Download Option ---
    st.subheader("⬇️ Download Filtered Data")
    st.download_button(
        label="Download CSV",
        data=filtered_df.to_csv(index=False).encode('utf-8'),
        file_name=f"AQI_Data_{selected_year}_{selected_month}_{selected_pollutant}.csv",
        mime='text/csv'
    )

    st.caption("🗂 Data Source: AQI Monitoring Dataset | Powered by Plotly & Streamlit")

if __name__ == "__main__":
    render()
