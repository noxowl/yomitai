from typer.testing import CliRunner

from yomitai import __version__
from yomitai.main import app


runner = CliRunner()


def test_version():
    assert __version__ == '0.1'


def test_default():
    result = runner.invoke(app, ['炙りカルビ'])
    assert result.exit_code == 0
    assert 'あぶり かるび' in result.stdout


def test_kana():
    sample = 'アブリ カルビ'
    result = runner.invoke(app, ['炙りカルビ', '--kana'])
    assert result.exit_code == 0
    assert sample in result.stdout

    result = runner.invoke(app, ['炙りカルビ', '--k'])
    assert result.exit_code == 0
    assert sample in result.stdout


def test_romaji():
    sample = 'aburi karubi'
    result = runner.invoke(app, ['炙りカルビ', '--romaji'])
    assert result.exit_code == 0
    assert sample in result.stdout

    result = runner.invoke(app, ['炙りカルビ', '--r'])
    assert result.exit_code == 0
    assert sample in result.stdout
