import argparse
import csv
from datetime import datetime


def skip(csv_reader, n_lines):
    for _ in range(n_lines):
        next(csv_reader)


def get_date_obj(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f%z")


def build_row(x_data, y_data, z_data, start, precision=3):
    time_delta = get_date_obj(x_data[1]) - start
    row = [
        time_delta.total_seconds(),
        round(float(x_data[0]) / 10, precision),
        round(float(y_data[0]) / 10, precision),
        round(float(z_data[0]) / 10, precision),
    ]
    return row


def extract(x_file, y_file, z_file, output_file, header_lines=3):
    with open(x_file, "r", newline="", encoding="utf-8") as x_csv, open(
        y_file, "r", newline="", encoding="utf-8"
    ) as y_csv, open(z_file, "r", newline="", encoding="utf-8") as z_csv, open(
        output_file, "w", newline="", encoding="utf-8"
    ) as output_csv:
        x_reader = csv.reader(x_csv, delimiter=";")
        y_reader = csv.reader(y_csv, delimiter=";")
        z_reader = csv.reader(z_csv, delimiter=";")
        output_writer = csv.writer(output_csv, delimiter=",")
        skip(x_reader, header_lines)
        skip(y_reader, header_lines)
        skip(z_reader, header_lines)

        # First value (start time)
        x_initial = next(x_reader)
        y_initial = next(y_reader)
        z_initial = next(z_reader)
        start = get_date_obj(x_initial[1])
        output_writer.writerow(build_row(x_initial, y_initial, z_initial, start))

        for x_data, y_data, z_data in zip(x_reader, y_reader, z_reader):
            output_writer.writerow(build_row(x_data, y_data, z_data, start))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--x_file",
        "-x",
        default="X-axis OBC magnetometer measure.csv",
        type=str,
        help="X data file path",
    )

    parser.add_argument(
        "--y_file",
        "-y",
        default="Y-axis OBC magnetometer measure.csv",
        type=str,
        help="Y data file path",
    )

    parser.add_argument(
        "--z_file",
        "-z",
        default="Z-axis OBC magnetometer measure.csv",
        type=str,
        help="Z data file path",
    )

    parser.add_argument(
        "--output_file", "-o", default="output.csv", type=str, help="Output path"
    )

    args = parser.parse_args()

    extract(args.x_file, args.y_file, args.z_file, args.output_file)
