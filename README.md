# SIMS-visualizaitions

This directory contains Python scripts and visualizations created in the project. These visualizations aim to provide insights into inventory trends and performance metrics derived from the MySQL database.

## Purpose
- To analyze inventory data for actionable insights.
- To visualize trends in stock levels, product categories, and supplier performance.

## Scripts
1. **`low_stock_analysis.py`**:  
   - Retrieves data on products with low stock (available quantity < 50).  
   - Outputs a histogram showing the distribution of low-stock products.

2. **`product_category_piechart.py`**:  
   - Groups products by type and visualizes the distribution as a pie chart.

3. **`supplier_performance.py`**:  
   - Calculates the average purchase price by supplier.  
   - Outputs a bar chart ranking suppliers by their average pricing.

## How to Run
1. Ensure you have installed the required libraries:  
   ```bash
   pip install pandas matplotlib seaborn mysql-connector-python
