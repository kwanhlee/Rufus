import sys
import datetime
import git

def main(git_dir):
    repository = git.Repo(git_dir)

    # 1. Print activate branch
    print("active branch: ", repository.active_branch.name)

    # 2. Print modified file
    print("local changes: ", repository.is_dirty())

    # 3. Authored in the last week
    last_commit = repository.head.commit
    last_commit_time = datetime.datetime.fromtimestamp(last_commit.authored_date)
    time_diff = datetime.datetime.now() - last_commit_time
    is_committed_this_week = time_diff < datetime.timedelta(days=7)
    print("recent commit: ", is_committed_this_week)

    # 4. Did Rufus do it?!
    author_name = last_commit.author.name
    is_rufus = author_name == "Rufus"
    print("blame Rufus: ", is_rufus )

if __name__ == "__main__":
    main(sys.arg[1])