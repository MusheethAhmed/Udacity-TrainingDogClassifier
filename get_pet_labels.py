from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Create a list of all files in the directory
    in_files = listdir(image_dir)
    
    # Create an empty dictionary for storing results (pet labels)
    results_dic = dict()
   
    # Process each file in the directory, extracting only the relevant parts
    # of the filename to create the pet label
    for idx in range(0, len(in_files)):
       
       # Skip files that start with a period (like .DS_Store on macOS)
       if in_files[idx][0] != ".":
           
           # Create a variable to hold the pet label
           pet_label = ""

           # Split the filename by underscores and use only the alphabetic words
           # to generate the pet label (lowercased and joined with a space)
           pet_label = " ".join([word.lower() for word in in_files[idx].split('_') if word.isalpha()])

           # Check if the filename is already in the dictionary
           # If not, add it to the dictionary with the extracted pet label
           if in_files[idx] not in results_dic:
               results_dic[in_files[idx]] = [pet_label]
           else:
               print("** Warning: Duplicate files exist in directory:", in_files[idx])
 
    # Return the results dictionary with image filenames and their respective pet labels
    return results_dic
