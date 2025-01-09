def execute_query(query):
    """Execute a SQL query and return the results as a DataFrame."""
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return pd.DataFrame(results)


query = """
SELECT Name AS ProductName, AvailableQuantity
FROM Product
WHERE AvailableQuantity < 50
ORDER BY AvailableQuantity ASC;
"""
low_stock_data = execute_query(query)
plt.figure(figsize=(8, 5))
sns.histplot(low_stock_data["AvailableQuantity"], bins=10, kde=True, color='blue')
plt.title("Distribution of Low-Stock Products")
plt.xlabel("Available Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


query = """
SELECT Type AS ProductType, COUNT(ProductID) AS Count
FROM Product
GROUP BY ProductType;
"""
product_types_data = execute_query(query)

plt.figure(figsize=(8, 8))
plt.pie(product_types_data["Count"], labels=product_types_data["ProductType"], autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
plt.title("Product Categories in Stock")
plt.tight_layout()
plt.show()

def average_purchase_price_by_supplier():
    # Query to calculate the average purchase price by supplier
    query = """
    SELECT 
        s.Name AS SupplierName,
        AVG(p.PurchasePrice) AS AveragePurchasePrice
    FROM 
        Product p
    JOIN 
        Supplier s ON p.SupplierID = s.SupplierID
    GROUP BY 
        s.SupplierID
    ORDER BY 
        AveragePurchasePrice DESC;
    """
    # Execute the query and store the result in a DataFrame
    data = execute_query(query)

    # Debug: Print the DataFrame content
    print("Data Retrieved from Query:")
    print(data.head())

    # Check if the DataFrame is empty
    if data.empty:
        print("No data available for visualization. Check the database or query.")
        return
    
    # Create a bar chart
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data, x="AveragePurchasePrice", y="SupplierName", palette="Blues_r")
    plt.title("Average Purchase Price by Supplier")
    plt.xlabel("Average Purchase Price")
    plt.ylabel("Supplier Name")
    plt.tight_layout()
    plt.show()

# Call the function
average_purchase_price_by_supplier()
