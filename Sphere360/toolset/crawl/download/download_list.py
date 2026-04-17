import sys

sys.path.append("..")
import core
from core import download

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-csv", type=str, required=True)
    parser.add_argument(
        "-o", "--output-dir", type=str, required=True, help="Output directory"
    )
    parser.add_argument("-j", "--jobs", type=int, default=8, help="Number of jobs")
    parser.add_argument(
        "-c", "--cookie", type=str, default=None, help="Path to cookies.txt file"
    )
    args = parser.parse_args()
    input_csv = args.input_csv
    output_dir = args.output_dir
    jobs = args.jobs
    cookie = args.cookie

    download.download_list.download_list_360(
        input_file=input_csv, output_folder=output_dir, jobs=jobs, cookie=cookie
    )
