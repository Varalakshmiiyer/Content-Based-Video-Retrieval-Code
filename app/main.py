import argparse

from app.helpers import get_video_filenames
from app.histogram import HistogramGenerator
import app.config as settings


def main():
    """
    Program entry point. Parses command line input.
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="print values for debugging program", action="store_true")
    args = parser.parse_args()
    settings.debug = args.debug

    train_hist_classifier()
    test_hist_classifier()


def train_hist_classifier():
    """
    Generates an averaged BGR histogram for all the videos in the directory-based database.
    :return: None
    """
    directory = "../footage/"
    files = get_video_filenames(directory)

    for file in files:
        print("generating histogram for {}".format(file))
        histogram_generator = HistogramGenerator(directory, file)
        histogram_generator.generate_video_histograms()
    print("\nGenerated histograms for all files in directory {}".format(directory))


def test_hist_classifier():
    """
    Prompts the user to crop the recorded video before generating an averaged BGR histogram and comparing it with the
    other averaged histograms for matching.
    :return: None
    """
    directory = "../recordings/"
    recordings = ["recording1.mp4", "recording2.mp4", "recording3.mp4"]  # 1: cloud-sky, 2: seal, 3: butterfly
    file = recordings[0]

    # calculate histogram for the recorded video
    print("\nPlease crop the recorded video for the histogram to be generated.")
    histogram_generator = HistogramGenerator(directory, file)
    histogram_generator.generate_recording_video_histograms()
    histogram_generator.match_histograms()
    print("Finished matching video using histogram comparison technique.")


if __name__ == "__main__":
    main()
