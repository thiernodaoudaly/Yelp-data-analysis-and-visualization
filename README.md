# Yelp Data Analysis & Visualization

<div align="center">

![PySpark](https://img.shields.io/badge/PySpark-3.x-E25A1C?style=flat-square&logo=apachespark&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-visualisation-11557C?style=flat-square)
![Seaborn](https://img.shields.io/badge/Seaborn-statistical%20plots-4C72B0?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter-notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

**Exploratory analysis of the Yelp Academic Dataset using PySpark — 17 analyses covering businesses, users, reviews, and behavioural patterns, served through a Streamlit dashboard.**

</div>

## Overview

The [Yelp Academic Dataset](https://www.yelp.com/dataset) contains millions of records across five interconnected JSON files. This project processes and analyses that data at scale using **Apache Spark**, then presents the results through a custom **Streamlit** dashboard with Plotly visualisations.

### Dataset schema

The dataset consists of five JSON files:

| File | Content |
|---|---|
| `yelp_academic_dataset_business.json` | Business details — location, categories, stars, attributes |
| `yelp_academic_dataset_review.json` | User reviews — text, rating, date, votes |
| `yelp_academic_dataset_user.json` | User profiles — activity, fans, compliments, elite status |
| `yelp_academic_dataset_checkin.json` | Check-in timestamps per business |
| `yelp_academic_dataset_tip.json` | Short tips (less detailed than reviews) |

## Analyses Performed

### Business insights

| # | Analysis | Key finding |
|---|---|---|
| 1 | Top 10 cities by business count | High-traffic cities dominate — driven by tourism and economic activity |
| 2 | Cities with highest average rating (min. 100 businesses) | Ratings cluster around 4 stars across most cities |
| 3 | Top 10 businesses by check-in volume | Identifies the most physically visited venues |
| 4 | Top 15 most frequent business categories | Dominated by restaurants, beauty, health, and auto services |
| 5 | Top 3 most reviewed categories per year | Mexican restaurants consistently lead since 2005 |
| 6 | Top 10 cities by average rating (≥3 stars) | Niche or less dense cities sometimes outperform majors |
| 7 | Business categories with highest average ratings | Escape rooms, therapeutic massage, barbers — high-engagement niches score highest |

### Review insights

| # | Analysis | Key finding |
|---|---|---|
| 8 | Distribution of reviews by star rating | Strong positivity bias — 4 and 5-star reviews dominate |
| 9 | Review volume evolution by year | Steady growth until 2019; slowdown likely linked to COVID-19 |
| 10 | Average review length distribution | ~567 characters on average — users write detailed feedback |

### User insights

| # | Analysis | Key finding |
|---|---|---|
| 11 | Top 10 most prolific reviewers (review count) | Power users with thousands of reviews |
| 12 | Top 10 most active users (reviews + tips + check-ins combined) | Composite activity score identifies true platform champions |
| 13 | Top 10 users by fan count | Influencer-level users with large followings |
| 14 | Top 10 most influential users (fans + compliments + useful votes) | Weighted influence score combining reach and quality signals |
| 15 | Top 10 most reliable users (trust score) | Users whose average rating is closest to the community average — proxy for objectivity |

### Correlation analyses

| # | Analysis | Key finding |
|---|---|---|
| 16 | Average rating vs. review count | Weak correlation — high ratings don't guarantee high visibility |
| 17 | Price range vs. average rating | No significant effect — customers rate fairly regardless of price |

## Architecture

```
yelp-data-analysis-and-visualization/
├── yelp_data_analysis_and_visualization.ipynb   # Full analysis pipeline
└── streamlit/
    ├── main.py                                  # Streamlit dashboard
    └── assets/images/                           # Pre-generated visualisations
        ├── schema.png
        ├── prepocessing.png
        ├── top_villes_with_entreprise.png
        ├── top_city_mean.png
        ├── top_categories.png
        ├── top_categories_year.png
        ├── distribution_price_note.png
        ├── avis_evolution.png
        ├── avis_length_distribution.png
        ├── correlation_note_moyenne_nombre_avis.png
        ├── top_user_actif.png
        ├── top_user_actif_score_activities.png
        ├── top_user_influent.png
        └── top_user_reliable.png
```

## Tech Stack

| Layer | Technology | Role |
|---|---|---|
| Big Data processing | PySpark (Apache Spark) | Load, clean, and query multi-million-row JSON files |
| SQL queries | Spark SQL + temporary views | Declarative analysis across joined datasets |
| Data manipulation | Pandas | Bridge between Spark DataFrames and visualisation |
| Visualisation | Matplotlib + Seaborn | Static charts in the notebook |
| Dashboard | Streamlit + Plotly | Interactive web interface |
| Environment | Google Colab | Spark session with 12GB driver memory |

## Setup & Usage

### Running the notebook (Google Colab recommended)

```bash
# Dependencies are installed inside the notebook:
# pip install findspark pandas matplotlib seaborn

# The dataset is downloaded automatically from:
# https://business.yelp.com/external-assets/files/Yelp-JSON.zip
```

Open `yelp_data_analysis_and_visualization.ipynb` in Google Colab and run all cells in order.

> A Spark session is initialised with 12GB driver memory — Colab's high-RAM runtime is recommended.

### Running the Streamlit dashboard

```bash
cd streamlit
pip install streamlit plotly pandas matplotlib seaborn
streamlit run main.py
# → http://localhost:8501
```

The dashboard uses the pre-generated images in `assets/images/` — no live Spark session required.

## Roadmap

- [ ] Deploy the Streamlit dashboard online (Streamlit Cloud or Hugging Face Spaces)
- [ ] Add real-time data streaming simulation with Spark Structured Streaming
- [ ] Sentiment analysis on review text (NLP)
- [ ] Business recommendation engine based on user history

## Contributors

**Thierno Daouda LY · Dioumamane FALL · Moussa SEYE**

## License

MIT License — see [LICENSE](LICENSE) for details.