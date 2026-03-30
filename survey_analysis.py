# Survey Satisfaction Analysis
# Loads survey data, analyzes satisfaction levels,
# and saves charts as image files.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------------------------
# Load Data
# ------------------------------------------------
def load_data(file_name):
    try:
        df = pd.read_csv(file_name)
        print("Survey data loaded successfully.")
        return df
    except:
        print("File not found or empty. Using sample data.")

        sample = {
            "RespondentID": range(1, 6),
            "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
            "Age": [28, 35, 42, 31, 26],
            "Gender": ["Female", "Male", "Male", "Female", "Female"],
            "Satisfaction": [
                "Very Satisfied",
                "Satisfied",
                "Neutral",
                "Very Satisfied",
                "Dissatisfied",
            ],
        }

        return pd.DataFrame(sample)


# ------------------------------------------------
# Analyze Satisfaction
# ------------------------------------------------
def analyze_data(df):

    order = [
        "Very Satisfied",
        "Satisfied",
        "Neutral",
        "Dissatisfied",
        "Very Dissatisfied",
    ]

    counts = df["Satisfaction"].value_counts().reindex(order, fill_value=0)

    print("\nSurvey Satisfaction Summary")
    print("----------------------------")
    print(counts)

    return counts


# ------------------------------------------------
# Bar Chart (Saved as File)
# ------------------------------------------------
def create_bar_chart(counts):

    sns.set_style("whitegrid")

    plt.figure(figsize=(10, 6))
    counts.plot(kind="bar", color="skyblue")

    plt.title("Survey Satisfaction Results")
    plt.xlabel("Satisfaction Level")
    plt.ylabel("Number of Responses")

    plt.tight_layout()

    # Save chart
    plt.savefig("satisfaction_bar_chart.png")

    print("Bar chart saved as satisfaction_bar_chart.png")

    plt.show()


# ------------------------------------------------
# Pie Chart (Saved as File)
# ------------------------------------------------
def create_pie_chart(counts):

    plt.figure(figsize=(8, 8))

    plt.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=90,
    )

    plt.title("Satisfaction Distribution")

    # Save chart
    plt.savefig("satisfaction_pie_chart.png")

    print("Pie chart saved as satisfaction_pie_chart.png")

    plt.show()


# ------------------------------------------------
# Main Function
# ------------------------------------------------
def main():

    df = load_data("survey_data.csv")

    print("\nPreview of Data")
    print(df.head())

    counts = analyze_data(df)

    create_bar_chart(counts)

    create_pie_chart(counts)


if __name__ == "__main__":
    main()