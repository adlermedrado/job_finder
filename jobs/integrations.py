from github import Github


class GithubIntegration:
    def __init__(self, github_token):
        self.client = Github(github_token)

    def fetch_issues(self, repo_name):
        repo = self.client.get_repo(repo_name)
        return [
            {'id': issue.id, 'title': issue.title, 'body': issue.body, 'url': issue.url}
            for issue in repo.get_issues(state='open')
        ]
