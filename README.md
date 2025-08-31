# GitHub Repository Analyzer

Ein Python-Tool zur Analyse von GitHub-Repositories über die GitHub REST API.

## 📋 Inhaltsverzeichnis

- [Überblick](#überblick)
- [Features](#features)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Konfiguration](#konfiguration)
- [Beispiele](#beispiele)
- [API-Limits](#api-limits)
- [Beitragen](#beitragen)
- [Lizenz](#lizenz)

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

3. **Script ausführbar machen:**
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

1. Gehe zu [GitHub Settings](https://github.com/settings/tokens)
2. Klicke auf "Developer settings" → "Personal access tokens" → "Tokens (classic)"
3. Klicke "Generate new token (classic)"
4. Wähle die folgenden Scopes:
   - `public_repo` (für öffentliche Repositories)
   - `repo` (für private Repositories, falls benötigt)
5. Kopiere den generierten Token

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

### Beispiel 1: Detaillierte Repository-Analyse

```python
from github_analyzer import GitHubAnalyzer

analyzer = GitHubAnalyzer("your_token")
analyzer.analyze_repository("torvalds", "linux")
```

**Output:**
```
🔍 Analyzing repository: torvalds/linux
==================================================
📁 Repository: torvalds/linux
📝 Description: Linux kernel source tree
🌐 URL: https://github.com/torvalds/linux
⭐ Stars: 150,000
🍴 Forks: 45,000
👀 Watchers: 150,000
📅 Created: 2011-09-16
🔄 Last Updated: 2023-12-01
📏 Size: 3,500,000 KB
⚖️ License: GPL-2.0

==================================================
🔤 Programming Languages:
   C: 97.2% (3,402,450 bytes)
   Assembly: 1.5% (52,500 bytes)
   Shell: 0.8% (28,000 bytes)
   ...
```

### Beispiel 2: Multiple Repositories vergleichen

```python
repos_to_compare = [
    ("microsoft", "typescript"),
    ("golang", "go"),
    ("rust-lang", "rust"),
    ("python", "cpython")
]

analyzer.compare_repositories(repos_to_compare)
```

### Beispiel 3: Eigene Analyse-Funktionen

```python
# Nur Contributor-Informationen abrufen
contributors = analyzer.get_contributors("owner", "repo")
for contributor in contributors[:5]:
    print(f"{contributor['login']}: {contributor['contributions']} commits")

# Nur Programmiersprachen abrufen
languages = analyzer.get_languages("owner", "repo")
print(f"Hauptsprache: {max(languages.keys(), key=languages.get)}")
```

## 🚦 API-Limits

### Rate Limits ohne Token
- **60 Requests pro Stunde** für unauthentifizierte Requests
- Geeignet für gelegentliche Nutzung

### Rate Limits mit Token
- **5,000 Requests pro Stunde** für authentifizierte Requests
- Empfohlen für regelmäßige Nutzung

### Best Practices
```python
import time

# Pause zwischen Requests einfügen
for repo in multiple_repos:
    analyzer.analyze_repository(owner, repo)
    time.sleep(1)  # 1 Sekunde Pause
```

## 🔧 Erweiterte Funktionen

### Custom Headers setzen

```python
analyzer = GitHubAnalyzer(token="your_token")
analyzer.headers["Accept"] = "application/vnd.github.v4+json"  # GraphQL API
```

### Fehlerbehandlung

```python
try:
    repo_info = analyzer.get_repo_info("owner", "repo")
    if repo_info:
        print(f"Repo gefunden: {repo_info['name']}")
    else:
        print("Repository nicht gefunden oder nicht zugänglich")
except Exception as e:
    print(f"Fehler: {e}")
```

## 🐛 Fehlerbehebung

### Häufige Probleme

1. **403 Forbidden**: Rate Limit erreicht
   ```python
   # Lösung: Token verwenden oder warten
   analyzer = GitHubAnalyzer("your_token")
   ```

2. **404 Not Found**: Repository existiert nicht
   ```python
   # Prüfe Repository-Namen und Owner
   repo_info = analyzer.get_repo_info("correct_owner", "correct_repo")
   ```

3. **Network Errors**:
   ```python
   import requests
   try:
       analyzer.analyze_repository("owner", "repo")
   except requests.exceptions.RequestException as e:
       print(f"Netzwerk-Fehler: {e}")
   ```

## 🤝 Beitragen

Beiträge sind willkommen! Hier ist, wie du helfen kannst:

1. **Fork** das Repository
2. **Branch** erstellen: `git checkout -b feature/amazing-feature`
3. **Commit** deine Änderungen: `git commit -m 'Add amazing feature'`
4. **Push** zum Branch: `git push origin feature/amazing-feature`
5. **Pull Request** erstellen

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

### Code Style

- Verwende Python PEP 8
- Füge Docstrings für alle Funktionen hinzu
- Schreibe Tests für neue Features

## 📄 Lizenz

Dieses Projekt steht unter der MIT Lizenz - siehe [LICENSE](LICENSE) Datei für Details.

## 🙏 Danksagungen

- [GitHub REST API](https://docs.github.com/en/rest) für die umfassende API
- [Requests Library](https://requests.readthedocs.io/) für HTTP-Requests
- Community-Beiträge und Feedback

## 📞 Support

Bei Fragen oder Problemen:

1. **Issues**: [GitHub Issues](https://github.com/your-username/github-analyzer/issues)
2. **Dokumentation**: [GitHub API Docs](https://docs.github.com/en/rest)
3. **Community**: [Discussions](https://github.com/your-username/github-analyzer/discussions)

---

**⭐ Wenn dir dieses Projekt gefällt, gib ihm einen Star auf GitHub!**
