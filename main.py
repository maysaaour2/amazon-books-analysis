"""
Analyze Best Selling Amazon Books
Dataset: "Amazon Top 50 Bestselling Books 2009-2019" (Kaggle) -> save it as bestsellers.csv
Columns: Name, Author, User Rating, Reviews, Price, Year, Genre
"""
import pandas as pd
import matplotlib.pyplot as plt

# 1. IMPORT
df = pd.read_csv("bestsellers.csv")
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
print("Rows, columns:", df.shape)
print(df.head(), "\n")

# 2. CLEAN
print("Missing values:\n", df.isna().sum(), "\n")
df = df.drop_duplicates()
df = df.dropna(subset=["name", "author", "price", "user_rating"])
# Same book can appear in several years: keep one row per book for book-level stats
books = df.drop_duplicates(subset="name")

# 3. ANALYSIS
print("=== Top 10 authors by number of bestsellers ===")
top_authors = books["author"].value_counts().head(10)
print(top_authors, "\n")

print("=== Fiction vs Non Fiction ===")
genre_stats = books.groupby("genre").agg(
    books=("name", "count"),
    avg_price=("price", "mean"),
    avg_rating=("user_rating", "mean"),
    avg_reviews=("reviews", "mean"),
).round(2)
print(genre_stats, "\n")

print("=== Top 10 most reviewed books ===")
print(books.nlargest(10, "reviews")[["name", "author", "reviews"]], "\n")

print("=== Top 10 highest rated books (min 1000 reviews) ===")
rated = books[books["reviews"] >= 1000]
print(rated.nlargest(10, "user_rating")[["name", "author", "user_rating"]], "\n")

print("=== Most expensive books ===")
print(books.nlargest(5, "price")[["name", "price"]], "\n")

print("=== Average price per year ===")
price_year = df.groupby("year")["price"].mean().round(2)
print(price_year, "\n")

print("=== Correlation ===")
print(books[["price", "user_rating", "reviews"]].corr().round(2), "\n")

# 4. CHARTS
top_authors.sort_values().plot(kind="barh", title="Top 10 authors by bestsellers")
plt.tight_layout(); plt.savefig("top_authors.png"); plt.clf()

genre_stats["books"].plot(kind="pie", autopct="%1.0f%%", title="Fiction vs Non Fiction")
plt.ylabel(""); plt.tight_layout(); plt.savefig("genres.png"); plt.clf()

price_year.plot(kind="line", marker="o", title="Average price per year")
plt.ylabel("Price ($)"); plt.tight_layout(); plt.savefig("price_per_year.png"); plt.clf()

books.plot(kind="scatter", x="price", y="user_rating", title="Price vs rating")
plt.tight_layout(); plt.savefig("price_vs_rating.png")

print("Charts saved as PNG files.")
