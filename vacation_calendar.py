import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# -----------------------
# Vacation Dates: June 21–28, 2025
# -----------------------
start_date = datetime(2025, 6, 21)
week_dates = [start_date + timedelta(days=i) for i in range(7)]

# -----------------------
# Sample Guest Data
# -----------------------
guest_data = [
    {"name": "Riley", "arrival": "2025-06-21 15:00", "departure": "2025-06-25 12:00"},
    {"name": "Reilly", "arrival": "2025-06-21 13:00", "departure": "2025-06-27 12:00"},
    {"name": "Foy", "arrival": "2025-06-22 15:00", "departure": "2025-06-27 12:00"},
    {"name": "Foley", "arrival": "2025-06-22 15:00", "departure": "2025-06-26 12:00"},
    {"name": "Callahan", "arrival": "2025-06-22 15:00", "departure": "2025-06-27 12:00"},

]

guest_df = pd.DataFrame(guest_data)
guest_df["arrival"] = pd.to_datetime(guest_df["arrival"])
guest_df["departure"] = pd.to_datetime(guest_df["departure"])

# -----------------------
# Sample Activities
# -----------------------
activity_data = [
    {"date": "2025-06-21", "activity": "Welcome BBQ 🍔"},
    {"date": "2025-06-22", "activity": "Beach Day 🏖️"},
    {"date": "2025-06-23", "activity": "Kayaking 🚣‍♀️"},
    {"date": "2025-06-24", "activity": "Hiking 🥾"},
    {"date": "2025-06-25", "activity": "Winery Tour 🍷"},
    {"date": "2025-06-26", "activity": "Free Day 🌤️"},
    {"date": "2025-06-27", "activity": "Boat Party 🚤"},
    {"date": "2025-06-28", "activity": "Farewell Breakfast 🥞"},
]
activity_df = pd.DataFrame(activity_data)
activity_df["date"] = pd.to_datetime(activity_df["date"])

# -----------------------
# Sample Meal Plan
# -----------------------
meal_plan = {
    "2025-06-21": {"Breakfast": "-", "Lunch": "-", "Dinner": "Pan Seared Tuna with Avocado 🐟 "},
    "2025-06-22": {"Breakfast": "Omelets", "Lunch": "Sandwiches from Kamuda's Market", "Dinner": "Lobsters 🦞"},
    "2025-06-23": {"Breakfast": "Quiche Options", "Lunch": "Tuna Melts", "Dinner": "Steak Night"},
    "2025-06-24": {"Breakfast": "Morning Side Bakery", "Lunch": "-", "Dinner": "-"},
    "2025-06-25": {"Breakfast": "Eggs and Popovers", "Lunch": "Meatball Subs", "Dinner": "Island Pork Tenderloin"},
    "2025-06-26": {"Breakfast": "Free Day", "Lunch": "Free Day", "Dinner": "Free Night"},
    "2025-06-27": {"Breakfast": "Muffins", "Lunch": "Leftovers", "Dinner": "Seafood Stew"},
}

# -----------------------
# UI Layout
# -----------------------
st.set_page_config(page_title="full", layout="wide")
st.title("St. Michael's College Reunion 2025: June 21 – 27, 2025")

tab1, tab2 = st.tabs(["📋 Activities & Arrivals", "🍽️ Meal Plan"])

# -----------------------
# Tab 1: Activities & Arrivals
# -----------------------
with tab1:
    st.header("🗓️ Weekly Overview")

    calendar_cols = st.columns(8)
    for i, date in enumerate(week_dates):
        with calendar_cols[i]:
            st.markdown(f"### {date.strftime('%a %d')}")
            
            # Arrivals
            arriving = guest_df[guest_df["arrival"].dt.date == date.date()]
            for _, row in arriving.iterrows():
                st.markdown(f"🟢 **{row['name']}** arrives at {row['arrival'].strftime('%H:%M')}")
                
            # Departures
            departing = guest_df[guest_df["departure"].dt.date == date.date()]
            for _, row in departing.iterrows():
                st.markdown(f"🔴 **{row['name']}** departs at {row['departure'].strftime('%H:%M')}")

            # Activity
            act = activity_df[activity_df["date"].dt.date == date.date()]
            if not act.empty:
                st.markdown(f"⭐ {act.iloc[0]['activity']}")
            else:
                st.markdown("➕ No activity planned")

    st.divider()
    st.subheader("📅 Who’s Here on a Selected Day")
    selected_day = st.date_input("Choose a date", value=week_dates[0], min_value=week_dates[0], max_value=week_dates[-1])
    present = guest_df[
        (guest_df["arrival"].dt.date <= selected_day) &
        (guest_df["departure"].dt.date > selected_day)
    ]
    if present.empty:
        st.write("No guests are present on this day.")
    else:
        for _, row in present.iterrows():
            st.markdown(f"- **{row['name']}** (Arr: {row['arrival'].strftime('%m/%d')}, Dep: {row['departure'].strftime('%m/%d')})")

# -----------------------
# Tab 2: Meal Plan
# -----------------------
with tab2:
    st.header("🍴 Daily Meal Plan")
    
    for date in week_dates:
        date_str = date.strftime('%Y-%m-%d')
        st.markdown(f"### {date.strftime('%A, %B %d')}")
        meals = meal_plan.get(date_str)
        if meals:
            st.markdown(f"- **Breakfast:** {meals['Breakfast']}")
            st.markdown(f"- **Lunch:** {meals['Lunch']}")
            st.markdown(f"- **Dinner:** {meals['Dinner']}")
        else:
            st.markdown("No meals planned for this day.")
        st.divider()

# import streamlit as st
# import pandas as pd
# from datetime import datetime, timedelta

# st.set_page_config(page_title="Vacation Calendar Planner", layout="wide")

# st.title("🏖️ Vacation Week Planner")
# st.markdown("View arrivals, departures, and daily activities for your vacation.")

# # Sample guest data (can be replaced by CSV upload)
# guest_data = [
#     {"name": "Alice", "arrival": "2025-06-17 14:00", "departure": "2025-06-21 10:00"},
#     {"name": "Bob", "arrival": "2025-06-18 16:00", "departure": "2025-06-22 09:00"},
#     {"name": "Charlie", "arrival": "2025-06-19 12:00", "departure": "2025-06-25 18:00"},
# ]

# guest_df = pd.DataFrame(guest_data)
# guest_df["arrival"] = pd.to_datetime(guest_df["arrival"])
# guest_df["departure"] = pd.to_datetime(guest_df["departure"])

# # Optional CSV Upload
# st.sidebar.header("📤 Upload Data")
# guest_file = st.sidebar.file_uploader("Upload Guests CSV (name,arrival,departure)", type="csv")
# activity_file = st.sidebar.file_uploader("Upload Activities CSV (date,activity)", type="csv")

# # Replace default data if uploaded
# if guest_file:
#     guest_df = pd.read_csv(guest_file, parse_dates=["arrival", "departure"])

# # Activities Data
# activity_data = [
#     {"date": "2025-06-17", "activity": "Beach day 🏖️"},
#     {"date": "2025-06-18", "activity": "Hiking trip 🥾"},
#     {"date": "2025-06-19", "activity": "Wine tour 🍷"},
#     {"date": "2025-06-20", "activity": "Free day 🌞"},
#     {"date": "2025-06-21", "activity": "Boat ride 🚤"},
# ]
# activity_df = pd.DataFrame(activity_data)
# activity_df["date"] = pd.to_datetime(activity_df["date"])

# if activity_file:
#     activity_df = pd.read_csv(activity_file, parse_dates=["date"])

# # Select week
# start_date = st.date_input("📅 Select start of vacation week", datetime(2025, 6, 17))
# week_dates = [start_date + timedelta(days=i) for i in range(7)]

# # Display calendar
# st.subheader("📋 Weekly Calendar")

# calendar_cols = st.columns(7)
# for i, date in enumerate(week_dates):
#     with calendar_cols[i]:
#         st.markdown(f"### {date.strftime('%a %b %d')}")

#         # Who's arriving?
#         arriving = guest_df[guest_df["arrival"].dt.date == date]
#         if not arriving.empty:
#             for _, row in arriving.iterrows():
#                 st.markdown(f"🟢 **{row['name']}** arrives at {row['arrival'].strftime('%H:%M')}")

#         # Who's departing?
#         departing = guest_df[guest_df["departure"].dt.date == date]
#         if not departing.empty:
#             for _, row in departing.iterrows():
#                 st.markdown(f"🔴 **{row['name']}** departs at {row['departure'].strftime('%H:%M')}")

#         # Activities
#         day_activities = activity_df[activity_df["date"].dt.date == date]
#         if not day_activities.empty:
#             for _, row in day_activities.iterrows():
#                 st.markdown(f"⭐ {row['activity']}")
#         else:
#             st.markdown("➕ No activity planned")

# # Day detail view
# st.subheader("🔍 View or Plan a Specific Day")
# selected_day = st.date_input("Select a day to plan", week_dates[0])

# # Guests present on selected day
# present = guest_df[
#     (guest_df["arrival"].dt.date <= selected_day) &
#     (guest_df["departure"].dt.date > selected_day)
# ]

# st.markdown(f"### 👥 Guests on {selected_day.strftime('%A, %B %d')}")
# if present.empty:
#     st.write("No one is present.")
# else:
#     for _, row in present.iterrows():
#         st.markdown(f"- {row['name']} (Arrived: {row['arrival'].strftime('%m-%d %H:%M')}, "
#                     f"Departs: {row['departure'].strftime('%m-%d %H:%M')})")

# # Activity planning
# st.markdown("### 📝 Add or Update Activity")
# new_activity = st.text_input("Activity for the day")
# if st.button("Save Activity"):
#     activity_df = activity_df[activity_df["date"].dt.date != selected_day]
#     if new_activity:
#         new_row = pd.DataFrame([{"date": selected_day, "activity": new_activity}])
#         activity_df = pd.concat([activity_df, new_row], ignore_index=True)
#     st.success(f"Activity for {selected_day.strftime('%A')} saved. Rerun to refresh calendar.")



# import streamlit as st
# import pandas as pd
# from datetime import datetime, timedelta

# # Title
# st.title("🏖️ Vacation Week Arrival Calendar")

# # Sample Data
# data = [
#     {"name": "Alice", "date": "2025-06-17", "time": "14:00", "link": "https://example.com/alice"},
#     {"name": "Bob", "date": "2025-06-17", "time": "18:30", "link": "https://example.com/bob"},
#     {"name": "Charlie", "date": "2025-06-18", "time": "12:00", "link": "https://example.com/charlie"},
#     {"name": "Diana", "date": "2025-06-19", "time": "09:00", "link": "https://example.com/diana"},
#     {"name": "Ethan", "date": "2025-06-21", "time": "16:15", "link": "https://example.com/ethan"},
# ]

# # Convert to DataFrame
# df = pd.DataFrame(data)
# df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])

# # Select week start
# start_date = st.date_input("Select the week starting date", datetime(2025, 6, 17))
# end_date = start_date + timedelta(days=6)

# # Filter for the week
# weekly_df = df[(df["datetime"].dt.date >= start_date) & (df["datetime"].dt.date <= end_date)]

# # Display calendar
# st.subheader("🗓️ Arrivals This Week")

# if weekly_df.empty:
#     st.info("No arrivals scheduled for this week.")
# else:
#     for date in pd.date_range(start_date, end_date):
#         st.markdown(f"### {date.strftime('%A, %B %d')}")
#         day_df = weekly_df[weekly_df["datetime"].dt.date == date.date()]
#         if day_df.empty:
#             st.write("No arrivals.")
#         else:
#             for _, row in day_df.iterrows():
#                 st.markdown(f"- **{row['name']}** arriving at **{row['time']}** [🔗 Link]({row['link']})")

# # Optional: Upload CSV
# st.sidebar.markdown("### 📤 Upload Custom Arrival Data")
# uploaded_file = st.sidebar.file_uploader("Upload a CSV with columns: name, date, time, link", type="csv")
# if uploaded_file:
#     user_df = pd.read_csv(uploaded_file)
#     user_df["datetime"] = pd.to_datetime(user_df["date"] + " " + user_df["time"])
#     df = user_df
#     st.success("Custom data loaded. Refresh the page to reset.")
