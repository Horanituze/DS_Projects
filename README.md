# DATA SCIENCE PROJECTS 
- Salaries
    - Data Science Salaries prediction
- GUI app 
    - DBMS GUI app
- AIRLINE DELAYS
    - 2015 Flights Delay
    - exploratory data analysis 
    - classification
- DATA VISUALIZATION USING R
    - A collection of data visualization exercises in R (ggplot2, `nycflights13`, EPA fuel economy data, election data, Gapminder, and more), exploring how chart design choices affect interpretation, and comparing different visualization techniques for the same data.

Each `.Rmd` file knits to a GitHub-flavored `.md` document (`output: github_document`) so plots render directly on GitHub.

## Contents

- [**01 — Visualization Design Principles**](./01-visualization-design-principles.md)
  Recreating a misleading truncated-baseline bar chart side-by-side with a corrected zero-baseline version, then applying the same design lens to EPA fuel economy data: fuel type distributions, fuel type trends over time, and four ways to compare highway MPG distributions across years (strip plot, boxplot, violin plot, ridgeline plot).

- [**02 — NYC Flights Analysis**](./02-nyc-flights-analysis.md)
  A full pass through `nycflights13`: airport reference data, departure delay summaries, air time distributions, top/summer-only/high-altitude destinations, cancellation rates by destination location (mapped), and the relationship between departure delay, arrival delay, wind speed, and time of day.

- [**03 — Statistical Distributions & Model Diagnostics**](./03-statistical-distributions.md)
  Comparing density and eCDF plots for self-reported height data, then a scatterplot matrix and faceted coplot examining relationships in rubber abrasion-loss testing data.


## Tools Used
R, ggplot2, dplyr, `nycflights13`, `ggridges`, `ggExtra`, `GGally`, `ggmosaic`, `plotly`, `gapminder`, `kableExtra`, `forcats`

