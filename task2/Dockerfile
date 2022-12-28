# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

#TEST
ARG RUN_TESTS=true
RUN if [ "$RUN_TESTS" = "true" ]; then (echo "\n testing \n" && python test_add.py) && (echo "test passed" && exit 0) || (echo "test failed" && exit 1); fi

# Expose port 5000
EXPOSE 5000

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "add_func.py"]
