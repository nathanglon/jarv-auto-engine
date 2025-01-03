import logging
from knowledge_graph.graph import KnowledgeGraph
from query_generation.generator import QueryGenerator
from exploration.explorer import QueryExplorer
from utils.database import DatabaseConnection
from utils.logging import setup_logging

class ContinuousQueryExplorer:
    def __init__(self, config_path="config/config.yaml"):
        self.config = self._load_config(config_path)
        setup_logging(self.config['logging'])
        
        self.db = DatabaseConnection(self.config['database'])
        self.knowledge_graph = KnowledgeGraph()
        self.query_generator = QueryGenerator(self.knowledge_graph)
        self.explorer = QueryExplorer(
            self.knowledge_graph,
            self.query_generator,
            self.config['exploration']
        )

    def start(self):
        """Start the continuous exploration process"""
        logging.info("Starting continuous query exploration")
        self.explorer.run_continuous_exploration()

    @staticmethod
    def _load_config(config_path):
        """Load configuration from YAML file"""
        import yaml
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
