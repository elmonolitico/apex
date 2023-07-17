# Papelerias Data Analysis Project

This repository contains the code and resources for the Papelerias Data Analysis Project. The project aims to demonstrate the capabilities of data analysis and showcase potential value-add using the dataset provided by Papelerias.

## Introduction

The primary objective of this project is to identify opportunities for cost reduction within Papelerias by analyzing the dataset. We will focus on understanding cost drivers, identifying inefficiencies, and recommending strategies to optimize costs. Additionally, we will explore operational efficiency by reviewing delivery times and measure the impact of different factors on fulfillment.

## Components of the Project

The project comprises the following components:

1. **Data Preparation**: The dataset is prepared using Python for further analysis. Several columns are engineered to provide valuable insights into processing time, profit margins, unit prices, and costs.

2. **Cost Reduction Analysis**: We analyze the dataset to identify cost reduction opportunities by examining cost drivers, profit margins, and unit costs. This analysis helps uncover inefficiencies and recommends strategies to optimize costs.

3. **Operational Efficiency**: We evaluate delivery times measured by fulfillment days and shipping modes to monitor and improve operational efficiency. This analysis helps identify bottlenecks and suggests measures for improvement.

4. **Basket Analysis**: We implement a basket analysis algorithm to identify product associations and provide recommendations for cross-selling or upselling. This analysis helps maximize customer value and increase revenue.

## Advantages of Storing Data in MongoDB

We utilize Atlas MongoDB to store the dataset, which offers the following advantages:

- Flexible document-based data model that accommodates varying data structures and allows easy scaling.
- Powerful querying capabilities and rich indexing options for efficient data retrieval.
- Built-in data replication and automated backups to ensure data durability and availability.
- Integration with visualization tools like Looker to create advanced reports and interactive data visualizations.

## Getting Started

To run the code and reproduce the analysis locally, follow these steps:

1. Clone the repository:
    git clone https://github.com/your-username/papelerias-project.git
2. Install the required dependencies:
    pip install -r requirements.txt

3. Update the API token and URL in the code files (`main_script.py` and `prep_functions.py`) with your own values.

4. Run the main script:
    python main_script.py


This will initiate the data processing and upload it to the designated API.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
