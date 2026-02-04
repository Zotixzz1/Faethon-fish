import sys
import traceback


def main() -> int:
    try:
        from client.ui.app_qt import run
    except Exception as e:
        print("Failed to import application entrypoint 'client.ui.app_qt.run':", file=sys.stderr)
        print(str(e), file=sys.stderr)
        print("\nMake sure you run this from the project root (so the `client` package is on PYTHONPATH) and that all dependencies are installed (e.g. PySide6).", file=sys.stderr)
        return 2

    try:
        # If run() returns an exit code, forward it. If it calls sys.exit internally, that will raise SystemExit.
        result = run()
        if isinstance(result, int):
            return result
        return 0
    except SystemExit as e:
        # numeric exit codes from sys.exit()
        code = e.code
        if isinstance(code, int):
            return code
        return 0
    except Exception:
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
