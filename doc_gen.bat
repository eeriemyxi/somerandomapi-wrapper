sphinx-apidoc -o docs -f -e --tocfile index somerandomapi somerandomapi/endpoint.py somerandomapi/http.py somerandomapi/sync_async_handler.py
cd docs
make html