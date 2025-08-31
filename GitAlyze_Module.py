#!/usr/bin/env python3
"""
GitHub Repository Analyzer
A tool to analyze GitHub repositories using the GitHub REST API
"""

import requests
import json
from datetime import datetime, timedelta
from collections import defaultdict
import time


class GitAlyze:
    def __init__(self, token=None):
        """
        Initialize the GitHub analyzer

        Args:
            token (str, optional): GitHub personal access token for higher rate limits
        """
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitHub-Analyzer-Python"
        }

        if token:
            self.headers["Authorization"] = f"token {token}"

    def get_repo_info(self, owner, repo):
        """Get basic repository information"""
        url = f"{self.base_url}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching repo info: {response.status_code}")
            return None

    def get_contributors(self, owner, repo):
        """Get repository contributors"""
        url = f"{self.base_url}/repos/{owner}/{repo}/contributors"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching contributors: {response.status_code}")
            return []

    def get_languages(self, owner, repo):
        """Get programming languages used in the repository"""
        url = f"{self.base_url}/repos/{owner}/{repo}/languages"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching languages: {response.status_code}")
            return {}

    def get_recent_commits(self, owner, repo, days=30):
        """Get recent commits from the last N days"""
        since_date = (datetime.now() - timedelta(days=days)).isoformat()
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        params = {"since": since_date, "per_page": 100}

        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching commits: {response.status_code}")
            return []

    def get_issues_and_prs(self, owner, repo):
        """Get open issues and pull requests"""
        issues_url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        prs_url = f"{self.base_url}/repos/{owner}/{repo}/pulls"

        # Get issues
        issues_response = requests.get(issues_url, headers=self.headers)
        prs_response = requests.get(prs_url, headers=self.headers)

        issues = issues_response.json() if issues_response.status_code == 200 else []
        prs = prs_response.json() if prs_response.status_code == 200 else []

        return issues, prs

    def analyze_repository(self, owner, repo):
        """Perform comprehensive analysis of a repository"""
        print(f"🔍 Analyzing repository: {owner}/{repo}")
        print("=" * 50)

        # Get basic repository info
        repo_info = self.get_repo_info(owner, repo)
        if not repo_info:
            print("Failed to fetch repository information")
            return

        # Basic info
        print(f"📁 Repository: {repo_info['full_name']}")
        print(f"📝 Description: {repo_info.get('description', 'No description')}")
        print(f"🌐 URL: {repo_info['html_url']}")
        print(f"⭐ Stars: {repo_info['stargazers_count']:,}")
        print(f"🍴 Forks: {repo_info['forks_count']:,}")
        print(f"👀 Watchers: {repo_info['watchers_count']:,}")
        print(f"📅 Created: {repo_info['created_at'][:10]}")
        print(f"🔄 Last Updated: {repo_info['updated_at'][:10]}")
        print(f"📏 Size: {repo_info['size']:,} KB")

        if repo_info.get('license'):
            print(f"⚖️  License: {repo_info['license']['name']}")

        print("\n" + "=" * 50)

        # Programming languages
        languages = self.get_languages(owner, repo)
        if languages:
            print("🔤 Programming Languages:")
            total_bytes = sum(languages.values())
            for lang, bytes_count in sorted(languages.items(), key=lambda x: x[1], reverse=True):
                percentage = (bytes_count / total_bytes) * 100
                print(f"   {lang}: {percentage:.1f}% ({bytes_count:,} bytes)")

        print("\n" + "=" * 50)

        # Contributors
        contributors = self.get_contributors(owner, repo)
        if contributors:
            print(f"👥 Contributors ({len(contributors)} total):")
            for i, contributor in enumerate(contributors[:10]):  # Show top 10
                print(f"   {i + 1}. {contributor['login']}: {contributor['contributions']} contributions")
            if len(contributors) > 10:
                print(f"   ... and {len(contributors) - 10} more contributors")

        print("\n" + "=" * 50)

        # Recent activity
        recent_commits = self.get_recent_commits(owner, repo, days=30)
        if recent_commits:
            print(f"📊 Recent Activity (Last 30 days): {len(recent_commits)} commits")

            # Analyze commit frequency by author
            commit_authors = defaultdict(int)
            for commit in recent_commits:
                if commit['author']:
                    commit_authors[commit['author']['login']] += 1

            print("   Most active contributors:")
            for author, count in sorted(commit_authors.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"   - {author}: {count} commits")

        # Issues and PRs
        issues, prs = self.get_issues_and_prs(owner, repo)
        print(f"🐛 Open Issues: {len([i for i in issues if 'pull_request' not in i])}")
        print(f"🔀 Open Pull Requests: {len(prs)}")

        print("\n" + "=" * 50)
        print("✅ Analysis complete!")

    def compare_repositories(self, repos):
        """Compare multiple repositories"""
        print("📊 Repository Comparison")
        print("=" * 60)

        repo_data = []
        for owner, repo in repos:
            info = self.get_repo_info(owner, repo)
            if info:
                repo_data.append(info)
                time.sleep(0.1)  # Rate limiting

        if not repo_data:
            print("No repository data found")
            return

        # Print comparison table
        print(f"{'Repository':<30} {'Stars':<8} {'Forks':<8} {'Size (KB)':<12} {'Language':<15}")
        print("-" * 80)

        for repo in sorted(repo_data, key=lambda x: x['stargazers_count'], reverse=True):
            name = repo['full_name'][:29]
            stars = f"{repo['stargazers_count']:,}"
            forks = f"{repo['forks_count']:,}"
            size = f"{repo['size']:,}"
            language = repo.get('language', 'Unknown')[:14]

            print(f"{name:<30} {stars:<8} {forks:<8} {size:<12} {language:<15}")


def main():

    analyzer = GitAlyze()  # Add your token here: GitHubAnalyzer("your_token_here")

    print("GitHub Repository Analyzer")
    print("=" * 30)

   #Examples
    print("\n1. Single Repository Analysis:")
    analyzer.analyze_repository("microsoft", "vscode")


    print("\n\n2. Repository Comparison:")
    repos_to_compare = [
        ("microsoft", "vscode"),
        ("facebook", "react"),
        ("python", "cpython"),
        ("torvalds", "linux")
    ]
    analyzer.compare_repositories(repos_to_compare)


if __name__ == "__main__":
    main()