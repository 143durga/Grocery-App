from sql_connection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.products_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
             "FROM products "
             "INNER JOIN uom ON products.uom_id = uom.uom_id")
    cursor.execute(query)

    response = []
    for (products_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'products_id': products_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    cursor.close()
    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products (name, uom_id, price_per_unit) "
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    products_id = cursor.lastrowid
    cursor.close()
    return products_id


if __name__ == '__main__':
    connection = get_sql_connection()
    products_id = insert_new_product(connection, {
        'product_name': 'cabbage',
        'uom_id': 1,
        'price_per_unit': 10
    })
    print(f"Inserted product with ID: {products_id}")
