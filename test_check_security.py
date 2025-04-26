import os
import pytest
from check_security import check_files

def test_all_files_present(tmp_path, monkeypatch):
    for filename in ["LICENSE", "README.md", "requirements.txt"]:
        (tmp_path / filename).write_text("content")

    monkeypatch.chdir(tmp_path)

    check_files()

def test_missing_license(tmp_path, monkeypatch):
    (tmp_path / "README.md").write_text("content")
    (tmp_path / "requirements.txt").write_text("content")
    monkeypatch.chdir(tmp_path)

    with pytest.raises(SystemExit):
        check_files()

def test_missing_readme(tmp_path, monkeypatch):
    (tmp_path / "LICENSE").write_text("content")
    (tmp_path / "requirements.txt").write_text("content")
    monkeypatch.chdir(tmp_path)

    with pytest.raises(SystemExit):
        check_files()

def test_missing_requirements(tmp_path, monkeypatch):
    (tmp_path / "LICENSE").write_text("content")
    (tmp_path / "README.md").write_text("content")
    monkeypatch.chdir(tmp_path)

    with pytest.raises(SystemExit):
        check_files()

def test_no_files(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    with pytest.raises(SystemExit):
        check_files()
