import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_eda():
    st.header("Exploratory Data Analysis")
    try:
        df = pd.read_csv("diabetes.csv")
        
        st.subheader("Dataset Sample")
        st.dataframe(df.head(10))

        st.subheader("Correlation Matrix Heatmap")
        fig_corr, ax_corr = plt.subplots(figsize=(12, 10))
        sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax_corr)
        st.pyplot(fig_corr)

        st.subheader("Class Distribution (Outcome)")
        class_dist = df["Outcome"].value_counts()
        labels = ["Non-Diabetic (0)", "Diabetic (1)"]
        
        # Bar Chart
        st.write("Bar Chart:")
        fig_bar, ax_bar = plt.subplots(figsize=(6, 4))

        sns.barplot(x=class_dist.index, y=class_dist.values, ax=ax_bar, palette='viridis')
        
        for index, value in enumerate(class_dist):
            ax_bar.text(
                index,
                value - (value * 0.5),
                str(value),
                ha='center',
                va='center',
                fontsize=12,
                fontweight='bold',
            )

        ax_bar.set_title("Count of Diabetic vs. Non-Diabetic")
        ax_bar.set_xlabel("Outcome", fontsize=12)
        ax_bar.set_ylabel("Count", fontsize=12)
        ax_bar.set_xticks(class_dist.index)
        ax_bar.set_xticklabels(["Non-Diabetic (0)", "Diabetic (1)"])

        st.pyplot(fig_bar)
        
        # Pie Chart
        st.write("Pie Chart:")
        fig_pie, ax_pie = plt.subplots()
        ax_pie.pie(
            class_dist, 
            labels=labels, 
            autopct='%1.1f%%',
            startangle=90, 
            textprops={'fontsize': 12}
        )
        ax_pie.axis('equal')

        st.pyplot(fig_pie)
        
        st.write("Raw Counts:")
        st.write("0: Non-Diabetic, 1: Diabetic")
        st.write(class_dist)

    except FileNotFoundError:
        st.error("File was not found")