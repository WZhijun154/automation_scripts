import git
import os.path as osp
import click


@click.command()
@click.option('--url', required=True, help='URL of the repository to update')
@click.option('--path', required=True, help='Path to the repository')
def update_repo(url: str, path: str) -> bool:
    try:
        if not osp.exists(osp.join(path, '.git')):
            git.Repo.clone_from(url=url, path=path)
        else:
            # let's pull the latest version
            repo = git.Repo(path)
            repo.remotes.origin.pull()
        return True  # Update successful
    except git.exc.GitCommandError as e:
        print(f"Error updating repository: {e}")
        return False  # Update failed


if __name__ == '__main__':
    update_repo()

# usage
# python update_repo.py --url url --path path
