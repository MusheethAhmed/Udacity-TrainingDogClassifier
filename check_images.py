
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER: [Musheeth Ahmed]
# DATE CREATED: [17 November 2024]
# REVISED DATE: [Date]
#
# PURPOSE: This script classifies pet images using a pretrained Convolutional Neural Network (CNN).
#          It compares predicted classifications to the true labels derived from the filenames and 
#          summarizes how well the model performs. The script allows comparison of different CNN architectures 
#          (e.g., VGG, AlexNet, ResNet).
#
# USAGE EXAMPLE:
# python check_images.py --dir <path-to-image-folder> --arch <model-architecture> --dogfile <dog-names-file>
#
# Example usage:
# python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Import necessary libraries
import time
from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    """
    Main function to orchestrate the steps for image classification:
    1. Retrieve input arguments (image directory, model architecture, dog names file).
    2. Extract pet labels from image filenames.
    3. Use a CNN model to classify images.
    4. Adjust results to identify correctly and incorrectly classified dogs.
    5. Calculate results statistics.
    6. Print the results.
    """
    
    # Measure start time
    start_time = time.time()

    # Step 1: Get command line arguments
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # Step 2: Extract pet labels from filenames
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    # Step 3: Classify images using the specified model architecture
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)

    # Step 4: Adjust results for dogs vs. non-dogs
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    # Step 5: Compute statistics on results
    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)

    # Step 6: Display results
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure end time and calculate total runtime
    end_time = time.time()
    total_runtime = end_time - start_time
    print("\n** Total Elapsed Runtime: {}:{}:{}".format(
        int(total_runtime // 3600),
        int((total_runtime % 3600) // 60),
        int(total_runtime % 60)
    ))

if __name__ == "__main__":
    main()
