# # # # import streamlit as st
# # # # import pandas as pd
# # # # import plotly.express as px

# # # # # Load data
# # # # df = pd.read_csv('data/othaim_data.csv')

# # # # st.set_page_config(page_title="Othaim Orders Dashboard", layout="wide")
# # # # st.title("📊 Othaim Orders Dashboard")

# # # # # Sidebar filters
# # # # with st.sidebar:
# # # #     st.header("Filters")
# # # #     cities = st.multiselect("Select Cities", options=df['city_name'].unique())
# # # #     restaurants = st.multiselect("Select Restaurants", options=df['restaurant_name_ar'].unique())
# # # #     acquisition = st.selectbox("Is Acquisition?", options=["All", "Yes", "No"])

# # # # # Apply filters
# # # # filtered_df = df.copy()

# # # # if cities:
# # # #     filtered_df = filtered_df[filtered_df['city_name'].isin(cities)]

# # # # if restaurants:
# # # #     filtered_df = filtered_df[filtered_df['restaurant_name_ar'].isin(restaurants)]

# # # # if acquisition != "All":
# # # #     acquisition_bool = True if acquisition == "Yes" else False
# # # #     filtered_df = filtered_df[filtered_df['is_acquisition'] == acquisition_bool]

# # # # # Top KPIs
# # # # total_orders = filtered_df['order_id'].nunique()
# # # # total_restaurants = filtered_df['restaurant_id'].nunique()
# # # # unique_offers = filtered_df['offer_ids'].nunique()

# # # # col1, col2, col3 = st.columns(3)
# # # # col1.metric("Total Orders", f"{total_orders:,}")
# # # # col2.metric("Unique Restaurants", f"{total_restaurants:,}")
# # # # col3.metric("Unique Offers Used", f"{unique_offers:,}")

# # # # st.markdown("---")

# # # # # Orders by City
# # # # orders_by_city = filtered_df['city_name'].value_counts().reset_index()
# # # # orders_by_city.columns = ['City', 'Orders']
# # # # fig_city = px.bar(orders_by_city, x='City', y='Orders', title="Orders per City", height=400)

# # # # # Top 10 Restaurants
# # # # top_restaurants = filtered_df['restaurant_name_ar'].value_counts().head(10).reset_index()
# # # # top_restaurants.columns = ['Restaurant', 'Orders']
# # # # fig_restaurant = px.bar(top_restaurants, x='Orders', y='Restaurant', title="Top 10 Restaurants", orientation='h', height=400)

# # # # # Offer Type Distribution
# # # # fig_offer = px.pie(filtered_df, names='rdf_offer_type', title="Offer Types Distribution", hole=0.5)

# # # # # Layout plots
# # # # col4, col5 = st.columns(2)
# # # # col4.plotly_chart(fig_city, use_container_width=True)
# # # # col5.plotly_chart(fig_restaurant, use_container_width=True)

# # # # st.plotly_chart(fig_offer, use_container_width=True)

# # # # # Detailed Table
# # # # st.markdown("### 📋 Detailed Data View")
# # # # st.dataframe(filtered_df, use_container_width=True)


# # # import streamlit as st
# # # import pandas as pd
# # # import plotly.express as px

# # # # Load data
# # # df = pd.read_csv('data/othaim_data.csv')

# # # st.set_page_config(page_title="Othaim Orders Dashboard", layout="wide")
# # # st.title("📊 Othaim Orders Dashboard")

# # # # Sidebar filters
# # # with st.sidebar:
# # #     st.header("Filters")
# # #     cities = st.multiselect("Select Cities", options=df['city_name'].unique())
# # #     restaurants = st.multiselect("Select Restaurants", options=df['restaurant_name_ar'].unique())
# # #     acquisition = st.selectbox("Is Acquisition?", options=["All", "Yes", "No"])
# # #     offer_id_input = st.text_input("Filter by Offer ID")

# # # # Apply filters
# # # filtered_df = df.copy()

# # # if cities:
# # #     filtered_df = filtered_df[filtered_df['city_name'].isin(cities)]

# # # if restaurants:
# # #     filtered_df = filtered_df[filtered_df['restaurant_name_ar'].isin(restaurants)]

# # # if acquisition != "All":
# # #     acquisition_bool = True if acquisition == "Yes" else False
# # #     filtered_df = filtered_df[filtered_df['is_acquisition'] == acquisition_bool]

# # # if offer_id_input:
# # #     filtered_df = filtered_df[filtered_df['offer_ids'].astype(str).str.contains(offer_id_input)]

# # # # Top KPIs
# # # total_orders = filtered_df['order_id'].nunique()
# # # total_restaurants = filtered_df['restaurant_id'].nunique()
# # # unique_offers = filtered_df['offer_ids'].nunique()

# # # col1, col2, col3 = st.columns(3)
# # # col1.metric("Total Orders", f"{total_orders:,}")
# # # col2.metric("Unique Restaurants", f"{total_restaurants:,}")
# # # col3.metric("Unique Offers Used", f"{unique_offers:,}")

# # # st.markdown("---")

# # # # Orders by City
# # # orders_by_city = filtered_df['city_name'].value_counts().reset_index()
# # # orders_by_city.columns = ['City', 'Orders']
# # # fig_city = px.bar(orders_by_city, x='City', y='Orders', title="Orders per City", height=400)

# # # # Top 10 Restaurants
# # # top_restaurants = filtered_df['restaurant_name_ar'].value_counts().head(10).reset_index()
# # # top_restaurants.columns = ['Restaurant', 'Orders']
# # # fig_restaurant = px.bar(top_restaurants, x='Orders', y='Restaurant', title="Top 10 Restaurants", orientation='h', height=400)

# # # # Offer Type Distribution
# # # fig_offer = px.pie(filtered_df, names='rdf_offer_type', title="Offer Types Distribution", hole=0.5)

# # # # Layout plots
# # # col4, col5 = st.columns(2)
# # # col4.plotly_chart(fig_city, use_container_width=True)
# # # col5.plotly_chart(fig_restaurant, use_container_width=True)

# # # st.plotly_chart(fig_offer, use_container_width=True)

# # # # Detailed Table
# # # st.markdown("### 📋 Detailed Data View")
# # # st.dataframe(filtered_df, use_container_width=True)

# # import streamlit as st
# # import pandas as pd
# # import plotly.express as px

# # # Load data
# # df = pd.read_csv('data/othaim_data.csv')

# # st.set_page_config(page_title="Othaim Orders Dashboard 2025", layout="wide")
# # st.title("📊 Othaim Orders Dashboard (2025)")

# # # Sidebar filters
# # with st.sidebar:
# #     st.header("Filters")
# #     cities = st.multiselect("Select Cities", options=df['city_name'].unique())
# #     acquisition = st.selectbox("Is Acquisition?", options=["All", "Yes", "No"])
# #     offer_id_input = st.text_input("Filter by Offer ID")

# # # Apply filters
# # filtered_df = df.copy()

# # if cities:
# #     filtered_df = filtered_df[filtered_df['city_name'].isin(cities)]

# # if acquisition != "All":
# #     acquisition_bool = True if acquisition == "Yes" else False
# #     filtered_df = filtered_df[filtered_df['is_acquisition'] == acquisition_bool]

# # if offer_id_input:
# #     filtered_df = filtered_df[filtered_df['offer_ids'].astype(str).str.contains(offer_id_input)]

# # # Top KPIs
# # total_orders = filtered_df['order_id'].nunique()
# # total_restaurants = filtered_df['restaurant_id'].nunique()
# # unique_offers = filtered_df['offer_ids'].nunique()

# # col1, col2, col3 = st.columns(3)
# # col1.metric("Total Orders", f"{total_orders:,}")
# # col2.metric("Unique Restaurants", f"{total_restaurants:,}")
# # col3.metric("Unique Offers Used", f"{unique_offers:,}")

# # st.markdown("---")

# # # Orders by City
# # orders_by_city = filtered_df['city_name'].value_counts().reset_index()
# # orders_by_city.columns = ['City', 'Orders']
# # fig_city = px.bar(orders_by_city, x='City', y='Orders', title="Orders per City", height=400)

# # # Top 10 Offer Names
# # top_offers = filtered_df['offer_names'].value_counts().head(10).reset_index()
# # top_offers.columns = ['Offer Name', 'Orders']
# # fig_offers = px.bar(top_offers, x='Orders', y='Offer Name', title="Top 10 Performing Offers", orientation='h', height=400)

# # # Offer Type Distribution
# # fig_offer = px.pie(filtered_df, names='rdf_offer_type', title="Offer Types Distribution", hole=0.5)

# # # Layout plots
# # col4, col5 = st.columns(2)
# # col4.plotly_chart(fig_city, use_container_width=True)
# # col5.plotly_chart(fig_offers, use_container_width=True)

# # st.plotly_chart(fig_offer, use_container_width=True)

# # # Detailed Table
# # st.markdown("### 📋 Detailed Data View")
# # st.dataframe(filtered_df, use_container_width=True)

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Load data
# df = pd.read_csv('data/othaim_data.csv')

# st.set_page_config(page_title="Othaim Orders Dashboard 2025", layout="wide")
# st.title("📊 Othaim Orders Dashboard (2025)")

# # Sidebar filters
# with st.sidebar:
#     st.header("Filters")
#     cities = st.multiselect("Select Cities", options=df['city_name'].unique())
#     acquisition = st.selectbox("Is Acquisition?", options=["All", "Yes", "No"])
#     acquisition_by_restaurant = st.selectbox("Is Acquisition by Restaurant?", options=["All", "Yes", "No"])
#     offer_id_input = st.text_input("Filter by Offer ID")

# # Apply filters
# filtered_df = df.copy()

# if cities:
#     filtered_df = filtered_df[filtered_df['city_name'].isin(cities)]

# if acquisition != "All":
#     acquisition_bool = True if acquisition == "Yes" else False
#     filtered_df = filtered_df[filtered_df['is_acquisition'] == acquisition_bool]

# if acquisition_by_restaurant != "All":
#     acquisition_restaurant_bool = True if acquisition_by_restaurant == "Yes" else False
#     filtered_df = filtered_df[filtered_df['is_acquision_by_restaurant'] == acquisition_restaurant_bool]

# if offer_id_input:
#     filtered_df = filtered_df[filtered_df['offer_ids'].astype(str).str.contains(offer_id_input)]

# # Top KPIs
# total_orders = filtered_df['order_id'].nunique()
# total_restaurants = filtered_df['restaurant_id'].nunique()
# unique_offers = filtered_df['offer_ids'].nunique()

# col1, col2, col3 = st.columns(3)
# col1.metric("Total Orders", f"{total_orders:,}")
# col2.metric("Unique Restaurants", f"{total_restaurants:,}")
# col3.metric("Unique Offers Used", f"{unique_offers:,}")

# st.markdown("---")

# # Orders by City
# orders_by_city = filtered_df['city_name'].value_counts().reset_index()
# orders_by_city.columns = ['City', 'Orders']
# fig_city = px.bar(orders_by_city, x='City', y='Orders', title="Orders per City", height=400)

# # Top 10 Offer Names
# top_offers = filtered_df['offer_names'].value_counts().head(10).reset_index()
# top_offers.columns = ['Offer Name', 'Orders']
# fig_offers = px.bar(top_offers, x='Orders', y='Offer Name', title="Top 10 Performing Offers", orientation='h', height=400)

# # Offer Type Distribution
# fig_offer = px.pie(filtered_df, names='rdf_offer_type', title="Offer Types Distribution", hole=0.5)

# # Layout plots
# col4, col5 = st.columns(2)
# col4.plotly_chart(fig_city, use_container_width=True)
# col5.plotly_chart(fig_offers, use_container_width=True)

# st.plotly_chart(fig_offer, use_container_width=True)

# # Detailed Table
# st.markdown("### 📋 Detailed Data View")

# # Select only important columns
# columns_to_show = [
#     'order_id',
#     'restaurant_name_ar',
#     'city_name',
#     'is_acquisition',
#     'is_acquision_by_restaurant',
#     'rdf_offer_applied',
#     'rdf_offer_type',
#     'offer_names'
# ]

# # Rename columns for readability
# rename_mapping = {
#     'order_id': 'Order ID',
#     'restaurant_name_ar': 'Restaurant Name (Arabic)',
#     'city_name': 'City',
#     'is_acquisition': 'Is Acquisition?',
#     'is_acquision_by_restaurant': 'Is Acquisition by Restaurant?',
#     'rdf_offer_applied': 'RDF Offer Applied',
#     'rdf_offer_type': 'RDF Offer Type',
#     'offer_names': 'Offer Names'
# }

# display_df = filtered_df[columns_to_show].rename(columns=rename_mapping)

# st.dataframe(display_df, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Othaim Orders Dashboard 2025", layout="wide")
st.markdown(""" <style>footer {visibility: hidden;} </style> """, unsafe_allow_html=True)

# --- TITLE ---
st.title("📊 Othaim Orders Dashboard (2025)")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    return pd.read_csv('data/othaim_data.csv')

df = load_data()

# --- SIDEBAR FILTERS ---
with st.sidebar:
    st.header("Filters")
    cities = st.multiselect("Select Cities", options=df['city_name'].unique())
    acquisition = st.selectbox("Is Acquisition?", options=["All", "Yes", "No"])
    acquisition_by_restaurant = st.selectbox("Is Acquisition by Restaurant?", options=["All", "Yes", "No"])
    offer_id_input = st.text_input("Filter by Offer ID")

# --- APPLY FILTERS WITH LOADING SPINNER ---
with st.spinner("Applying filters..."):
    filtered_df = df.copy()

    if cities:
        filtered_df = filtered_df[filtered_df['city_name'].isin(cities)]

    if acquisition != "All":
        acquisition_bool = True if acquisition == "Yes" else False
        filtered_df = filtered_df[filtered_df['is_acquisition'] == acquisition_bool]

    if acquisition_by_restaurant != "All":
        acquisition_restaurant_bool = True if acquisition_by_restaurant == "Yes" else False
        filtered_df = filtered_df[filtered_df['is_acquision_by_restaurant'] == acquisition_restaurant_bool]

    if offer_id_input:
        filtered_df = filtered_df[filtered_df['offer_ids'].astype(str).str.contains(offer_id_input)]

# --- CHECK IF EMPTY AFTER FILTERS ---
if filtered_df.empty:
    st.warning("⚠️ No matching records found based on selected filters.")
else:
    # --- KPIs ---
    total_orders = filtered_df['order_id'].nunique()
    total_restaurants = filtered_df['restaurant_id'].nunique()
    unique_offers = filtered_df['offer_ids'].nunique()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Orders", f"{total_orders:,}")
    #col2.metric("Unique Restaurants", f"{total_restaurants:,}")
    col3.metric("Unique Offers Used", f"{unique_offers:,}")

    st.markdown("---")

    # --- VISUALS ---

        # --- DETAILED KPI NUMBERS ---
    st.markdown("### 📈 Detailed KPI Numbers")

    if offer_id_input:
        # If specific offer ID is searched
        offer_count = filtered_df[filtered_df['offer_ids'].astype(str).str.contains(offer_id_input)].shape[0]
        
        st.subheader(f"Results for Offer ID containing: '{offer_id_input}'")
        st.metric(label="Matching Orders", value=f"{offer_count:,}")

    else:
        # Top 5 most used coupon IDs
        top_coupons = (
            filtered_df['coupon_id']
            .value_counts()
            .head(5)
            .reset_index()
        )
        top_coupons.columns = ['Coupon ID', 'Count']

        # Display each top coupon as a separate metric
        cols = st.columns(len(top_coupons))

        for idx, row in top_coupons.iterrows():
            cols[idx].metric(label=f"Coupon ID: {row['Coupon ID']}", value=f"{row['Count']:,}")

    st.markdown("---")

    # Orders by City
    orders_by_city = filtered_df['city_name'].value_counts().reset_index()
    orders_by_city.columns = ['City', 'Orders']
    fig_city = px.bar(orders_by_city, x='City', y='Orders', title="Orders per City", height=400)

    # Top 10 Offer Names
    top_offers = filtered_df['offer_names'].value_counts().head(10).reset_index()
    top_offers.columns = ['Offer Name', 'Orders']
    fig_offers = px.bar(top_offers, x='Orders', y='Offer Name', title="Top 10 Performing Offers", orientation='h', height=400)

    # Offer Type Distribution
    fig_offer = px.pie(filtered_df, names='rdf_offer_type', title="Offer Types Distribution", hole=0.5)

    # Layout plots
    col4, col5 = st.columns(2)
    col4.plotly_chart(fig_city, use_container_width=True)
    col5.plotly_chart(fig_offers, use_container_width=True)

    st.plotly_chart(fig_offer, use_container_width=True)




    # Detailed Table
    st.markdown("### 📋 Detailed Data View")

    columns_to_show = [
        'order_id',
        'offer_ids',
        'restaurant_name_ar',
        'city_name',
        'is_acquisition',
        'is_acquision_by_restaurant',
        'rdf_offer_applied',
        'rdf_offer_type',
        'offer_names'
    ]

    rename_mapping = {
        'order_id': 'Order ID',
        'offer_ids': 'Offer ID',
        'restaurant_name_ar': 'Restaurant Name (Arabic)',
        'city_name': 'City',
        'is_acquisition': 'Is Acquisition?',
        'is_acquision_by_restaurant': 'Is Acquisition by Restaurant?',
        'rdf_offer_applied': 'RDF Offer Applied',
        'rdf_offer_type': 'RDF Offer Type',
        'offer_names': 'Offer Names'
    }

    # Prepare display DataFrame
    display_df = filtered_df[columns_to_show].rename(columns=rename_mapping)

    # Map 0/1 to No/Yes for the relevant columns
    yes_no_columns = ['Is Acquisition?', 'Is Acquisition by Restaurant?', 'RDF Offer Applied']

    for col in yes_no_columns:
        display_df[col] = display_df[col].map({0: 'No', 1: 'Yes'})

    st.dataframe(display_df, use_container_width=True)


# --- THEME ---
# Light mode should be set externally:
# (in Streamlit Cloud settings OR config.toml locally:)
# Example config.toml content:
# [theme]
# base="light"
