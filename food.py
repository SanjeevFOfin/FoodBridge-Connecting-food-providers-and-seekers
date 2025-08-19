# ==========================================================
# FoodBridge – Connecting food providers and seekers
# Full Streamlit App (Intro + Metrics + Tables + 19 SQL Analyses + Charts)
# ==========================================================

# -------------------------------
# Imports
# -------------------------------
import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(page_title="FoodBridge", layout="wide")

# -------------------------------
# Global Styles (enforce black text + center content + background)
# -------------------------------
st.markdown(
    """
    <style>
        /* Page background image */
        .stApp {
            background: url("https://images.unsplash.com/photo-1504674900247-0877df9cc836") no-repeat center center fixed;
            background-size: cover;
        }

        /* Make most markdown text black */
        .stMarkdown, .stMarkdown p, .stMarkdown span, .stMarkdown li,
        h1, h2, h3, h4, h5, h6 {
            color: black !important;
        }

        /* Center main block and widen */
        .block-container {
            max-width: 1300px;
            padding-top: 1rem;
            padding-bottom: 4rem;
            background: rgba(255, 255, 255, 0.5); /* white overlay for readability */
            border-radius: 12px;
        }

        /* Card look for metric boxes */
        .metric-card {
            text-align:center; 
            color:black; 
            font-size:22px; 
            font-weight:700; 
            background: rgba(255,255,255,0.85);
            padding: 18px 12px; 
            border-radius: 14px; 
            box-shadow: 0 3px 18px rgba(0,0,0,0.08);
            border: 1px solid rgba(0,0,0,0.06);
        }
        .metric-value {
            font-size: 30px; 
            font-weight: 800;
        }

        /* Force all dataframe/table text to white */
        .stDataFrame td, .stDataFrame th,
        .stTable td, .stTable th,
        .dataframe td, .dataframe th,
        div[data-testid="stDataFrame"] div,
        div[data-testid="stTable"] div {
            color: white !important;
        }



        /* Expander label to black and bold */
        div.streamlit-expanderHeader {
            color: black !important;
            font-weight: 800 !important;
            font-size: 20px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# Database Utilities
# ==========================================================
DB_KWARGS = dict(
    host="localhost",
    user="root",
    password="blacky1996",        # Using your direct password as requested
    database="food_wastage"
)

def run_query(query: str) -> pd.DataFrame:
    """Run a SQL query and return a pandas DataFrame."""
    conn = mysql.connector.connect(**DB_KWARGS)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

@st.cache_data(show_spinner=False)
def load_table(table_name: str) -> pd.DataFrame:
    """Load a whole table with caching."""
    return run_query(f"SELECT * FROM {table_name}")

def show_df_white(df: pd.DataFrame):
    """Display a dataframe with white text style."""
    df = df.reset_index(drop=True)        # drop old index
    df.index = df.index + 1               # start numbering from 1
    st.dataframe(
        df.style.set_properties(**{"color": "white"})
    )

# ==========================================================
# Title
# ==========================================================
st.title("FoodBridge – Connecting food providers and seekers")

# ==========================================================
# Project Intro (keep your wording)
# ==========================================================
st.markdown(
    """
    <h3 style='color:black;'>Project Name: FoodBridge – Connecting food providers and seekers</h3>
    <h3 style='color:black;'>Project Type: Data Analysis & Web Application</h3>
    <h3 style='color:black;'>Contribution: Individual (SANJEEV RAJ T)</h3>
    <h3 style='color:black;'>GitHub Link: 
        <a href='https://github.com/SanjeevFOfin/FoodBridge-Connecting-food-providers-and-seekers' 
        style='color:blue;'>My Project Repository</a>
    </h3>
    <h3 style='color:black;'>Project Summary:</h3>
    <p style='color:black; font-size:18px;'>
    This project addresses the issue of food wastage by connecting surplus food providers 
    (restaurants, grocery stores, individuals) with NGOs and people in need. 
    Using SQL for data storage and analysis, and Streamlit for the user interface, 
    the system enables filtering, search, and real-time updates for efficient food redistribution.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================================
# Skills Takeaway (keep your wording)
# ==========================================================
st.markdown(
    """
    <h3 style='color:black;'>Skills Take Away from This Project</h3>
    <p style='color:black; font-size:18px;'>
    <b>Python</b>, <b>SQL</b>, <b>Streamlit</b>, <b>Data Analysis</b>
    </p>
    <p style='color:black; font-size:18px;'>
    <b>Domain:</b> Food Management, Waste Reduction, Social Good
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================================
# Problem Statement (styled, expandable)
# ==========================================================
with st.expander("📌 Problem Statement", expanded=True):
    st.markdown(
        """
        <p style='font-size:20px; line-height:1.6; color:black;'>
        Food wastage is a significant issue, with many households and restaurants discarding surplus food 
        while numerous people struggle with food insecurity.
        This project aims to develop a <b>Local Food Wastage Management System</b> where:
        <ul>
            <li>Restaurants and individuals can list surplus food.</li>
            <li>NGOs or individuals in need can claim the food.</li>
            <li>SQL stores available food details and locations.</li>
            <li>A Streamlit app enables interaction, filtering, CRUD operations, and visualization.</li>
        </ul>
        </p>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# Raw Tables (keep your original tables)
# ==========================================================
st.subheader("📊 Providers Data")
df_providers_all = load_table("providers_data")
show_df_white(df_providers_all)

st.subheader("📊 Receivers Data")
df_receivers_all = load_table("receivers_data")
show_df_white(df_receivers_all)

st.subheader("📊 Claims Data")
df_claims_all = load_table("claims_data")
show_df_white(df_claims_all)

st.subheader("📊 Food Listings Data")
df_food_listings_all = load_table("food_listings_data")
show_df_white(df_food_listings_all)

st.markdown("---")

# ==========================================================
# Advanced SQL Analyses & Visualizations (#1–#19)
# (Nothing removed; everything enhanced and appended)
# ==========================================================
st.markdown("<h2 style='color:black;'>📊 Advanced SQL Analyses & Visualizations</h2>", unsafe_allow_html=True)

# Helper for charts: set black font on every figure
def set_black_font(fig):
    fig.update_layout(font=dict(color="black"))
    return fig

# 1. Providers & Receivers by City (distinct)
st.subheader("1️⃣ How many food providers and receivers are there in each city?")
query1 = """
SELECT City, 
       COUNT(DISTINCT Provider_ID) AS Total_Providers,
       COUNT(DISTINCT Receiver_ID) AS Total_Receivers
FROM (
    SELECT City, Provider_ID, NULL AS Receiver_ID FROM providers_data
    UNION ALL
    SELECT City, NULL AS Provider_ID, Receiver_ID FROM receivers_data
) AS combined
GROUP BY City
ORDER BY City;
"""
df_q1 = run_query(query1)
show_df_white(df_q1)

if not df_q1.empty:
    df_q1_melt = df_q1.melt(id_vars="City", var_name="Type", value_name="Count")
    fig_q1 = px.bar(df_q1_melt, x="City", y="Count", color="Type", barmode="group",
                    title="Providers & Receivers by City")
    st.plotly_chart(set_black_font(fig_q1), use_container_width=True)

# 2. Maximum Providers City
st.subheader("2️⃣ City with Maximum Providers")
query2 = """
SELECT City, COUNT(*) AS Provider_Count
FROM providers_data
GROUP BY City
ORDER BY Provider_Count DESC
LIMIT 1;
"""
df_q2 = run_query(query2)
show_df_white(df_q2)
if not df_q2.empty:
    fig_q2 = px.bar(df_q2, x="City", y="Provider_Count", title="Top City by Provider Count")
    st.plotly_chart(set_black_font(fig_q2), use_container_width=True)

# 3. Maximum Receivers City
st.subheader("3️⃣ City with Maximum Receivers")
query3 = """
SELECT City, COUNT(*) AS Receiver_Count
FROM receivers_data
GROUP BY City
ORDER BY Receiver_Count DESC
LIMIT 1;
"""
df_q3 = run_query(query3)
show_df_white(df_q3)
if not df_q3.empty:
    fig_q3 = px.bar(df_q3, x="City", y="Receiver_Count", title="Top City by Receiver Count")
    st.plotly_chart(set_black_font(fig_q3), use_container_width=True)

# 4. Combined Totals per City
st.subheader("4️⃣ Combined Totals of Providers & Receivers per City")
query4 = """
SELECT 
    p.City,
    COUNT(DISTINCT p.Provider_ID) AS Provider_Count,
    COUNT(DISTINCT r.Receiver_ID) AS Receiver_Count
FROM providers_data p
LEFT JOIN receivers_data r 
    ON p.City = r.City
GROUP BY p.City
ORDER BY Provider_Count DESC, Receiver_Count DESC;
"""
df_q4 = run_query(query4)
show_df_white(df_q4)
if not df_q4.empty:
    df_q4_melt = df_q4.melt(id_vars="City", var_name="Type", value_name="Count")
    fig_q4 = px.bar(df_q4_melt, x="City", y="Count", color="Type", barmode="group",
                    title="Combined Providers & Receivers per City")
    st.plotly_chart(set_black_font(fig_q4), use_container_width=True)

# 5. Max Providers City vs Max Receivers City
st.subheader("5️⃣ Maximum Providers & Receivers — City Comparison")
query5 = """
SELECT 
    p.City AS Max_Providers_City,
    p.Provider_Count,
    r.City AS Max_Receivers_City,
    r.Receiver_Count
FROM 
    (SELECT City, COUNT(*) AS Provider_Count
     FROM providers_data
     GROUP BY City
     ORDER BY Provider_Count DESC
     LIMIT 1) p
CROSS JOIN
    (SELECT City, COUNT(*) AS Receiver_Count
     FROM receivers_data
     GROUP BY City
     ORDER BY Receiver_Count DESC
     LIMIT 1) r;
"""
df_q5 = run_query(query5)
show_df_white(df_q5)
if not df_q5.empty:
    two_rows = pd.DataFrame({
        "City": [df_q5.at[0, "Max_Providers_City"], df_q5.at[0, "Max_Receivers_City"]],
        "Count": [df_q5.at[0, "Provider_Count"], df_q5.at[0, "Receiver_Count"]],
        "Type": ["Max Providers City", "Max Receivers City"]
    })
    fig_q5 = px.bar(two_rows, x="Type", y="Count", color="City",
                    title="Max Providers vs Max Receivers (Cities)")
    st.plotly_chart(set_black_font(fig_q5), use_container_width=True)

# 6. Provider Type with Most Listings
st.subheader("6️⃣ Which type of food provider contributes the most food?")
query6 = """
SELECT Provider_Type, COUNT(*) AS Total_Food_Listings
FROM food_listings_data
GROUP BY Provider_Type
ORDER BY Total_Food_Listings DESC;
"""
df_q6 = run_query(query6)
show_df_white(df_q6)
if not df_q6.empty:
    fig_q6 = px.bar(df_q6, x="Provider_Type", y="Total_Food_Listings",
                    title="Food Listings by Provider Type")
    st.plotly_chart(set_black_font(fig_q6), use_container_width=True)

# 7. Contact Info by City (input)
st.subheader("7️⃣ Contact information of food providers in a specific city")
city_choice = st.text_input("Enter city (default: New Carol):", value="New Carol")
query7 = f"SELECT Name, Contact, Address FROM providers_data WHERE City = '{city_choice}';"
df_q7 = run_query(query7)
show_df_white(df_q7)

# 8. Receivers with Most Claims
st.subheader("8️⃣ Which receivers have claimed the most food?")
query8 = """
SELECT r.Name, COUNT(c.Claim_ID) AS Total_Claims
FROM claims_data c
JOIN receivers_data r ON c.Receiver_ID = r.Receiver_ID
GROUP BY r.Name
ORDER BY Total_Claims DESC;
"""
df_q8 = run_query(query8)
show_df_white(df_q8)
if not df_q8.empty:
    fig_q8 = px.bar(df_q8.head(15), x="Total_Claims", y="Name", orientation="h",
                    title="Top Receivers by Claims (Top 15)")
    fig_q8.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(set_black_font(fig_q8), use_container_width=True)

# 9. Top 10 Receivers by Claims
st.subheader("9️⃣ Top 10 Receivers by Claims")
query9 = """
SELECT r.Name, COUNT(c.Claim_ID) AS Total_Claims
FROM claims_data c
JOIN receivers_data r ON c.Receiver_ID = r.Receiver_ID
GROUP BY r.Name
ORDER BY Total_Claims DESC
LIMIT 10;
"""
df_q9 = run_query(query9)
show_df_white(df_q9)
if not df_q9.empty:
    fig_q9 = px.bar(df_q9, x="Total_Claims", y="Name", orientation="h",
                    title="Top 10 Receivers by Claims")
    fig_q9.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(set_black_font(fig_q9), use_container_width=True)

# 10. Total Quantity Available
st.subheader("🔟 Total Quantity of Food Available")
query10 = "SELECT SUM(Quantity) AS Total_Quantity_Available FROM food_listings_data;"
df_q10 = run_query(query10)
show_df_white(df_q10)
if not df_q10.empty and pd.notna(df_q10.at[0, "Total_Quantity_Available"]):
    st.markdown(
        f"<div style='color:black; font-size:22px; font-weight:700;'>"
        f"Total Quantity Available: {int(df_q10.at[0, 'Total_Quantity_Available'])}</div>",
        unsafe_allow_html=True
    )

# 11. Top 10 Providers by Donated Quantity
st.subheader("1️⃣1️⃣ Top 10 Providers by Total Quantity Donated")
query11 = """
SELECT p.Name AS Provider_Name, 
       SUM(f.Quantity) AS Total_Quantity
FROM food_listings_data f
JOIN providers_data p 
     ON f.Provider_ID = p.Provider_ID
GROUP BY p.Name
ORDER BY Total_Quantity DESC
LIMIT 10;
"""
df_q11 = run_query(query11)
show_df_white(df_q11)
if not df_q11.empty:
    fig_q11 = px.bar(df_q11, x="Total_Quantity", y="Provider_Name", orientation="h",
                     title="Top 10 Providers by Donated Quantity")
    fig_q11.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(set_black_font(fig_q11), use_container_width=True)

# 12. City with Highest Listings (+ Top cities chart)
st.subheader("1️⃣2️⃣ City with Highest Number of Food Listings")
query12 = """
SELECT Location AS City, COUNT(*) AS Total_Listings
FROM food_listings_data
GROUP BY Location
ORDER BY Total_Listings DESC
LIMIT 1;
"""
df_q12 = run_query(query12)
show_df_white(df_q12)

query12_all = """
SELECT Location AS City, COUNT(*) AS Total_Listings
FROM food_listings_data
GROUP BY Location
ORDER BY Total_Listings DESC;
"""
df_q12_all = run_query(query12_all)
if not df_q12_all.empty:
    fig_q12 = px.bar(df_q12_all.head(15), x="City", y="Total_Listings",
                     title="Top Cities by Food Listings (Top 15)")
    st.plotly_chart(set_black_font(fig_q12), use_container_width=True)

# 13. Most Common Food Types
st.subheader("1️⃣3️⃣ Most Commonly Available Food Types")
query13 = """
SELECT Food_Type, COUNT(*) AS Occurrences
FROM food_listings_data
GROUP BY Food_Type
ORDER BY Occurrences DESC;
"""
df_q13 = run_query(query13)
show_df_white(df_q13)
if not df_q13.empty:
    fig_q13 = px.bar(df_q13, x="Food_Type", y="Occurrences",
                     title="Occurrences by Food Type")
    st.plotly_chart(set_black_font(fig_q13), use_container_width=True)

# 14. Claims per Food Item
st.subheader("1️⃣4️⃣ How many food claims have been made for each food item?")
query14 = """
SELECT f.Food_Name, COUNT(c.Claim_ID) AS Total_Claims
FROM claims_data c
JOIN food_listings_data f ON c.Food_ID = f.Food_ID
GROUP BY f.Food_Name
ORDER BY Total_Claims DESC;
"""
df_q14 = run_query(query14)
show_df_white(df_q14)
if not df_q14.empty:
    fig_q14 = px.bar(df_q14.head(20), x="Total_Claims", y="Food_Name", orientation="h",
                     title="Claims per Food Item (Top 20)")
    fig_q14.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(set_black_font(fig_q14), use_container_width=True)

# 15. Provider with Highest Successful Claims (+ top list)
st.subheader("1️⃣5️⃣ Provider with Highest Number of Successful Claims")
query15 = """
SELECT p.Name, COUNT(c.Claim_ID) AS Successful_Claims
FROM claims_data c
JOIN food_listings_data f ON c.Food_ID = f.Food_ID
JOIN providers_data p ON f.Provider_ID = p.Provider_ID
WHERE c.Status = 'Completed'
GROUP BY p.Name
ORDER BY Successful_Claims DESC
LIMIT 1;
"""
df_q15 = run_query(query15)
show_df_white(df_q15)

query15_all = """
SELECT p.Name, COUNT(c.Claim_ID) AS Successful_Claims
FROM claims_data c
JOIN food_listings_data f ON c.Food_ID = f.Food_ID
JOIN providers_data p ON f.Provider_ID = p.Provider_ID
WHERE c.Status = 'Completed'
GROUP BY p.Name
ORDER BY Successful_Claims DESC;
"""
df_q15_all = run_query(query15_all)
if not df_q15_all.empty:
    fig_q15 = px.bar(df_q15_all.head(15), x="Successful_Claims", y="Name", orientation="h",
                     title="Successful Claims by Provider (Top 15)")
    fig_q15.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(set_black_font(fig_q15), use_container_width=True)

# 16. Claims by Status (Percentages)
st.subheader("1️⃣6️⃣ Percentage of Food Claims by Status")
query16 = """
SELECT Status, 
       COUNT(*) AS Count,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims_data), 2) AS Percentage
FROM claims_data
GROUP BY Status;
"""
df_q16 = run_query(query16)
show_df_white(df_q16)
if not df_q16.empty:
    fig_q16 = px.pie(df_q16, names="Status", values="Count", hole=0.35,
                     title="Claims by Status (%)")
    fig_q16.update_traces(textinfo="percent+label")
    st.plotly_chart(set_black_font(fig_q16), use_container_width=True)

# 17. Average Quantity Claimed per Receiver
st.subheader("1️⃣7️⃣ Average Quantity of Food Claimed per Receiver")
query17 = """
SELECT r.Name, ROUND(AVG(f.Quantity), 2) AS Avg_Quantity_Claimed
FROM claims_data c
JOIN receivers_data r ON c.Receiver_ID = r.Receiver_ID
JOIN food_listings_data f ON c.Food_ID = f.Food_ID
GROUP BY r.Name
ORDER BY Avg_Quantity_Claimed DESC;
"""
df_q17 = run_query(query17)
show_df_white(df_q17.head(20))
if not df_q17.empty:
    fig_q17 = px.bar(df_q17.head(20), x="Avg_Quantity_Claimed", y="Name", orientation="h",
                     title="Avg Quantity Claimed per Receiver (Top 20)")
    fig_q17.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(set_black_font(fig_q17), use_container_width=True)

# 18. Most Claimed Meal Type
st.subheader("1️⃣8️⃣ Which Meal Type is Claimed the Most?")
query18 = """
SELECT Meal_Type, COUNT(*) AS Claim_Count
FROM claims_data c
JOIN food_listings_data f ON c.Food_ID = f.Food_ID
GROUP BY Meal_Type
ORDER BY Claim_Count DESC;
"""
df_q18 = run_query(query18)
show_df_white(df_q18)
if not df_q18.empty:
    fig_q18 = px.bar(df_q18, x="Meal_Type", y="Claim_Count",
                     title="Claims by Meal Type")
    st.plotly_chart(set_black_font(fig_q18), use_container_width=True)

# 19. Total Donated Quantity by Provider
st.subheader("1️⃣9️⃣ Total Quantity of Food Donated by Each Provider")
query19 = """
SELECT p.Name, SUM(f.Quantity) AS Total_Donated
FROM food_listings_data f
JOIN providers_data p ON f.Provider_ID = p.Provider_ID
GROUP BY p.Name
ORDER BY Total_Donated DESC;
"""
df_q19 = run_query(query19)
show_df_white(df_q19.head(25))
if not df_q19.empty:
    fig_q19 = px.bar(df_q19.head(25), x="Total_Donated", y="Name", orientation="h",
                     title="Total Quantity Donated by Provider (Top 25)")
    fig_q19.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(set_black_font(fig_q19), use_container_width=True)

st.markdown("---")

# ==========================================================
# 0) Session Data (Temporary Working Copies for Filters/CRUD)
# ==========================================================
if "df_providers" not in st.session_state:
    st.session_state.df_providers = load_table("providers_data")
if "df_receivers" not in st.session_state:
    st.session_state.df_receivers = load_table("receivers_data")
if "df_food" not in st.session_state:
    st.session_state.df_food = load_table("food_listings_data")
if "df_claims" not in st.session_state:
    st.session_state.df_claims = load_table("claims_data")

st.info("All edits you make below are **temporary** (in-memory only) and won't change the MySQL database.")

# -----------------------------
# 1) FILTERS (apply to the previews below only)
# -----------------------------
st.subheader("Filters")

# Derive options safely from available columns
prov_cities = st.session_state.df_providers["City"].dropna().unique().tolist() if "City" in st.session_state.df_providers.columns else []
recv_cities = st.session_state.df_receivers["City"].dropna().unique().tolist() if "City" in st.session_state.df_receivers.columns else []
food_locations = st.session_state.df_food["Location"].dropna().unique().tolist() if "Location" in st.session_state.df_food.columns else []
all_cities = sorted({*prov_cities, *recv_cities, *food_locations})

provider_types = sorted(st.session_state.df_food["Provider_Type"].dropna().unique().tolist()) if "Provider_Type" in st.session_state.df_food.columns else []
food_types = sorted(st.session_state.df_food["Food_Type"].dropna().unique().tolist()) if "Food_Type" in st.session_state.df_food.columns else []
meal_types = sorted(st.session_state.df_food["Meal_Type"].dropna().unique().tolist()) if "Meal_Type" in st.session_state.df_food.columns else []

colf1, colf2, colf3, colf4 = st.columns(4)
with colf1:
    city_filter = st.multiselect("City", options=all_cities)
with colf2:
    provider_type_filter = st.multiselect("Provider Type", options=provider_types)
with colf3:
    food_type_filter = st.multiselect("Food Type", options=food_types)
with colf4:
    meal_type_filter = st.multiselect("Meal Type", options=meal_types)

# Apply filters to copies (for preview only)
prov_preview = st.session_state.df_providers.copy()
recv_preview = st.session_state.df_receivers.copy()
food_preview = st.session_state.df_food.copy()

if city_filter:
    if "City" in prov_preview.columns:
        prov_preview = prov_preview[prov_preview["City"].isin(city_filter)]
    if "City" in recv_preview.columns:
        recv_preview = recv_preview[recv_preview["City"].isin(city_filter)]
    if "Location" in food_preview.columns:
        food_preview = food_preview[food_preview["Location"].isin(city_filter)]

if provider_type_filter and "Provider_Type" in food_preview.columns:
    food_preview = food_preview[food_preview["Provider_Type"].isin(provider_type_filter)]
if food_type_filter and "Food_Type" in food_preview.columns:
    food_preview = food_preview[food_preview["Food_Type"].isin(food_type_filter)]
if meal_type_filter and "Meal_Type" in food_preview.columns:
    food_preview = food_preview[food_preview["Meal_Type"].isin(meal_type_filter)]

st.caption("Filtered previews (not affecting the SQL queries above)")
pt1, pt2, pt3 = st.tabs(["Providers", "Receivers", "Food Listings"])
with pt1:
    st.dataframe(prov_preview, use_container_width=True)
with pt2:
    st.dataframe(recv_preview, use_container_width=True)
with pt3:
    st.dataframe(food_preview, use_container_width=True)

st.divider()

# -----------------------------
# 2) CRUD (Temporary, Session-Only)
# -----------------------------
st.subheader("Data Management (Temporary CRUD)")
choice_table = st.selectbox("Choose table", ["providers_data", "receivers_data", "food_listings_data", "claims_data"])
choice_op = st.radio("Operation", ["Add", "Update", "Delete"], horizontal=True)

# Utility to get current df ref
DF_MAP = {
    "providers_data": "df_providers",
    "receivers_data": "df_receivers",
    "food_listings_data": "df_food",
    "claims_data": "df_claims",
}
cur_key = DF_MAP[choice_table]
cdf = st.session_state[cur_key]

# Identify ID column heuristically
id_col_candidates = [c for c in cdf.columns if c.lower().endswith("_id")]
id_col = id_col_candidates[0] if id_col_candidates else (cdf.columns[0] if len(cdf.columns) else None)

if choice_op == "Add":
    with st.form("add_form"):
        st.write(f"Add new row to **{choice_table}**")
        new_row = {}
        for col in cdf.columns:
            if col == id_col:
                # Auto-increment id in-session
                try:
                    next_id = (pd.to_numeric(cdf[col], errors='coerce').max() or 0) + 1
                except Exception:
                    next_id = len(cdf) + 1
                st.text_input(col, value=str(int(next_id)), disabled=True, key=f"add_{col}")
                new_row[col] = int(next_id)
            else:
                default_val = "" if cdf[col].dtype == object else 0
                val = st.text_input(col, value=str(default_val), key=f"add_{col}")
                new_row[col] = val
        submitted = st.form_submit_button("Add")
        if submitted:
            st.session_state[cur_key] = pd.concat([cdf, pd.DataFrame([new_row])], ignore_index=True)
            st.success("Row added (session only).")

elif choice_op == "Update":
    if id_col is None:
        st.warning("No ID column detected; cannot update.")
    else:
        ids = cdf[id_col].astype(str).tolist()
        sel_id = st.selectbox("Select ID to update", ids)
        row = cdf[cdf[id_col].astype(str) == sel_id].iloc[0]
        with st.form("upd_form"):
            st.write(f"Update row {sel_id} in **{choice_table}**")
            updated = {}
            for col in cdf.columns:
                val = st.text_input(col, value=str(row[col]), key=f"upd_{col}")
                updated[col] = val
            submitted = st.form_submit_button("Save Changes")
            if submitted:
                idx = cdf[cdf[id_col].astype(str) == sel_id].index
                for k, v in updated.items():
                    st.session_state[cur_key].loc[idx, k] = v
                st.success("Row updated (session only).")

else:  # Delete
    if id_col is None:
        st.warning("No ID column detected; cannot delete.")
    else:
        ids = cdf[id_col].astype(str).tolist()
        del_id = st.selectbox("Select ID to delete", ids)
        if st.button("Delete Row"):
            st.session_state[cur_key] = cdf[cdf[id_col].astype(str) != del_id].reset_index(drop=True)
            st.success("Row deleted (session only).")

st.caption("Below are your in-session tables after CRUD edits (refresh clears changes unless you cache/save them).")
ct1, ct2, ct3, ct4 = st.tabs(["providers_data", "receivers_data", "food_listings_data", "claims_data"])
with ct1: st.dataframe(st.session_state.df_providers, use_container_width=True)
with ct2: st.dataframe(st.session_state.df_receivers, use_container_width=True)
with ct3: st.dataframe(st.session_state.df_food, use_container_width=True)
with ct4: st.dataframe(st.session_state.df_claims, use_container_width=True)

st.divider()

# -----------------------------
# 3) Key Insights
# -----------------------------
total_providers = run_query("SELECT COUNT(DISTINCT Provider_ID) AS c FROM providers_data;")['c'][0]
total_receivers = run_query("SELECT COUNT(DISTINCT Receiver_ID) AS c FROM receivers_data;")['c'][0]
most_claimed_food = run_query("""
    SELECT Food_Name 
    FROM (
        SELECT Food_Name, COUNT(*) AS cnt
        FROM food_listings_data
        GROUP BY Food_Name
        ORDER BY cnt DESC
        LIMIT 1
    ) t;
""")['Food_Name'][0]

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
        <div style='text-align:center; color:black; font-size:24px; font-weight:bold;'>
            Total Providers<br><span style='font-size:30px;'>{total_providers}</span>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div style='text-align:center; color:black; font-size:24px; font-weight:bold;'>
            Total Receivers<br><span style='font-size:30px;'>{total_receivers}</span>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
        <div style='text-align:center; color:black; font-size:24px; font-weight:bold;'>
            Most Claimed Food<br><span style='font-size:30px;'>{most_claimed_food}</span>
        </div>
    """, unsafe_allow_html=True)


# ==========================================================
# Key Problems, Solutions & Conclusion (styled black)
# ==========================================================
st.markdown("<h2 style='color:black; font-weight:bold;'>🔑 Key Problems, Solutions & Insights</h2>", unsafe_allow_html=True)

# Problem 1
st.markdown("<h3 style='color:black;'>1️⃣ Problem: Food Wastage vs Food Insecurity</h3>", unsafe_allow_html=True)
st.markdown("""
<p style='color:black; font-size:22px;'>
- <b style='font-size:24px;'>Problem:</b> Large amounts of surplus food discarded by restaurants & households while many go hungry.<br>
- <b style='font-size:24px;'>Solution:</b> FoodBridge connects providers (restaurants, grocery stores, individuals) with receivers (NGOs, needy people) using real-time listings & claims.
</p>
""", unsafe_allow_html=True)

# Problem 2
st.markdown("<h3 style='color:black;'>2️⃣ Problem: Unequal Distribution Across Cities</h3>", unsafe_allow_html=True)
st.markdown("""
<p style='color:black; font-size:22px;'>
- <b style='font-size:24px;'>Problem:</b> Some cities have more providers but fewer receivers, while others show the opposite.<br>
- <b style='font-size:24px;'>Solution:</b> SQL analysis identifies mismatches so NGOs can focus efforts in underserved regions.
</p>
""", unsafe_allow_html=True)

# Problem 3
st.markdown("<h3 style='color:black;'>3️⃣ Problem: Provider Engagement</h3>", unsafe_allow_html=True)
st.markdown("""
<p style='color:black; font-size:22px;'>
- <b style='font-size:24px;'>Problem:</b> Few provider types contribute the majority of food.<br>
- <b style='font-size:24px;'>Solution:</b> Identify top provider types (restaurants, grocery stores) & encourage underperforming ones.
</p>
""", unsafe_allow_html=True)

# Problem 4 + live table (claims status distribution)
st.markdown("<h3 style='color:black;'>4️⃣ Problem: Claim Success & Tracking</h3>", unsafe_allow_html=True)
st.markdown("""
<p style='color:black; font-size:22px;'>
- <b style='font-size:24px;'>Problem:</b> Not all claims succeed (pending/cancelled due to logistics).<br>
- <b style='font-size:24px;'>Solution:</b> Monitor claim status, success rates & optimize delivery models.
</p>
""", unsafe_allow_html=True)

query_status = """
SELECT Status, COUNT(*) AS Count,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims_data), 2) AS Percentage
FROM claims_data
GROUP BY Status;
"""
df_status = run_query(query_status)
show_df_white(df_status)
if not df_status.empty:
    fig_status = px.pie(df_status, names="Status", values="Count", hole=0.35, title="Live Claim Status Mix")
    fig_status.update_traces(textinfo="percent+label")
    st.plotly_chart(set_black_font(fig_status), use_container_width=True)

# Conclusion
st.markdown("<h2 style='color:black; font-weight:bold;'>✅ Conclusion</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='color:black; font-size:20px;'>
This project shows how <b>SQL + Streamlit</b> can solve real-world challenges:<br>
- Efficient redistribution of surplus food<br>
- Data-driven insights on providers, receivers, and claims<br>
- Reduced wastage and improved food security
</p>
<p style='color:black; font-size:20px;'>
<b>Future Scope:</b><br>
1. Automate notifications (SMS/Email) to NGOs for new listings.<br>
2. Build a recommendation engine for receivers based on location & food type.<br>
3. Expand system to multiple regions with scalability in mind.
</p>
""", unsafe_allow_html=True)

# EOF
