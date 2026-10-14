
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self):
        self.df = None

    def load_data(self):
        path = input("Enter CSV file path: ")
        try:
            self.df = pd.read_csv(path)
            print("Dataset loaded!")
        except Exception as e:
            print("Error:", e)

    def explore(self):
        if self.df is not None:
            print(self.df.head())
            print(self.df.info())
            print(self.df.describe())
            print(self.df.isnull().sum())

    def clean(self):
        if self.df is not None:
            self.df = self.df.drop_duplicates()
            self.df = self.df.fillna(0)
            print("Data cleaned!")

    def analyze(self):
        if self.df is not None:
            print(self.df.describe())
            print(self.df.select_dtypes(
                include="number").sum())

    def visualize(self):
        if self.df is not None:
            self.df.select_dtypes(
                include="number").hist(figsize=(8, 6))
            plt.tight_layout()
            plt.show()

            sns.heatmap(
                self.df.select_dtypes(
                    include="number").corr(),
                annot=True
            )
            plt.show()

    def save_plot(self):
        if self.df is not None:
            self.df.select_dtypes(
                include="number").hist()
            plt.savefig("sales_chart.png")
            plt.show()
            print("Chart saved!")

def main():
    app = SalesDataAnalyzer()

    while True:
        print("""
--- SALES DATA ANALYSIS ---
1. Load Dataset
2. Explore Data
3. Clean Data
4. Analyze Data
5. Visualize Data
6. Save Visualization
7. Exit
""")
        ch = input("Enter choice: ")

        if ch == "1": app.load_data()
        elif ch == "2": app.explore()
        elif ch == "3": app.clean()
        elif ch == "4": app.analyze()
        elif ch == "5": app.visualize()
        elif ch == "6": app.save_plot()
        elif ch == "7": break
        else: print("Invalid choice")

if __name__ == "__main__":
    main()
