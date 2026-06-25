# python-proxy-pattern-access-control-caching
This example demonstrates the Proxy design pattern in Python. It features a `DataServiceProxy` that controls access to a `RealDataService` based on user roles and caches fetched data to optimize performance. The proxy ensures only authorized roles can retrieve sensitive information and avoids redundant computations by serving cached results.
