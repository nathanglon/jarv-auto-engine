# jarv-auto-engine
Uses github.com/dorianglon/Jarv for the agentic model as it's friend. Runs auto queries on company data to probe for new correlations and insights on the company that analysts don't see and/or can't see.

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
