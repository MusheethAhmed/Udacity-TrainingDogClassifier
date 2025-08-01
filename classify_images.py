from classifier import classifier  # Import the classifier function

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. 
    
    Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain:
                  index 0 = pet image label (string)
                  --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int) where 1 = match between pet image
                            and classifier labels, 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet, alexnet, vgg (string)
              
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    # Iterate through each key (image filename) in results_dic
    for key in results_dic:
        # Create full image path to pass to the classifier function
        image_path = images_dir + key
        
        # Use classifier function to get the model label for the image
        model_label = classifier(image_path, model)
        
        # Convert the model_label to lowercase and strip leading/trailing whitespaces
        model_label = model_label.lower().strip()

        # Compare pet image label (truth) with classifier label
        truth = results_dic[key][0]
        match = 1 if truth in model_label else 0

        # Add the classifier label and match status to the results dictionary
        results_dic[key].extend([model_label, match])
