# Python Proxy Pattern Access Control Caching

This example demonstrates the Proxy design pattern in Python. It features a `DataServiceProxy` that controls access to a `RealDataService` based on user roles and caches fetched data to optimize performance. The proxy ensures only authorized roles can retrieve sensitive information and avoids redundant computations by serving cached results.

## Language

`python`

## How to Run

Save the code as `main.py`. Open a terminal or command prompt in the same directory. Run the script using `python main.py`.

## Original Article

This example accompanies the Turkish article: [Proxy Tasarım Deseni: Kontrollü Erişim ve Performans Optimizasyonu](https://fatihsoysal.com/blog/?p=42829).

## License

MIT — see [LICENSE](LICENSE).
