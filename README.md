# GitHub Repository Analyzer

Ein Python-Tool zur Analyse von GitHub-Repositories über die GitHub REST API.

## 🚀 Überblick

Der GitHub Repository Analyzer ist ein Python-Script, das detaillierte Analysen von GitHub-Repositories durchführt. Es nutzt die GitHub REST API, um umfassende Informationen über Repositories zu sammeln und übersichtlich darzustellen.

## ✨ Features

- **📊 Repository-Übersicht**: Grundlegende Informationen wie Stars, Forks, Größe, Lizenz
- **💻 Programmiersprachen-Analyse**: Verteilung der verwendeten Programmiersprachen
- **👥 Contributor-Statistiken**: Top-Contributors und deren Beiträge
- **📈 Aktivitäts-Tracking**: Commit-Aktivität der letzten 30 Tage
- **🐛 Issues & Pull Requests**: Anzahl offener Issues und PRs
- **🔄 Repository-Vergleich**: Vergleich mehrerer Repositories
- **⚡ Rate Limiting**: Eingebauter Schutz vor API-Limits
- **🔐 Token-Support**: Unterstützung für GitHub Personal Access Tokens

## 🛠 Installation

### Voraussetzungen

- Python 3.6+
- `requests` Bibliothek

### Installation

1. **Repository klonen oder Script herunterladen:**
   ```bash
   git clone https://github.com/your-username/github-analyzer.git
   cd github-analyzer
   ```

2. **Abhängigkeiten installieren:**
   ```bash
   pip install requests
   ```

3. **Script ausführbar machen: (unter Linux benötigt)**
   ```bash
   chmod +x github_analyzer.py
   ```

## 🎯 Verwendung

### Basis-Verwendung

```python
from github_analyzer import GitHubAnalyzer

# Analyzer ohne Token initialisieren
analyzer = GitHubAnalyzer()

# Einzelnes Repository analysieren
analyzer.analyze_repository("microsoft", "vscode")
```

### Mit GitHub Token (empfohlen)

```python
# Mit Token für höhere Rate Limits
analyzer = GitHubAnalyzer("your_github_token_here")
analyzer.analyze_repository("facebook", "react")
```

### Repository-Vergleich

```python
repos = [
    ("microsoft", "vscode"),
    ("facebook", "react"),
    ("python", "cpython")
]

analyzer.compare_repositories(repos)
```

### Command Line Interface

```bash
python github_analyzer.py
```

## ⚙️ Konfiguration

### GitHub Token erstellen

### Token verwenden

```python
# Option 1: Direkt im Code
analyzer = GitHubAnalyzer("ghp_your_token_here")

# Option 2: Umgebungsvariable (empfohlen)
import os
token = os.getenv('GITHUB_TOKEN')
analyzer = GitHubAnalyzer(token)
```

Umgebungsvariable setzen:
```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

## 📝 Beispiele

Multiple Repositories vergleichen

```python
repos_to_compare = [
    ("microsoft", "typescript"),
    ("golang", "go"),
    ("rust-lang", "rust"),
    ("python", "cpython")
]

analyzer.compare_repositories(repos_to_compare)
```



## 🚦 API-Limits

### Rate Limits ohne Token
- **60 Requests pro Stunde** für unauthentifizierte Requests
- Geeignet für gelegentliche Nutzung

### Rate Limits mit Token
- **5,000 Requests pro Stunde** für authentifizierte Requests
- Empfohlen für regelmäßige Nutzung



### Development Setup

```bash
# Repository klonen
git clone https://github.com/your-username/github-analyzer.git
cd github-analyzer

# Virtual Environment erstellen
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder
venv\Scripts\activate  # Windows

# Dependencies installieren
pip install -r requirements.txt
```


