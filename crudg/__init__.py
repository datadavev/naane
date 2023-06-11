"""CRUD operations on a GitHub repository

Provides a loose wrapper around pyGitHub
"""
import typing
import github
import github.GithubObject


class CRUDg:

    def __init__(self, repository: github.Repository):
        self.repo = repository

    def create(
        self,
        path: str,
        content: str,
        branch: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
    ) -> dict:
        """Create a new object at path in repo with content str.
        If branch is None self.default_branch is used.
        If message is None a default message will be generated.
        """
        if branch is None:
            branch = github.GithubObject.NotSet
        if message is None:
            message = f"CRUDg create: {path}"
        return self.repo.create_file(path, message, content, branch=branch)

    def read(self, path: str, branch: typing.Optional[str] = None) -> github.ContentFile:
        """Get the object at the specified path."""
        if branch is None:
            branch = github.GithubObject.NotSet
        return self.repo.get_contents(path, ref=branch)

    def update(
        self,
        path: str,
        content: str,
        message: typing.Optional[str] = None,
        branch: typing.Optional[str] = None,
    ) -> dict:
        """Fetch file object and update with content"""
        if message is None:
            message = f"CRUDg update."
        if branch is None:
            branch = github.GithubObject.NotSet
        file_content = self.read(path)
        return self.repo.update_file(
            file_content.path, message, content, file_content.sha, branch=branch
        )

    def delete(self, path:str, branch:typing.Optional[str] = None):
        if branch is None:
            branch = github.GithubObject.NotSet
