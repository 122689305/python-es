import es_util

# input and configuration 

k = 1
yaml_path = './schema.yaml'
query = '''
    SELECT COUNT(*) FROM orders
    JOIN customers ON orders.customer_id = customers.customer_id
    JOIN products ON orders.product_id = products.product_id
    WHERE orders.product_id = 1 AND customers.address LIKE '%United States%'
'''
#    
# test body
args = (query, k, yaml_path)
result = es_util.k_ES(*args)
original_result = es_util.original_k_ES(*args)
print 'result=%f, original_result=%f'%(result, original_result)
