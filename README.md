# jarv-auto-engine
Uses github.com/dorianglon/Jarv for the agentic model as it's friend. Runs auto queries on company data to probe for new correlations and insights on the company that analysts don't see and/or can't see.

Here is the project structure:

jarv-auto-engine
│
├── README.md
├── requirements.txt
├── setup.py
├── config/
│   └── config.yaml
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── knowledge_graph/
│   │   ├── __init__.py
│   │   ├── graph.py
│   │   └── relationships.py
│   │
│   ├── query_generation/
│   │   ├── __init__.py
│   │   ├── generator.py
│   │   └── validator.py
│   │
│   ├── embeddings/
│   │   ├── __init__.py
│   │   └── encoder.py
│   │
│   ├── exploration/
│   │   ├── __init__.py
│   │   ├── explorer.py
│   │   └── sampling.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── database.py
│       └── logging.py
│
├── tests/
│   ├── __init__.py
│   ├── test_knowledge_graph.py
│   ├── test_query_generation.py
│   └── test_exploration.py
│
└── notebooks/
    └── examples.ipynb


Instructions:

## Features

- Automated query pattern discovery
- Continuous learning and optimization
- Knowledge graph-based relationship mapping
- Intelligent query generation
- Performance monitoring and optimization

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

1. Copy `config/config.yaml.example` to `config/config.yaml`
2. Update the configuration with your database credentials and desired parameters

## Usage

Basic usage:

```python
from src.main import QueryExplorer

explorer = QueryExplorer()
explorer.start()
```

For detailed examples, see `notebooks/examples.ipynb`

## Testing

```bash
pytest tests/
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
