import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r"C:\Users\antho\OneDrive\Education\FreeCodeCamp\Data Analysis with Python\Datasets\fcc-forum-pageviews.csv", index_col="date", parse_dates=True)


# Clean data
q1 = df["value"].quantile(0.025)
q3 = df["value"].quantile(0.975)

df = df[(df["value"] >= q1) & (df["value"] <= q3)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df["value"])

    # Set labels and title
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)

    # Save image and return fig (don't change this part)
    fig.savefig(r"C:\Users\antho\OneDrive\Education\FreeCodeCamp\Data Analysis with Python\Figures\line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Years"] = df_bar.index.year
    df_bar["Months"] = df_bar.index.month_name()
    df_bar = pd.DataFrame(df_bar.groupby(["Years", "Months"], sort=False)["value"].mean().round().astype(int))
    df_bar = df_bar.rename(columns={"value": "Average Page Views"})
    df_bar = df_bar.reset_index()
    missing_data = {
        "Years": [2016, 2016, 2016, 2016],
        "Months": ['January', 'February', 'March', 'April'],
        "Average Page Views": [0, 0, 0, 0]
    }

    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")
    chart = sns.barplot(data=df_bar, x="Years", y="Average Page Views", hue="Months", palette="tab10")
    chart.set_xticklabels(chart.get_xticklabels(), horizontalalignment='center')

    # Save image and return fig (don't change this part)
    fig.savefig(r"C:\Users\antho\OneDrive\Education\FreeCodeCamp\Data Analysis with Python\Figures\bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Year-wise box plot
    sns.boxplot(
        x = "year",
        y = "value",
        showmeans=True,
        data=df_box,
        ax=ax1
    )
    ax1.set_title("Year-wise Box Plot (Trend)")

    # Month-wise box plot with rotated x-axis labels
    sns.boxplot(
        x = "month",
        y = "value",
        showmeans=True,
        data=df_box,
        ax=ax2
    )

    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig(r"C:\Users\antho\OneDrive\Education\FreeCodeCamp\Data Analysis with Python\Figures\box_plot.png")
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()