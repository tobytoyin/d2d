from models import Document


class ObsidianDocument(Document):
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()