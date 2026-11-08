from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
NEW_EXERCISES_DIR = REPO_ROOT / "new_exercises"
PRACTICED_DIR = REPO_ROOT / "practiced"


def move_exercise(file_name: str) -> Path:
    source = (NEW_EXERCISES_DIR / file_name).resolve()
    target = (PRACTICED_DIR / file_name).resolve()

    if not source.exists():
        raise FileNotFoundError(f"找不到檔案: {source}")

    if target.exists():
        raise FileExistsError(f"目標檔案已存在: {target}")

    source.rename(target)
    return target


def git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="將已檢查通過的練習題從 new_exercises 移到 practiced")
    parser.add_argument("file_name", help="例如：exercise_34.py")
    parser.add_argument("--commit", action="store_true", help="移動後自動 git add / commit")
    parser.add_argument("--push", action="store_true", help="在 --commit 後自動 push")
    args = parser.parse_args()

    try:
        moved_path = move_exercise(args.file_name)
    except (FileNotFoundError, FileExistsError) as exc:
        print(f"錯誤: {exc}")
        return 1

    print(f"已搬移: {moved_path}")

    if args.commit:
        add_result = git("add", str(moved_path.relative_to(REPO_ROOT)))
        if add_result.returncode != 0:
            print(add_result.stderr.strip() or add_result.stdout.strip())
            return add_result.returncode

        commit_message = f"Move {args.file_name} to practiced"
        commit_result = git("commit", "-m", commit_message, "-m", "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>")
        if commit_result.returncode != 0:
            print(commit_result.stderr.strip() or commit_result.stdout.strip())
            return commit_result.returncode

        print(f"已提交: {commit_message}")

        if args.push:
            push_result = git("push")
            if push_result.returncode != 0:
                print(push_result.stderr.strip() or push_result.stdout.strip())
                return push_result.returncode
            print("已推送到遠端")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
