from pathlib import Path

import typer
import requests
from loguru import logger
from tqdm import tqdm

from makemore.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

DATASET_URL = "https://raw.githubusercontent.com/karpathy/makemore/master/names.txt"

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "names.txt",
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Downloading dataset...")
    for i in tqdm(range(1), total=1):
        response = requests.get(DATASET_URL)
        with open(input_path, "wb") as f:
            f.write(response.content)
    logger.info("namex.txt correctly download!")
    # -----------------------------------------


if __name__ == "__main__":
    app()
