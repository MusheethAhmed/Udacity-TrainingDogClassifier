from classifier import classifier  # Import the classifier function

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. 
    
    Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. The list will contain:
                  index 0 = pet image label (string)
                  --- index 1 & index 2 are added by this function ---
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int) where 1 = match between pet image
                            and classifier labels, 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
              
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    # Iterate through each key (image filename) in results_dic
    for key in results_dic:
        # 3a: Create full image path and call classifier function
        image_path = images_dir + key
        model_label = classifier(image_path, model)

        # 3b: Convert model_label to lowercase and strip whitespace
        model_label = model_label.lower().strip()

        # 3c: Compare pet image label to classifier label and add to results_dic
        truth = results_dic[key][0]
        if truth in model_label:
            # Add model label and match indicator (1) if labels match
            results_dic[key].extend([model_label, 1])
        else:
            # Add model label and match indicator (0) if labels don't match
            results_dic[key].extend([model_label, 0])
