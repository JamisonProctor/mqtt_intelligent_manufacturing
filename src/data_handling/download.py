import shutil
from pathlib import Path
import kagglehub

DATASET_SLUG = "ziya07/intelligent-manufacturing-dataset"
TARGET_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "intelligent-manufacturing-dataset"

def download_dataset():
    try:
        dataset_path = Path(kagglehub.dataset_download(DATASET_SLUG)).resolve()
    except Exception as e:
        print(f"Download failed: {e}")
        return

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    for file in dataset_path.iterdir():
        shutil.copy(file, TARGET_DIR / file.name)

if __name__ == "__main__":
    download_dataset()
