import streamlit as st
import pandas as pd
import plotly.express as px
import calendar

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Othaim Successful Coupon Orders Dashboard 2025",
    layout="wide"
)
st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# --- TITLE ---
st.title("📊 Othaim Successful Coupon Orders Dashboard (2025)")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    return pd.read_csv('data/othaim_data_v2.csv')

df = load_data()

# --- SIDEBAR FILTERS ---
with st.sidebar:
    st.header("Filters")
    cities                    = st.multiselect("Select Cities", df['city_name'].unique())
    acquisition               = st.selectbox("Is Acquisition?", ["All", "Yes", "No"])
    acquisition_by_restaurant = st.selectbox("Is Acquisition by Restaurant?", ["All", "Yes", "No"])
    offer_id_input            = st.text_input("Filter by Offer ID")

# --- APPLY FILTERS ---
filtered_df = df.copy()
if cities:
    filtered_df = filtered_df[filtered_df['city_name'].isin(cities)]
if acquisition != "All":
    filtered_df = filtered_df[filtered_df['is_acquisition'] == (acquisition == "Yes")]
if acquisition_by_restaurant != "All":
    filtered_df = filtered_df[
        filtered_df['is_acquision_by_restaurant'] == (acquisition_by_restaurant == "Yes")
    ]
if offer_id_input:
    filtered_df = filtered_df[
        filtered_df['offer_ids'].astype(str).str.contains(offer_id_input, na=False)
    ]

if filtered_df.empty:
    st.warning("⚠️ No matching records found.")
    st.stop()

# --- BASIC KPIs ---
total_orders      = filtered_df['order_id'].nunique()
total_restaurants = 65969
unique_offers     = filtered_df['offer_ids'].nunique()

k1, k2, k3 = st.columns(3)
k1.metric("Total Orders",           f"{total_orders:,}")
k2.metric("Restaurant ID",         str(total_restaurants), delta=None)
k3.metric("Unique Offers Used",     f"{unique_offers:,}")

st.markdown("---")

# --- PARSE DATES ---
filtered_df['created_at'] = pd.to_datetime(filtered_df.get('created_at'), errors='coerce')

# --- DATE SELECTION ---
selected_date = st.date_input("Select Date", value=pd.Timestamp.today().date())
sel = pd.to_datetime(selected_date)

# --- PERIOD BOUNDS ---
start_of_week  = sel - pd.Timedelta(days=(sel.weekday() + 1) % 7)  # Sunday
end_of_week    = start_of_week + pd.Timedelta(days=6)
start_of_month = sel.replace(day=1)
last_day       = calendar.monthrange(sel.year, sel.month)[1]
end_of_month   = sel.replace(day=last_day)
start_of_year  = sel.replace(month=1, day=1)
end_of_year    = sel.replace(month=12, day=31)

# --- FILTER FOR PERIODS ---
df_day   = filtered_df[filtered_df['created_at'].dt.date == sel.date()]
df_week  = filtered_df[
    (filtered_df['created_at'] >= start_of_week) &
    (filtered_df['created_at'] <= end_of_week)
]
df_month = filtered_df[
    (filtered_df['created_at'] >= start_of_month) &
    (filtered_df['created_at'] <= end_of_month)
]
df_year  = filtered_df[
    (filtered_df['created_at'] >= start_of_year) &
    (filtered_df['created_at'] <= end_of_year)
]

# --- PERIOD KPIs ---
d_orders = df_day['order_id'].nunique()
w_orders = df_week['order_id'].nunique()
m_orders = df_month['order_id'].nunique()
y_orders = df_year['order_id'].nunique()

c1, c2, c3, c4 = st.columns(4)
c1.metric("🕒 Orders on Date", f"{d_orders:,}")
c2.metric("📅 Orders in Week",  f"{w_orders:,}")
c3.metric("🗓️ Orders in Month", f"{m_orders:,}")
c4.metric("📈 Orders in Year",  f"{y_orders:,}")

st.markdown("---")

# --- GRANULARITY TABS ---
tabs = st.tabs([
    "Day (Hourly)",
    "Week (Daily)",
    "Month (Daily)",
    "Year (Monthly)"
])

with tabs[0]:
    if not df_day.empty:
        hourly = (
            df_day
            .assign(Hour=df_day['created_at'].dt.hour)
            .groupby('Hour')
            .size()
            .reset_index(name='Orders')
        )
        fig = px.bar(
            hourly, x='Hour', y='Orders',
            title=f"Hourly Successful Coupon Orders on {selected_date}"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No orders on selected date.")

with tabs[1]:
    if not df_week.empty:
        weekly = (
            df_week
            .assign(Date=df_week['created_at'].dt.date)
            .groupby('Date')
            .size()
            .reset_index(name='Orders')
        )
        fig = px.bar(
            weekly, x='Date', y='Orders',
            title=f"Daily Successful Coupon Orders for Week\n{start_of_week.date()} – {end_of_week.date()}"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No orders in selected week.")

with tabs[2]:
    monthly = (
        df_month
        .assign(Date=df_month['created_at'].dt.date)
        .groupby('Date')
        .size()
        .reset_index(name='Orders')
    )
    all_days = pd.date_range(start_of_month, end_of_month).date
    full = (
        pd.DataFrame({'Date': all_days})
        .merge(monthly, on='Date', how='left')
        .fillna(0)
        .assign(Orders=lambda d: d['Orders'].astype(int))
    )
    fig = px.bar(
        full, x='Date', y='Orders',
        title=f"Daily Successful Coupon Orders for {sel.strftime('%B %Y')}"
    )
    st.plotly_chart(fig, use_container_width=True)

with tabs[3]:
    yearly = (
        df_year
        .assign(Month=df_year['created_at'].dt.month)
        .groupby('Month')
        .size()
        .reset_index(name='Orders')
    )
    all_months = pd.DataFrame({'Month': list(range(1, 13))})
    full = (
        all_months
        .merge(yearly, on='Month', how='left')
        .fillna(0)
        .assign(Orders=lambda d: d['Orders'].astype(int))
    )
    full['Month_Name'] = full['Month'].apply(lambda m: calendar.month_name[m])
    fig = px.bar(
        full, x='Month_Name', y='Orders',
        title=f"Monthly Successful Coupon Orders in {sel.year}"
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- CITY CHART ---
city_df = (
    filtered_df['city_name']
      .value_counts()
      .rename_axis('City')
      .reset_index(name='Orders')
)
fig_city = px.bar(
    city_df, x='City', y='Orders',
    title="Successful Coupon Orders per City"
)

# --- TOP 5 OFFERS CHART ---
offers_df = (
    filtered_df['offer_names']
      .value_counts()
      .head(5)
      .rename_axis('Offer Name')
      .reset_index(name='Orders')
)
fig_offers = px.bar(
    offers_df, x='Orders', y='Offer Name',
    orientation='h', title="Top 5 Performing Offers"
)

col7, col8 = st.columns(2)
col7.plotly_chart(fig_city,   use_container_width=True)
col8.plotly_chart(fig_offers, use_container_width=True)

st.markdown("---")

# --- DETAILED DATA TABLE ---
cols = [
    'order_id','offer_ids','restaurant_name_ar','city_name',
    'is_acquisition','is_acquision_by_restaurant','offer_names'
]
mapping = {
    'order_id':                   'Order ID',
    'offer_ids':                  'Offer ID',
    'restaurant_name_ar':         'Restaurant Name (Arabic)',
    'city_name':                  'City',
    'is_acquisition':             'Is Acquisition?',
    'is_acquision_by_restaurant': 'Is Acquisition by Restaurant?',
    'offer_names':                'Offer Names'
}
view = (
    filtered_df[cols]
      .rename(columns=mapping)
      .assign(**{
          'Is Acquisition?':             lambda d: d['Is Acquisition?'].map({0:'No',1:'Yes'}),
          'Is Acquisition by Restaurant?': lambda d: d['Is Acquisition by Restaurant?'].map({0:'No',1:'Yes'})
      })
)
st.dataframe(view, use_container_width=True)
