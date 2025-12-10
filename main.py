# main.py

from orchestration import Orchestrator
from product_data import RAW_PRODUCT_DATA


def main() -> None:
    orchestrator = Orchestrator(RAW_PRODUCT_DATA)
    result_paths = orchestrator.run()
    print("Generated pages:")
    for name, path in result_paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()