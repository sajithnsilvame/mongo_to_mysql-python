
#  MongoDB to MySQL Data Converter

This Python script allows you to convert data from a MongoDB database to a MYSQL database.

## Getting Started

1. **Clone the project repository:**

    ```bash
    git clone https://github.com/sajithnsilvame/mongo_to_mysql-python.git
    cd mongo_to_mysql-python
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file in the project directory and add your environment variables:**

    ```
    ## after add mongo uri add '/', example - "www.mongodb.com/"

    MONGO_URI="your_mongo_uri"
    MONGO_DATABASE="your_mongo_database"

    SQL_HOST=your_sql_host
    SQL_DATABASE=your_sql_database
    SQL_USER=your_sql_user
    SQL_PASSWORD=your_sql_password

    ```

    (important: after add mongo uri add '/', example - "www.mongodb.com/")

## Convert MongoDB To MySQL Database

Using This You Can Convert Your Full MongoDB Database To MySQL Database

1. **To transfer data from all Collections into MYSQL tables:**

    ```
    python mongo_to_mysql.py

    ```

2. **To transfer data from a specific collection into MYSQL table:**

    To transfer data from a specific MongoDB collection to a MySQL table, use the following command. Replace **_products_** with the name of your collection
    ```
    python mongo_to_mysql.py --collection products
    ```
    
3. **To transfer data from all collections while skipping certain columns:**

    To transfer data from all MongoDB collections to MySQL tables while skipping certain **_columns_**, use the following command. Replace **_name,category_** with the columns you want to skip:

    ```
    python mongo_to_mysql.py --skip name,category

    ```

4. **To transfer data from a specific collection while skipping certain columns:**

    To transfer data from a specific MongoDB collection to a MySQL table while skipping certain columns, use the following command. Replace **_products_** with the name of your collection and **_name,category_** with the columns you want to skip:

    ```
    python mongo_to_mysql.py --collection products --skip name,category

    ```

# COPYRIGHT

All rights reserved by Sajith N Silva @2024

Connect with me:
- GitHub: [https://github.com/sajithnsilvame](https://github.com/sajithnsilvame)
- Twitter: [https://x.com/SajithNSilvame](https://x.com/SajithNSilvame)
- LinkedIn: [https://www.linkedin.com/in/sajith-nishantha-silva](https://www.linkedin.com/in/sajith-nishantha-silva)
- Facebook: [https://www.facebook.com/sajithnsilva.me](https://www.facebook.com/sajithnsilva.me)
- Instagram: [https://www.instagram.com/sajithnsilvame](https://www.instagram.com/sajithnsilvame)
