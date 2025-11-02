# analytics/analytics.py
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]  # project root
DATA_CSV = BASE / "data" / "halloween_events.csv"
OUT_DIR = BASE / "images"
OUT_DIR.mkdir(exist_ok=True)

def load_data():
    df = pd.read_csv(DATA_CSV, parse_dates=["date"])
    return df

def summary(df):
    s = {
        "total_events": len(df),
        "unique_cities": df['city'].nunique(),
        "average_price_gbp": df['price_gbp'].mean(),
        "average_attendance": df['attendance'].mean(),
        "min_price_gbp": df['price_gbp'].min(),
        "max_price_gbp": df['price_gbp'].max(),
        "max_attendance": df['attendance'].max(),
    }
    return s

def plot_events_per_city(df):
    counts = df.groupby('city').size().sort_values(ascending=False)
    ax = counts.plot(kind='bar', figsize=(6,4))
    ax.set_title("Events per city")
    ax.set_ylabel("Number of events")
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(OUT_DIR / "events_per_city.png")
    plt.close(fig)

def plot_price_per_event(df):
    ax = df.plot.bar(x='title', y='price_gbp', legend=False, figsize=(8,4))
    ax.set_title("Price per event (GBP)")
    ax.set_xlabel("")
    ax.set_ylabel("Price (GBP)")
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(OUT_DIR / "price_per_event.png")
    plt.close(fig)

def plot_event_timeline(df):
    fig, ax = plt.subplots(figsize=(8,2))
    ax.scatter(df['date'].dt.date, [1]*len(df))
    ax.set_yticks([])
    ax.set_title("Event dates timeline")
    fig.autofmt_xdate(rotation=25)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "events_timeline.png")
    plt.close(fig)



def plot_attendance_per_event(df):
    ax = df.plot.bar(x='title', y='attendance', legend=False, figsize=(8,4), color='orange')
    ax.set_title("Attendance per event")
    ax.set_xlabel("")
    ax.set_ylabel("Attendance")
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(OUT_DIR / "attendance_per_event.png")
    plt.close(fig)

def plot_average_attendance_per_city(df):
    avg_attendance = df.groupby('city')['attendance'].mean().sort_values(ascending=False)
    ax = avg_attendance.plot(kind='bar', figsize=(6,4), color='purple')
    ax.set_title("Average attendance per city")
    ax.set_ylabel("Average attendance")
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(OUT_DIR / "average_attendance_per_city.png")
    plt.close(fig)

def plot_price_vs_attendance(df):
    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(df['price_gbp'], df['attendance'], color='teal')
    ax.set_title("Price vs Attendance")
    ax.set_xlabel("Price (GBP)")
    ax.set_ylabel("Attendance")
    for i, row in df.iterrows():
        ax.text(row['price_gbp']+0.1, row['attendance']+5, row['city'], fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "price_vs_attendance.png")
    plt.close(fig)


def main():
    df = load_data()
    print("Summary:", summary(df))
    plot_events_per_city(df)
    plot_price_per_event(df)
    plot_event_timeline(df)
    plot_attendance_per_event(df)
    plot_average_attendance_per_city(df)
    plot_price_vs_attendance(df)
    print(f"Saved images to {OUT_DIR}")
    
if __name__ == "__main__":
    main()



