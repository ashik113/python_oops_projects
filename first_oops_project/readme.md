Medicine Price Retrieval System
The Medicine Price Retrieval System is a Python program designed to help users retrieve the prices of medicines based on the associated disease. It provides a convenient way to query the prices of medicines for specific diseases, making it useful for medical professionals, pharmacists, and individuals seeking information about medication costs.

Features
Medicine Class: Defines a Medicine class with attributes for Medicine Name, Batch Number, Disease, and Price.
Solution Class: Provides a method getPriceByDisease to retrieve the prices of medicines associated with a given disease.
Input Handling: Takes user input to create a list of Medicine objects and query for medicine prices based on disease.
Case Insensitive Matching: Performs case-insensitive matching for disease names to ensure accurate retrieval of prices.
Simple Interface: Offers a straightforward interface for users to input data and retrieve medicine prices.
Usage
To use the Medicine Price Retrieval System, follow these steps:

Input the number of medicines.
For each medicine, input the Medicine Name, Batch Number, Disease, and Price.
Input the disease for which you want to retrieve medicine prices.
The program will display the prices of medicines associated with the specified disease.
Example
Suppose we have a list of medicines with their associated diseases and prices as follows:

markdown
Copy code
Medicine Name    | Batch   | Disease       | Price
------------------------------------------------
Paracetamol      | 1234    | Fever         | 50
Amoxicillin      | 5678    | Infection     | 80
Omeprazole       | 9101    | Acid Reflux   | 100
If we input Fever as the disease, the program will output 50, indicating the price of Paracetamol.

Contribution
Contributions to the Medicine Price Retrieval System are welcome! If you have any suggestions, feature requests, or bug reports, please feel free to open an issue or submit a pull request on GitHub.
